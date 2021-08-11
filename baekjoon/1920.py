import sys

def binary_search(data, start, end, f):
    if start > end:
        return 0
    
    mid = (start + end) // 2
    
    if data[mid] == f:
        return 1
    
    if f > data[mid]:
        return binary_search(data, mid+1, end, f)
    
    else:
        return binary_search(data, start, mid-1, f)
    

N = int(input())

data = list(map(int, sys.stdin.readline().strip().split()))

data.sort()

M = int(input())

f = list(map(int, sys.stdin.readline().strip().split()))

for target in f:
    print(binary_search(data, 0, N-1, target))
    


