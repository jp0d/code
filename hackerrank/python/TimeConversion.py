#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'timeConversion' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#
def timeConversion(s):
    # Write your code here
    if s[8:] == 'PM':
        if int(s[:2]) == 12:
            s = str(int(s[:2])) + s[2:8]
        else:
            str(int(s[:2]) + 12) + s[2:8]
    else:
        str(int(s[:2]) - 12) + s[2:8]
        
    print(s)
    
    return s
        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = timeConversion(s)

    fptr.write(result + '\n')

    fptr.close()