#!/bin/python3

import math
import os
import random
import re
import sys


def reverseArray(a):
    b = []
    for i in range(len(a) - 1, -1, -1):
        b.append(a[i])
        
    return b


if __name__ == '__main__':
    nums = [0,1,2,2,3,0,4,2]

    print(reverseArray(nums))
