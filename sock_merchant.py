#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'sockMerchant' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER_ARRAY ar
#


def sockMerchant(n, ar):
    sock_count = {}
    pairs = 0

    for sock in ar:
        if sock in sock_count:
            sock_count[sock] += 1
        else:
            sock_count[sock] = 1

    for count in sock_count.values():
        pairs += count // 2

    return pairs


if __name__ == '__main__':
    n = 9
    ar = [10, 20, 20, 10, 10, 30, 50, 10, 20]

    response = sockMerchant(n, ar)

    print(response)
