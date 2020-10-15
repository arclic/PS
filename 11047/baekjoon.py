import sys

N, K = list(map(int, sys.stdin.readline().strip().split()))

data = []

for _ in range(N):
    data.append(int(sys.stdin.readline().strip()))

cnt = 0
   
for idx in range(N-1, -1, -1):
    cnt += (K // data[idx])
    K %= data[idx]
    
print(cnt)

