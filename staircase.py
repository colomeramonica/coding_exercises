#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'staircase' function below.
#
# The function accepts INTEGER n as parameter.
#

def staircase(n):
    spaces = ' '
    symbol = '#'
    
    for i in range(n, 0, -1):
        print(f"{(i - 1)* spaces}{(n - i + 1) * symbol}")

if __name__ == '__main__':
    n = 6

    print(staircase(n))
