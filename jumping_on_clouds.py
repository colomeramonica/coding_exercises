#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'countingValleys' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER steps
#  2. STRING path
#


def jumpingOnClouds(c):
    cumulus = []

    for i in range(len(c)):
        if c[i] == 0:
            cumulus.append(i)

    for i in range(len(cumulus)):
        if (i < len(cumulus) - 1 and cumulus[i+1] - cumulus[i] == 1):
            cumulus.pop(cumulus[i])

    return len(cumulus)


if __name__ == '__main__':
    c = [0, 1, 0, 0, 0, 1, 0]

    print(jumpingOnClouds(c))
