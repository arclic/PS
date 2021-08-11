import sys

N, M, V = list(map(int, sys.stdin.readline().split()))
data = []

DFS = [] # Stack
BFS = [] # Queue

for _ in range(M):
    data.append(list(map(int, sys.stdin.readline().split())))


# DFS 수행
DFS.append(V)
DFS_order = []
DFS_order.append(str(V))
visited = []
visited.append(V)

while DFS:
    minValue = 2000
    head = DFS[-1]
    for i, j in data:
        if i == head and j not in visited and j < minValue:
            minValue = j
        
        if j == head and i not in visited and i < minValue:
            minValue = i
    
    if minValue == 2000:
        DFS.pop()
    
    else:
        DFS.append(minValue)
        DFS_order.append(str(minValue))
        visited.append(minValue)
        
print(" ".join(DFS_order))

# BFS 수행
BFS.append(V)
BFS_order = []
visited = []
visited.append(V)

while BFS:
    head = BFS.pop()
    BFS_order.append(str(head))
    values = []
    
    for i, j in data:
        if i == head and j not in visited:
            values.append(j)
            visited.append(j)
        
        if j == head and i not in visited:
            values.append(i)
            visited.append(i)
        
    values.sort(reverse = True)
    BFS = values + BFS

print(" ".join(BFS_order))
