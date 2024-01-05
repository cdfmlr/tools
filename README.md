# My Tools

Personal tools: simple and useful.

Notice: some programs here were hard-coded for my own convenience. However, you can easily  tailor constants to fit your jobs.

## Setup

Just add the `active.sh` into your `~/.zshrc`:

```sh
source /path/to/tools/active.sh
```

Then all tools wil be ready.

## protnum

Convert a date (e.g. 23-12-31) to a port number (e.g. 23721). The process of transformation is reversible.

Usage:

```sh
protnum [YY-MM-DD]
        Default: today
```

## makegitignore

A command to fill `./.gitignore` with templates from [github.com/github/gitignore](https://github.com/github/gitignore).

Usage:

```sh
$ makegitignore [-h] [--default-envs] [--favorite] [--macos]
                         [--jetbrains] [--visualstudiocode] [--virtualenv]
                         [--c] [--go] [--python] [--node] [--lang LANG]
                         [--env ENV]
```

Run `makegitignore --help` for more details.


E.g.

```sh
$ makegitignore -d --go --lang Swift --lang TeX --env Windows
```

## f2utf8

Any text file to UTF-8.

```sh
f2utf8.py [-h] [-o OUTFILE] file

convert file to utf-8 encoded

positional arguments:
  file

optional arguments:
  -h, --help            show this help message and exit
  -o OUTFILE, --outfile OUTFILE
```

## ignore_folders_in_spotlight

[SUDO] Make spotlight ignoring folders:

```sh
ignore_folders_in_spotlight [-h] [-n NAME] [-s SPOTLIGHT_PLIST_PATH] path

Ignore a path in Spotlight

positional arguments:
  path                  Path to ignore

optional arguments:
  -h, --help            show this help message and exit
  -n NAME, --name NAME  Name of the path to ignore
  -s SPOTLIGHT_PLIST_PATH, --spotlight-plist-path SPOTLIGHT_PLIST_PATH
                        Path to the Spotlight plist
```

e.g. ignore all node_modules:

```sh
ignore_folders_in_spotlight -n node_modules /
```

## httpserve

A simple static http server with CORS allowed:

```sh
httpserve [-h] [--cgi] [--bind ADDRESS] [--directory DIRECTORY] [port]

positional arguments:
  port                  specify alternate port (default: 8000)

optional arguments:
  -h, --help            show this help message and exit
  --cgi                 run as CGI server
  --bind ADDRESS, -b ADDRESS
                        specify alternate bind address (default: all interfaces)
  --directory DIRECTORY, -d DIRECTORY
                        specify alternate directory (default: current directory)
```

e.g.

```sh
httpserve -d ./myweb 8000
```

## httpstatic

A golang alternative to `httpserve`, with better performance (maybe) and more features (e.g. 206).


```sh
httpstatic -d . -l :8080
```

Serving static files from a directory (`.`) over HTTP (`:8080`) with CORS allowed.
Notice the arguments are different from `httpserve`.

⚠️ Build before use (TODO: make a global Makefile for any required tools later):

```sh
cd ./httpstatic && make
```

## cloudflareTunnelHealth

This script is used to check whether a CF tunnel is alive.

```sh
cloudflareTunnelHealth <tunnel name or id>
```

Stdout:

- "OK: ..."   if tunnel is all right
- "ERROR ..." if tunnel dead or program error

Return value:
    
- 0: (200) OK: tunnel alive
- 1: (400) argv error
- 2: (417) ERROR: tunnel dead
- 3: (500) unexpected error

## emsend

Send emails.

```sh
emsend [-f SENDER] [-p PASSWORD] [-m SMTP_HOST] [-t RECEIVERS]
       [-s SUBJECT] [-c CONTENT] [-a ATTACHMENTS] [-S SIGNATURE]

Send email.

optional arguments:
  -h, --help            show this help message and exit
  -f SENDER, --from SENDER
                        Sender email address. Default: None (set by MYEMAIL_SENDER)
  -p PASSWORD, --password PASSWORD
                        Sender email password. Default: None (set by MYEMAIL_PASSWORD)
  -m SMTP_HOST, --smtp SMTP_HOST
                        SMTP host. Default: None (set by MYEMAIL_SMTP_HOST)
  -t RECEIVERS, --to RECEIVERS
                        Receiver email address. Multiple receivers can be specified by
                        multiple -t options: -t receiver1 -t receiver2
  -s SUBJECT, --subject SUBJECT
                        subject, default: "No subject"
  -c CONTENT, --content CONTENT
                        content in plain text. Default: read from stdin
  -a ATTACHMENTS, --attachment ATTACHMENTS
                        attachment file path. Multiple attachments can be specified by
                        multiple -a options: -a attachment1 -a attachment2
  -S SIGNATURE, --signature SIGNATURE
                        signature, default: "<sender> <current time>"
```

example:

```sh
emsend -f foo@bar.com -p greetPassW0rd -m smtp.bar.com -t fuzz@buzz.com -s 'A test email'
<content from stdin>
```

```sh
export MYEMAIL_SENDER=foo@bar.com
export MYEMAIL_PASSWORD=greetPassW0rd
export MYEMAIL_SMTP_HOST=smtp.bar.com
emsend -t fuzz@buzz.com -a hello.jpg -c hello.txt
emsend --help | emsend -t fuzz@buzz.com -s 'emsend help'
```

## cfddns

A python client used to update dynamic DNS entries on Cloudfalre.

```
usage: cfddns [-h] --token TOKEN --zone ZONE --name NAME --type TYPE [--content CONTENT | --autoconf-tmp-ipv6]
              --proxied [--verbose]

optional arguments:
  -h, --help           show this help message and exit
  --verbose            verbose output.

Cloudflare configure:
  --token TOKEN        bearer token
  --zone ZONE          zone identifier

Record to be updated:
  --name NAME          DNS record name (or @ for the zone apex) in Punycode. Example: example.com
  --type TYPE          Record type. Example: AAAA
  --content CONTENT    A valid IPv6 address. Example: 2400:cb00:2049::1
  --autoconf-tmp-ipv6  Use an autoconf temporary IPv6 address from ifconfig as content.
  --proxied            Whether the record is receiving the performance and security benefits of Cloudflare.
```

References:

- DDNS: https://www.cloudflare.com/learning/dns/glossary/dynamic-dns/
- DNS Record Detail API: https://developers.cloudflare.com/api/operations/dns-records-for-a-zone-dns-record-details
- Update DNS Record API: https://developers.cloudflare.com/api/operations/dns-records-for-a-zone-update-dns-record


## minidocker

> no longer maintained

This script helps to start a docker demon by running `minikube start -p no-k8s-docker` and setting up docker env: `eval $(minikube -p no-k8s-docker docker-env)`.

Usage:

```sh
$ minidocker {start,stop}
```

## others

All kinds of clutter. Read the source code before using.

## private

Very personal tools that are not suitable for public.
