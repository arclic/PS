import sys

N = int(sys.stdin.readline().strip())
P = sorted(list(map(int, sys.stdin.readline().strip().split())))

result = 0

for i, data in enumerate(P):
    result += data * (N - i)
    
print(result)
