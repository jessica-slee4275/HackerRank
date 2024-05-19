"""
input
4
73
67
38
33

>>>
Every student receives a grade in the inclusive range from 0 to 100.
Any grade less than 40 is a failing grade.
73 -> round to 75
67 -> don't round
38 -> round 40
33 -> round to 35, but less than 40 -> keep 33

output
75
67
40
33
"""

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
    # Write your code here

    new_grades = []
    
    for grade in grades:
        ceil_grade = int(math.ceil(grade/5))*5
        if ceil_grade < 40 or ceil_grade-grade >= 3:
            new_grades.append(grade)
        else:
            new_grades.append(ceil_grade)
    return new_grades

    # new_grades = []
    # for grade in grades:
    #     next_multiple = (grade//5+1)*5
    #     if next_multiple < 40 :
    #         new_grades.append(grade)
    #     elif next_multiple - grade < 3:
    #         new_grades.append(next_multiple)
    #     else:
    #         new_grades.append(grade)
    # return new_grades

if __name__ == '__main__':

    grades_count = int(input().strip())

    grades = []

    for _ in range(grades_count):
        grades_item = int(input().strip())
        grades.append(grades_item)

    result = gradingStudents(grades)

    print('\n'.join(map(str, result)))
