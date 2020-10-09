# PyPy3로 채점
import sys
from pprint import pprint


def clean(data, curX, curY, order, R, C, limitMin, limitMax):
    startX, startY = curX, curY
    moveX, moveY = order.pop()
    while True:
        if curX + moveX == startX and curY + moveY == startY:
            data[curX][curY] = 0
            break
        elif limitMin <= curX + moveX <= limitMax and 0 <= curY + moveY < C:
            data[curX][curY] = data[curX + moveX][curY + moveY]
            curX += moveX
            curY += moveY
        else:
            moveX, moveY = order.pop()
            
        

movement = [[-1, 0], [1, 0], [0, -1], [0, 1]]

R, C, T = list(map(int, sys.stdin.readline().strip().split()))

dataMap = []

for _ in range(R):
    dataMap.append(list(map(int, sys.stdin.readline().strip().split())))

# T초 후
for _ in range(T):
    
    newMap = [[0] * C for _ in range(R)]
    
    # 미세먼지 전파
    for i in range(R):
        for j in range(C):
            if dataMap[i][j] > 0:
                newMap[i][j] += dataMap[i][j]
                
                # 전파되는 양
                A = dataMap[i][j] // 5;
                
                for x, y in movement:
                    if 0 <= i + x < R and 0 <= j + y < C and dataMap[i+x][j+y] != -1:
                        newMap[i][j] -= A
                        newMap[i+x][j+y] += A

    # 공기 정청기로 빨아들임
    
    # 반시계 방향 // 끝에서 부터 끌어당기게 설정
    antiClockwise = [[0, -1],[1, 0],[0, 1],[-1, 0]]
    # 시계방향
    clockwise = [[0, -1],[-1, 0],[0, 1],[1, 0]]
    
    # 공기청정기 위치 찾기
    for i in range(R):
        if dataMap[i][0] == -1:
            xcor, ycor = i, 0
            break
    
    # 위에필터 먼저 빨아들이기
    clean(newMap, xcor, ycor, antiClockwise, R, C, 0, xcor)
    # 아래필터 빨아들이기
    clean(newMap, xcor+1, ycor, clockwise, R, C, xcor+1, R-1)
    
    newMap[xcor][ycor] = -1
    newMap[xcor+1][ycor] = -1
    
    dataMap = newMap
    
total = 0

for i in range(R):
    for j in range(C):
        if dataMap[i][j] != -1:
            total += dataMap[i][j]

print(total)
    
                        
