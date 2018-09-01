#!/bin/python3

import os
import sys

#
# Complete the timeConversion function below.
#
def timeConversion(s):
    le = len(s);
    st = s[le-2] + s[le-1];
    st2 = s[0]+s[1];
    
    if st == "PM":
        st2 = int(st2);
        if st2 != 12:
            st2 = st2 +12;
    else:
        if st2 == "12":
            st2 = '00';
    i =2;
    x = "";
    while i<len(s)-2:
        x = x + s[i];
        i = i+1;
    s = str(st2) + x;
    return s;

if __name__ == '__main__':
    f = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = timeConversion(s)

    f.write(result + '\n')

    f.close()
