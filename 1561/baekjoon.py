import sys
import math
    
N, M = list(map(int, input().split()))
TIME = list(map(int, sys.stdin.readline().strip().split()))

left = 1
right = N * 30

while left <= right:
    mid = (left + right) // 2

    count = 0
    closest = 0
    closestCount = 0
    
    for t in TIME:
        count += int(math.ceil(mid/t))
        
        if ((mid-1)//t) * t > closest:
            closest = ((mid-1)//t) * t
    
    for t in TIME:
        closestCount += int(math.ceil(closest/t))
    
    if closestCount < N <= count:
        break
    
    if count > N:
        right = mid - 1
        
    else:
        left = mid + 1

for idx, t in enumerate(TIME, 1):
    if closest % t == 0:
        closestCount += 1

    if closestCount == N:
        print(idx)
        break
