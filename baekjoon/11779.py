import sys

n = int(sys.stdin.readline().strip())
m = int(sys.stdin.readline().strip())

dist = [ [float('inf')] * (n+1) for _ in range(n+1)]

path = [(float('inf'), -1)] * (n+1)
visited = [0] * (n+1)

for _ in range(m):
    u, v, w = list(map(int, sys.stdin.readline().strip().split()))
    if w < dist[u][v]:
        dist[u][v] = w
    
s, e = list(map(int, sys.stdin.readline().strip().split()))

path[s] = (0, -1)
visited[s] = 1

while s != e:
    minValue = float('inf')
    
    for i in range(1, n+1):
        if path[s][0] + dist[s][i] < path[i][0]:
            path[i] = (path[s][0] + dist[s][i], s)
    
        if visited[i] == 0 and minValue > path[i][0]:
            minValue = path[i][0]
            nextS = i
            
    visited[nextS] = 1
    s = nextS

print(path[e][0])
route = []
r = path[e][1]
route.append(str(e))

while r != -1:
    route.append(str(r))
    r = path[r][1]
    
print(len(route))
print(" ".join(reversed(route)))
