import sys
from pprint import pprint
from collections import deque

def move(data, pos, direction):
    global N, M
    
    if direction == "up":
        x = pos[0]
        y = pos[1]
        while x >= 0:
            if data[x-1][y] == ".":
                data[x-1][y] = data[x][y]
                data[x][y] = "."
                x -= 1
                
            elif data[x-1][y] == "O":
                data[x][y] = "."
                return (-1, -1)
            
            else:
                return (x, y)
            
    elif direction == "down":
        x = pos[0]
        y = pos[1]
        while x < N:
            if data[x+1][y] == ".":
                data[x+1][y] = data[x][y]
                data[x][y] = "."
                x += 1
                
            elif data[x+1][y] == "O":
                data[x][y] = "."
                return (-1, -1)
            
            else:
                return (x, y)
            
    elif direction == "left":
        x = pos[0]
        y = pos[1]
        while y >= 0:
            if data[x][y-1] == ".":
                data[x][y-1] = data[x][y]
                data[x][y] = "."
                y -= 1
                
            elif data[x][y-1] == "O":
                data[x][y] = "."
                return (-1, -1)
            
            else:
                return (x, y)
            
    elif direction == "right":
        x = pos[0]
        y = pos[1]
        while y < M:
            if data[x][y+1] == ".":
                data[x][y+1] = data[x][y]
                data[x][y] = "."
                y += 1
                
            elif data[x][y+1] == "O":
                data[x][y] = "."
                return (-1, -1)
            
            else:
                return (x, y)
            

def moveBall(data, redPos, bluePos, direction):
    global N, M
    newMap = []
    
    # data를 deep copy
    for i in range(N):
        line = []
        for j in range(M):
            line.append(data[i][j])
            
        newMap.append(line)
    
    if direction == "up":
        # 파란 공이 더 위에 있을 때
        if bluePos[0] < redPos[0]:
            bluePos = move(newMap, bluePos, "up")
            redPos = move(newMap, redPos, "up")
        # 빨간 공이 더 위에 있을 때
        else:
            redPos = move(newMap, redPos, "up")
            bluePos = move(newMap, bluePos, "up")
            
    elif direction == "down":
        # 파란 공이 더 아래에 있을 때
        if bluePos[0] > redPos[0]:
            bluePos = move(newMap, bluePos, "down")
            redPos = move(newMap, redPos, "down")
        # 빨간 공이 더 아래에 있을 때
        else:
            redPos = move(newMap, redPos, "down")
            bluePos = move(newMap, bluePos, "down")
    
    elif direction == "left":
        # 파란 공이 더 왼쪽에 있을 때
        if bluePos[1] < redPos[1]:
            bluePos = move(newMap, bluePos, "left")
            redPos = move(newMap, redPos, "left")
        # 빨간 공이 더 왼쪽에 있을 때
        else:
            redPos = move(newMap, redPos, "left")
            bluePos = move(newMap, bluePos, "left")
    
    elif direction == "right":
        # 파란 공이 더 오른쪽에 있을 때
        if bluePos[1] > redPos[1]:
            bluePos = move(newMap, bluePos, "right")
            redPos = move(newMap, redPos, "right")
        # 빨간 공이 더 오른쪽에 있을 때
        else:
            redPos = move(newMap, redPos, "right")
            bluePos = move(newMap, bluePos, "right")
            
    return newMap, redPos, bluePos

N, M = list(map(int, sys.stdin.readline().strip().split()))

data = []

for i in range(N):
    line = [x for x in sys.stdin.readline().strip()]
    if line.count("R") != 0:
        redPos = (i, line.index("R"))
    
    if line.count("B") != 0:
        bluePos = (i, line.index("B"))
    
    data.append(line)
    
visited = {}
queue = deque()
queue.appendleft([data, redPos, bluePos, 0])
visited[redPos, bluePos] = 1

possible = False

while queue and not possible:
    [data, redPos, bluePos, numMove] = queue.pop()
    
    for direction in ["up", "down", "left", "right"]:
        newMap, newRedPos, newBluePos = moveBall(data, redPos, bluePos, direction)
        
        if newRedPos == (-1, -1) and newBluePos != (-1, -1):
            possible = True
            break
        elif newRedPos != (-1, -1) and newBluePos != (-1, -1) and numMove < 9 and (newRedPos, newBluePos) not in visited.keys():
            queue.appendleft([newMap, newRedPos, newBluePos, numMove + 1])
            visited[newRedPos, newBluePos] = 1
            
if possible:
    print(1)
else:
    print(0)
