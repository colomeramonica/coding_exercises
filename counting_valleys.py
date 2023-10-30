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


def countingValleys(steps, path):
    valley = 0
    level = 0

    for i in range(steps):
        if path[i] == 'U':
            level += 1
        elif path[i] == 'D':
            level -= 1

        if level == 0 and path[i] == 'U':
            valley += 1

    return valley


if __name__ == '__main__':
    steps = 8
    path = ['UDDDUDUU']

    print(countingValleys(steps, path))
