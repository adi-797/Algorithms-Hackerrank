#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the miniMaxSum function below.
def miniMaxSum(arr):
    sum1 =0;
    sum2 =0;
    a = sorted(arr);
    b = sorted(arr, reverse =True);
    for i in range(4):
        sum1 = sum1 + b[i];
        sum2 = sum2 + a[i];
    print(str(sum2) + " " + str(sum1));

if __name__ == '__main__':
    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)
