#!/usr/bin/env python 
### shhhhhhhhhhhhhhhhhhahbooya!!

"""
Input the fly.txt file to this script.
When running this script use:
./hw1.py < fly.txt | cat > conversion_list

The output is a file named conversion_list to be used 
to cross reference with the .ctab file


"""


import sys
import string

drome_list =[]

for cat in sys.stdin:
    if "DROME" in cat:
        fields = cat.rstrip( "\r\n" ).split()
        numcol = len(fields)
        if numcol == 4:
            drome_list.append( fields[2:4] )
        if numcol == 5:
            drome_list.append( fields[3:5] )
    else:
        continue
print '\n'.join(map('\t'.join,drome_list))
 
