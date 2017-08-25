from __future__ import print_function
import sys

# This script replaces the pattern '[0x02][0x00]*[one extra char]'
# with '[arg]' from the input stream, where arg is the first arg
# given to the command.

try:
    strip = False
    while True:
        c = sys.stdin.read(1)
        if len(c) < 1:
            break  # End of file reached.
        elif ord(c) == 2:
            print("[" + sys.argv[1] + "] ", end='')
            strip = True  # On 0x02 print tag and start stripping.
        elif strip:
          if ord(c) != 0:
            strip = False  # If 0x00 strip it, if not skip first char and stop stripping.
        else:
            print(c, end='')  # Print regular chars when not in strip mode.
except KeyboardInterrupt:
    pass
