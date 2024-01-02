#!/usr/bin/python3
"""
A python client used to update dynamic DNS entries on Cloudfalre.

References:

  - DDNS: https://www.cloudflare.com/learning/dns/glossary/dynamic-dns/
  - DNS Record Detail API: https://developers.cloudflare.com/api/operations/dns-records-for-a-zone-dns-record-details
  - Update DNS Record API: https://developers.cloudflare.com/api/operations/dns-records-for-a-zone-update-dns-record
"""

import json
import argparse
import subprocess
import http.client
from dataclasses import dataclass
from typing import Optional


@dataclass
class Record:
    """ Cloudflare DNS Record """
    name: str     # "example.com"
    type: str     # "A"
    content: str  # "198.51.100.4"
    proxied: bool # False


def cloudflare_request(token: str, method: str, url: str, body: Optional[str] = None):
    conn = http.client.HTTPSConnection("api.cloudflare.com")

    headers = {
        'Content-Type': "application/json",
        'Authorization': f"Bearer {token}",
        }

    conn.request(method, url, body, headers)

    res = conn.getresponse()
    data = res.read()

    j = json.loads(data)

    if not j.get('result', False):
        raise ValueError(j)

    return j['result']


def get_dns_records(token: str, zone_id: str) -> dict:
    return cloudflare_request(token,
            "GET", f"/client/v4/zones/{zone_id}/dns_records")


def update_dns_record(token: str, zone_id: str, record_id: str, updated: Record):
    return cloudflare_request(token,
            "PUT", f"/client/v4/zones/{zone_id}/dns_records/{record_id}", 
             body=json.dumps(updated.__dict__))


def get_autoconf_temp_ipv6() -> str:
    """designed for macOS 13.3"""

    # check=True: do assert
    subprocess.run('test "$(uname)" = "Darwin"', shell=True, check=True)

    #for req_cmd in ['ifconfig', 'grep', 'cut']:
    #    w = subprocess.run(f'which {req_cmd}', shell=True, capture_output=True)
    #    print(f'[DBG] which {req_cmd}: {w.stdout.decode()}')

    
    cmd = '''/sbin/ifconfig en1 | \
             /usr/bin/grep inet6 | \
             /usr/bin/grep "autoconf temporary" | \
             /usr/bin/grep --invert-match "deprecated" | \
             /usr/bin/cut -d " " -f 2'''
    run = subprocess.run(cmd, shell=True, capture_output=True)
    ips = run.stdout.decode().strip()
    print(f'[DBG] {ips=}')
    return ips.split('\n')[-1]


def cli() -> argparse.Namespace:
    parser = argparse.ArgumentParser(prog='cfddns', description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)

    group_cloudflare = parser.add_argument_group('Cloudflare configure')

    group_cloudflare.add_argument('--token', type=str, help="bearer token", required=True)
    group_cloudflare.add_argument('--zone', type=str, help="zone identifier", required=True)

    group_update = parser.add_argument_group('Record to be updated')

    group_update.add_argument('--name', type=str, required=True, 
                              help="DNS record name (or @ for the zone apex) in Punycode. Example: example.com")
    group_update.add_argument('--type', type=str, required=True, 
                              help="Record type. Example: AAAA")
    
    content_mutex = group_update.add_mutually_exclusive_group()
    
    content_mutex.add_argument('--content', type=str, 
                              help="A valid IPv6 address. Example: 2400:cb00:2049::1")
    content_mutex.add_argument('--autoconf-tmp-ipv6', action='store_true', 
                              help="Use an autoconf temporary IPv6 address from ifconfig as content.")

    group_update.add_argument('--proxied', action='store_true', required=True, 
                              help="Whether the record is receiving the performance and security benefits of Cloudflare.")

    parser.add_argument('--verbose', action='store_true', help="verbose output.")

    args = parser.parse_args()
    # print(args)
    return args


if __name__ == "__main__":
    args = cli()
    
    updated = Record(
            name=args.name, 
            type=args.type, 
            content=args.content or get_autoconf_temp_ipv6(), 
            proxied=args.proxied)

    records = get_dns_records(args.token, args.zone)
    if args.verbose:
        print("Get records from Cloudflare zone:\n", records)

    record = [r for r in records if r.get('name') == updated.name]

    assert len(record) == 1
    record = record[0]

    if args.verbose:
        print("\nRecord to be updated:\n", record)
        print("Updated record:\n", updated, "\n")

    if record['content'] == updated.content:
        print('Record is already up-to-date.')
        exit(0)


    result = update_dns_record(args.token, args.zone, record['id'], updated)
    if args.verbose:
        print('Updated:\n', result)

