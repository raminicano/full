#!/usr/bin/env python

mynum = [1,2,3,4,5]

def square_number(nums):
    while nums <= max(mynum):
        yield nums ** 2
    return

for i in mynum:
    num = square_number(i)
    print(f"Square number: {i} ^ {i} : {next(num)}")

