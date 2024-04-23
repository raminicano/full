#!/usr/bin/env python

import random

class findMax(object):
    def __init__(self, li):
        self.li = li
        self.max = 0

    def findMax(self):
        self.max = self.li[0]
        for i in range(len(self.li)):
            if self.li[i] > self.max:
                self.max = self.li[i]

        return self.max

data = random.sample(range(1, 101), 10)
print(data)
x = findMax(data)
print(x.findMax())