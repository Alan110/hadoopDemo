#! /usr/local/bin/python3

import sys

data = {};

for line in sys.stdin:
    words = line.strip()
    word,count = words.split('\t')

    count = int(count)
    if  word not in data:
        data[word] = 1
    else:
        data[word] += 1

print (data)
