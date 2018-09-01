#!/bin/python3

import os
import sys

#
# Complete the gradingStudents function below.
#
def gradingStudents(grades):
    count =0;
    #grades = list(filter(lambda x: x > 37, grades));
    for i in range(len(grades)):
        if grades[i]>37:
            for j in range(5):
                temp = grades[i];
                temp = temp + j;
                if temp%5 != 0:
                    count = count + 1;
                else:
                    if count < 3:
                        grades[i] = grades[i] + count;
        count= 0;
    return grades;

if __name__ == '__main__':
    f = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    grades = []

    for _ in range(n):
        grades_item = int(input())
        grades.append(grades_item)

    result = gradingStudents(grades)

    f.write('\n'.join(map(str, result)))
    f.write('\n')

    f.close()
