#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'formingMagicSquare' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY s as parameter.
#

def formingMagicSquare(s):
   elementsSum = []
   mainDiag = 0
   secondDiag  = 0
   for row in s:
       lineSum = sum(row)
       elementsSum.append(lineSum) 
       
   for i in range(len(s)):
        for j in range(len(s)):
            if i == j:
                mainDiag += s[i][j]
            if i + j == len(s) - 1:
                secondDiag += s[i][j]
    
   elementsSum.append(mainDiag)
   elementsSum.append(secondDiag)
   
   hightestValue = max(elementsSum)
   index = []
   
   for element in elementsSum:
       index.append(hightestValue - element)
    
   return min(index)

if __name__ == '__main__':
    s = [[5, 3, 4], [1, 5, 8], [6, 4, 2]]

    result = formingMagicSquare(s)

    print(result)