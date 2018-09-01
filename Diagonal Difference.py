#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the diagonalDifference function below.
def diagonalDifference(arr):
    row = len(arr);
    col = len(arr[0]);
    sum_row = 0;
    sum_col = 0;
    i=0;
    j=0;
    #for i,j in zip(row, column):
    while i<row:
        sum_row = sum_row + arr[i][j];
        i = i+1;
        j = j+1;
    
    i = 0;
    j = col-1;
    while i<row:
        sum_col = sum_col +arr[i][j];
        i = i + 1;
        j = j-1;
    
    sum = abs(sum_row - sum_col);
    return sum;
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    result = diagonalDifference(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
