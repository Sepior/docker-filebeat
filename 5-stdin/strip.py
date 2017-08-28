from __future__ import print_function
import sys
import re

# This script strips away the pattern '[0x02][0x00]*[one extra char]'
# from the input stream. It also replaces any 0x02 with '\n'.
 
# try:
#     strip = False
#     while True:
#         c = sys.stdin.read(1)
#         if len(c) < 1:
#             break  # End of file reached.
#         elif ord(c) == 2:
#             print()
#             strip = True  # On 0x02 start stripping.
#         elif strip:
#             if ord(c) != 0:
#                 strip = False  # If 0x00 strip it, if not skip first char and stop stripping.
#         else:
#             print(c, end='')  # Print regular chars when not in strip mode.
# except KeyboardInterrupt:
#     pass



# This script inserts the tag 'FNUT[TAG]TUNF' at every line beginning
# that matches '[.*].*'
PRE = r'filebeat'
POST = r'beatfile'
TAG = PRE + sys.argv[1] + POST

def is_part_of_multiline_msg(line):
    return re.match(r'\s', line, re.UNICODE)

try:
    buf = []
    skip_next = False
    while True:
        c = sys.stdin.read(1)
        if len(c) < 1:
            break  # End of file reached.
        elif ord(c) in [0, 1, 2]:
            skip_next = True  # Skip first real char after one of these.
        else:
            if skip_next:
                skip_next = False
            else:
                if ord(c) == 10:
                    line = "".join(buf)
                    if is_part_of_multiline_msg(line):
                        print(line)
                    else:
                        print(TAG + line)  # We print the container name only at beginning of new message.
                    buf = []
                else:
                    buf.append(c)
except KeyboardInterrupt:
    pass
