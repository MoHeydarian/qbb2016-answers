#!/usr/bin/env python

import sys
import string


count = 0
for line in sys.stdin:
    if line.startswith( "@" ):
        continue
    fields = line.rstrip( "\r\n" ).split( "\t" )
    for field in fields[12:]:
        subfields = field.split( ":")
        if subfields [0] == "NM":
            if subfields [2] =="0":
                count+=1    

print count
        