#!/usr/bin/env python

even = set([0, 2, 4, 6, 8])
print(even)

hello = set("Hello")
print(hello)

p = even & hello
print(p)

even.add(10)
print(even)

hello.remove('e')
print(hello)

s1 = set([1,2,3,4,5])
s2 = set([4,5,6,7,8])

# intersection
print(s1.intersection(s2))
print(s1 &s2)

dic = {'a':1, 'b':2, 'c':3, 'd':4, 'e':5}
dic.keys()