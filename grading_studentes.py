#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'gradingStudents' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY grades as parameter.
#

def gradingStudents(grades):
    rounded_grades = []
    
    totalGrades = grades[0]
    grades = grades[1:]
    for i in range(totalGrades):
        closest_multiple = round(grades[i] / 5) * 5
        
        if (closest_multiple > grades[i] and closest_multiple - grades[i] < 3 and grades[i] >= 38):
            rounded_grades.append(closest_multiple)
            continue
            
        rounded_grades.append(grades[i])
        
    return rounded_grades

if __name__ == '__main__':
    grades = [4, 73, 67, 38, 33]

    result = gradingStudents(grades)
    print(result)

