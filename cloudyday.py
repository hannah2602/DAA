#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'maximumPeople' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts following parameters:
#  1. LONG_INTEGER_ARRAY p
#  2. LONG_INTEGER_ARRAY x
#  3. LONG_INTEGER_ARRAY y
#  4. LONG_INTEGER_ARRAY r
#

def maximumPeople(p, x, m, c, r):
    n = len(p)
    events = []
    
    for i in range(m):
        events.append((c[i] - r[i], 'start', i))
        events.append((c[i] + r[i] + 1, 'end', i))
    
    for i in range(n):
        events.append((x[i], 'town', i))
    
    events.sort()
    
    active_clouds = set()
    cloud_population = [0] * m
    town_sunny_population = [0] * n
    total_sunny = 0
    
    for event in events:
        position, event_type, index = event
        if event_type == 'start':
            active_clouds.add(index)
        elif event_type == 'end':
            active_clouds.remove(index)
        elif event_type == 'town':
            if len(active_clouds) == 0:
                total_sunny += p[index]
            elif len(active_clouds) == 1:
                cloud_population[list(active_clouds)[0]] += p[index]
    
    max_sunny_with_one_removed = total_sunny + max(cloud_population, default=0)
    return max_sunny_with_one_removed

# Input reading
n = int(input().strip())
p = list(map(int, input().strip().split()))
x = list(map(int, input().strip().split()))
m = int(input().strip())
c = list(map(int, input().strip().split()))
r = list(map(int, input().strip().split()))

print(maximumPeople(p, x, m, c, r))

