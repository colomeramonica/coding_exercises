#!/bin/python3

import math
import os
import random
import re
import sys


def removeElement(nums, val):
    n = len(nums) - 1
    for i in range(n):
        if (nums[i] == val):
            nums.remove(nums[i])
            n = len(nums) - 1

    return len(nums)


if __name__ == '__main__':
    nums = [0,1,2,2,3,0,4,2]
    val = 2

    print(removeElement(nums, val))
