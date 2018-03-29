#!/usr/bin/python

import sys

salesTotal = 0
items = 0
oldkey = None

for line in sys.stdin:
	data_mapped = line.strip().split("\t")  
	if len(data_mapped) != 2:
        # Something has gone wrong. Skip this line.
        	continue
	

	thiskey,thissale = data_mapped

	if oldkey != None and oldkey != thiskey:
		print oldkey,"\t",float(salesTotal)/float(items)
		oldkey = thiskey
		salesTotal = 0
		items = 0
	
	oldkey = thiskey
	salesTotal = salesTotal + float(thissale)
	items = items +1

if oldkey != None:
    print oldkey, "\t Mean: ", float(salesTotal)/float(items)
	
	
