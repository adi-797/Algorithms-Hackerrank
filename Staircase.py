#!/bin/python3

import  math
import os
import random
import re
import sys

# Complete the staircase function below.
def staircase(n):
    i = 0;
    j = 0;
    k = 0;
    st = "";
    st2 = "";
    while i<n:
        while j<n-1-i:
            st = st + " ";
            j=j+1;
            
        while k<i+1:
            st2 = st2 + "#";
            k=k+1;
            
        print(st + st2);
        st="";
        st2="";
        j=0;
        k=0;
        i = i+1;
        

if __name__ == '__main__':
    n = int(input())

    staircase(n)
