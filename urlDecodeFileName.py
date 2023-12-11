"""
Decode url-encoded file name.

usage: ls *.epub | urlDecodeFileName
"""

import os
import sys
import urllib.parse

for line in sys.stdin:
    filename = line.strip()
    decoded = urllib.parse.unquote(filename)
    print(f'{filename} => {decoded}')
    os.rename(filename, decoded)

