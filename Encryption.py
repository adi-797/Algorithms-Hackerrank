#!/bin/python

import math
import os
import random
import re
import sys

# Complete the encryption function below.
def encryption(s):
    s.replace(" ","");
    r = "";
    cols = int(math.floor(math.sqrt(len(s))));
    rows = int(math.ceil(math.sqrt(len(s))));
    if cols * rows < len(s):
        cols += 1
    for i in xrange(rows):
        for j in xrange(cols):
            if j * rows + i < len(s):
                r += s[j * rows + i]
            else:
                r += '';
        r += ' '
    print r;


    
if __name__ == '__main__':

    s = raw_input()

    result = encryption(s)
