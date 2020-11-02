import sys

N, M = list(map(int, sys.stdin.readline().strip().split()))

MAP = []

for _ in range(N):
    MAP.append([_ for _ in sys.stdin.readline().strip()])
    

visited = [[0 for _ in range(M)] for _ in range(N)]

bfs = []
bfs.append((0, 0, 1))
visited[0][0] = 1

while bfs:
    i, j, depth = bfs.pop()
    
    if i == N-1 and j == M-1:
        print(depth)
        break
    
    if  0 <= j+1 < M and visited[i][j+1] == 0 and MAP[i][j+1] == "1":
        bfs.insert(0, (i, j+1, depth + 1))
        visited[i][j+1] = 1
    
    if  0 <= i+1 < N and visited[i+1][j] == 0 and MAP[i+1][j] == "1":
        bfs.insert(0, (i+1, j, depth + 1))
        visited[i+1][j] = 1
        
    if  0 <= j-1 < M and visited[i][j-1] == 0 and MAP[i][j-1] == "1":
        bfs.insert(0, (i, j-1, depth + 1))
        visited[i][j-1] = 1
        
    if  0 <= i-1 < N and visited[i-1][j] == 0 and MAP[i-1][j] == "1":
        bfs.insert(0, (i-1, j, depth + 1))
        visited[i-1][j] = 1
        
    
