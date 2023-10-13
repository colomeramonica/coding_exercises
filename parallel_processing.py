#!/bin/python3

import math
import os
import random
import re
import sys



#
# Complete the 'minTime' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY files
#  2. INTEGER numCores
#  3. INTEGER limit
#

def minTime(files, numCores, limit):
    n = files[0]
    
    files = files[1:]
    files.sort(reverse = True)

    for i in range(n):
        if (numCores > 1):
            if (files[i] % numCores == 0):
                files[i] = int(files[i] / numCores)
            if (limit > 1):
                continue
            break
    return sum(files)
             
                
if __name__ == '__main__':

    files = [5, 4, 1, 3, 2, 8]
    numCores = 4
    limit = 1

    result = minTime(files, numCores, limit)
    
    print(result)
