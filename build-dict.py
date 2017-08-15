#!/usr/bin/python3

import sys

base = sys.argv[1]
num = int(sys.argv[2])

for i in range(1, num):
    print(base+str(i))
