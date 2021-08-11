import sys
from collections import deque

M, N, H = list(map(int, sys.stdin.readline().strip().split()))

mapDict = {}
notRiped = 0

for i in range(H):
    mapDict[i] = []
    for _ in range(N):
        inputList = list(map(int, sys.stdin.readline().strip().split()))
        mapDict[i].append(inputList)
        notRiped += inputList.count(0)
    
queue = deque()
for k in mapDict.keys():
    for i in range(N):
        for j in range(M):
            if mapDict[k][i][j] == 1:
                queue.appendleft((i, j, k, 0))

directions = [[1, 0, 0], [0, 1, 0], [0, 0, 1], [-1, 0, 0], [0, -1, 0], [0, 0, -1]]
possible = False

if notRiped == 0:
    print(0)
    queue = []
    possible = True

while queue:
    i, j, k, day = queue.pop()
    
    for direction in directions:
        
        i2 = i+direction[0]
        j2 = j+direction[1]
        k2 = k+direction[2]
        
        if 0 <= i2 < N and 0 <= j2 < M and 0 <= k2 < H and mapDict[k2][i2][j2] == 0:
            queue.appendleft((i2, j2, k2, day + 1))
            notRiped -= 1
            mapDict[k2][i2][j2] = -1
            
    if notRiped == 0:
        print(day+1)
        possible = True
        break  

if not possible:
    print(-1)
