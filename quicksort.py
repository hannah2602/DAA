#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'quickSort' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def quickSort(arr):
    pivot = arr[0]  # Pivot element, always the first element in arr
    left = []
    equal = []
    right = []
    
    for num in arr:
        if num < pivot:
            left.append(num)
        elif num == pivot:
            equal.append(num)
        else:
            right.append(num)
    
    return left + equal + right

if __name__ == '__main__':
    n = int(input().strip())
    arr = list(map(int, input().rstrip().split()))

    result = quickSort(arr)

    print(' '.join(map(str, result)))


