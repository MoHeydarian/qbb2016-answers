#!/usr/bin/env python

import sys
import string


count = 0
for line in sys.stdin:
    if line.startswith( "@" ):
        continue
    fields = line.rstrip( "\r\n" ).split( "\t" )

    if fields [2] == "*":
        pass
    else:
        count+=1

print count
        