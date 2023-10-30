#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'repeatedString' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts following parameters:
#  1. STRING s
#  2. LONG_INTEGER n
#


def repeatedString(s, n):
    freq = 0
    string = list(s)
    for i in range(0, n - len(s)):
        string.append(string[i])

    for i in range(len(string)):
        if (string[i] == 'a'):
            freq += 1
    return freq


if __name__ == '__main__':
    s = 'a'
    n = 10

    print(repeatedString(s, n))
