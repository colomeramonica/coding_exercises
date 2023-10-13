#!/bin/python3

import math
import os
import random
import re
import sys



#
# Complete the 'decryptPassword' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def decryptPassword(s):
    password = list(s)
    i = 0

    while (i < len(password)):
        if (password[i].islower() and password[i+1].isupper()):
            password[i], password[i+1] = password[i+1], password[i]
            password.insert(i+2, '*')
            i += 2
            continue

        if (password[i].isnumeric()):
            password.insert(0, password[i])
            password.insert(i, '0')

        i += 1

    return ''.join(password)

if __name__ == '__main__':
    s = 'hAck3rr4nk'

    result = decryptPassword(s)
    
    print(result)
