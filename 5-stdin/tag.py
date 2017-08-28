from __future__ import print_function
import sys
import re

# This script inserts the tag 'FNUT[TAG]TUNF' at every line beginning
# that matches '[.*].*'
PRE = r'filebeat'
POST = r'beatfile'
TAG = PRE + sys.argv[1] + POST

while True:
    line = sys.stdin.readline()
    line = re.sub(r'\A(\[.*?\])', TAG + r'\1', line)
    #matches = re.search(r'\A(\[.*?\])', line)
    #if matches:
    #    print('Match:', matches.group(1))
    print(line)
