import sys
from pprint import pprint

N = int(sys.stdin.readline().strip())

data = []

# movements
movements = [[-1, 0], [0, -1], [0, 1], [1, 0]]

# 상어의 현재 위치
curX = -1
cury = -1

# 상어의 현재 크기
curSize = 2

# 상어가 현재 먹은 물고기 수
curAte = 0

# 흘러간 시간
totalTime = 0

for _ in range(N):
    data.append(list(map(int, sys.stdin.readline().strip().split())))
    if 9 in data[-1]:
        curX = _
        curY = data[-1].index(9)

# 엄마불러야 하나?
momCall = False

while not momCall:
    momCall = True
    
    added = []
    added.append((curX, curY))
    queue = []
    queue.append((curX, curY, 0))
    
    minDistance = 1000
    minX = 100
    minY = 100
    
    while queue:
        x, y, dist = queue.pop()
        
        if 0 < data[x][y] < curSize and (x != curX or y != curY) :
            if (dist <= minDistance):
                minDistance = dist
                
                if minX > x:
                    minX = x
                    minY = y
                    
                elif minX == x and minY > y:
                    minY = y
                    
            else:
                break
        
        for moveX, moveY in movements:
            if 0 <= x + moveX < N and 0 <= y + moveY < N and (x + moveX, y + moveY) not in added and data[x + moveX][y + moveY] <= curSize:
                added.append((x + moveX, y + moveY))
                queue.insert(0, (x + moveX, y + moveY, dist + 1))
    
    if minDistance != 1000:
        totalTime += minDistance
        momCall = False
        curAte += 1
        data[curX][curY] = 0
        curX = minX
        curY = minY

        if curAte == curSize:
            curSize += 1
            curAte = 0
                
print(totalTime)
        
