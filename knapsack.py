#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'unboundedKnapsack' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER k
#  2. INTEGER_ARRAY arr
#

def unboundedKnapsack(k, arr):
    n = len(arr)
    dp = [0] * (k + 1)
    
    for i in range(1, k + 1):
        for j in range(n):
            if arr[j] <= i:
                dp[i] = max(dp[i], dp[i - arr[j]] + arr[j])
    
    return dp[k]

if __name__ == '__main__':
    t = int(input().strip())  # Number of test cases
    
    for _ in range(t):
        n, k = map(int, input().strip().split())
        arr = list(map(int, input().strip().split()))
        
        result = unboundedKnapsack(k, arr)
        print(result)
