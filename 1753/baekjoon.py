import sys

V, E = list(map(int, sys.stdin.readline().strip().split()))
K = int(input())

adj = {}

for i in range(1, V+1):
    adj[i] = []
    
for _ in range(E):
    u, v, w = list(map(int, sys.stdin.readline().strip().split()))
    adj[u].append((v, w))
    
minPath = [-1] * (V + 1)
visited = [0] * (V + 1)

minPath[K] = 0
visited[K] = 1

done = False

while not done:
    done = True
    
    for v, w in adj[K]:
        if minPath[v] == -1 or minPath[v] > minPath[K] + w:
            minPath[v] = minPath[K] + w
            
    minValue = float('inf')
    
    for i in range(1, V+1):
        if visited[i] == 0 and minPath[i] != -1 and minPath[i] < minValue:
            minValue = minPath[i]
            K = i
            done = False
            
    visited[K] = 1
    
for i in range(1, V+1):
    if  minPath[i] == -1:
        print("INF")
    else:
        print(minPath[i])
            
    
