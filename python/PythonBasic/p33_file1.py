#!/usr/bin/env python

f = open('test.txt', 'w')
line = 1
while line:
    line = f.readline()
print(line)

f.close()
