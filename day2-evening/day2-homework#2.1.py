#!/usr/bin/env python

"""
This file will map the identifiers to a new file that has all the c_tab data as well as the identifiers
to run it, the first file following this .py script should be the list of names, and will be made into a dictonary
the second file following .py script should be the c_tab file, and IMPORTANTLY the third input should be "0" or "1".

Options for third input: to retrieve only the transcripts with corresponding UniProt IDs enter "0", to retrieve all transcripts (and indicate non-coding transcripts) eneter "1". 
"""

import sys

drome_list = open(sys.argv[1])
c_tab = open(sys.argv[2])
flavor = sys.argv[3]

new_file = []

dic={}
for line in drome_list.readlines():
    cut=line.rstrip().split('\t')
    dic[cut[1]]=cut[0]
    # this is reading the tab delmited file and then making it into our dictionary, named dic
#for i in dic:
    #print i, dic[i]
    # this is a way to print out and read our dic to make sure it is right

if flavor == "0":

    for entry in c_tab.readlines():
        feilds = entry.rstrip('\r\n').split("\t")
        #print feilds
        FB_id = feilds[8]
        if FB_id not in dic:
            print "\t".join(feilds) +'\t'
            #new_file.append( feilds[0:12] )
        else:
            print "\t".join(feilds) +'\t' + dic[FB_id]
            #new_file.append( feilds[0:12].join(dic[FB_id] ) )

else:
    for entry in c_tab.readlines():
        feilds = entry.rstrip('\r\n').split("\t")
        #print feilds
        FB_id = feilds[8]
        if FB_id not in dic:
            print "\t".join(feilds) +'\t' + "Non-coding"
            #new_file.append( feilds[0:12] )
        else:
            print "\t".join(feilds) +'\t' + dic[FB_id]
            #new_file.append( feilds[0:12].join(dic[FB_id] ) )
    
#strip_file = new_file.rstrip('\r\n').split("\t")
#print '\t'.join(new_file)
#for i in new_file:
#    print i
    
"""    
    #print: file
import sys

drome_list = []

for line in sys.stdin:
    if "DROME" in line:
        feilds = line.rstrip( "\r\n" ).split( )
    #strip the feilds in each line and split them delimited by blank space
        numcol = len(feilds)
        if numcol == 4:
            drome_list.append( feilds [2:4] )
        if numcol == 5:
            drome_list.append( feilds [3:5])
    
print '\n'.join(map('\t'.join,drome_list))
"""