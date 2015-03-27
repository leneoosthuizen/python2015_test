#!/usr/bin/env python

import sys

#sys.path.append(~/Document/python/python2015_test/bin/)

def count_name(filename, protein_name):
    input_file = open(filename)
    count = 0
    for line in input_file:
        if line.rstrip() == protein_name:
            count += 1
    return count

if len(sys.argv) != 3:
    sys.exit("Usage: count_name.py <protein names file> <protein name>")

filename = sys.argv[1]
protein_name = sys.argv[2]
name_count = count_name(filename, protein_name)

print protein_name, name_count


