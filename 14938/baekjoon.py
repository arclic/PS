import sys

n, m, r = list(map(int, sys.stdin.readline().strip().split()))

items = [0] + list(map(int, sys.stdin.readline().strip().split()))

dist = [[float('inf')] * (n+1) for _ in range(n+1)]

for _ in range(r):
    a, b, i = list(map(int, sys.stdin.readline().strip().split()))
    dist[a][b] = dist[b][a] = i
    
for k in range(1, n+1):
    for i in range(1, n+1):
        for j in range(1, n+1):
            if i == j:
                dist[i][j] = 0
                
            if dist[i][j] > dist[i][k] + dist[k][j]:
                dist[i][j] = dist[i][k] + dist[k][j]
                
maxItem = 0

for i in range(1, n+1):
    total = 0
    
    for j in range(1, n+1):
        if dist[i][j] <= m:
            total += items[j]
            
    if maxItem < total:
        maxItem = total

print(maxItem)
