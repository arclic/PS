import sys

def getValue(cor):
    global dataMap
    value = 0
    
    for x, y in cor:
        if x >= 0 and x < N and y >= 0 and y < M:
            value += dataMap[x][y]
        else:
            return -1
    
    return value
    
N, M = list(map(int, sys.stdin.readline().strip().split()))

dataMap = []

for i in range(N):
    dataMap.append(list(map(int, sys.stdin.readline().strip().split())))
    
maxValue = 0

for i in range(N):
    for j in range(M):
        # 일자 블록
        maxValue = max(maxValue, getValue([(i, j), (i, j+1), (i, j+2), (i, j+3)]))
        maxValue = max(maxValue, getValue([(i, j), (i+1, j), (i+2, j), (i+3, j)]))
        
        # 네모 블록
        maxValue = max(maxValue, getValue([(i, j), (i, j+1), (i+1, j), (i+1, j+1)]))
        
        # L자 블록 - 대칭
        maxValue = max(maxValue, getValue([(i, j), (i+1, j), (i+2, j), (i+2, j+1)]))
        maxValue = max(maxValue, getValue([(i, j), (i+1, j), (i+2, j), (i+2, j-1)]))
        maxValue = max(maxValue, getValue([(i, j), (i+1, j), (i+2, j), (i, j+1)]))
        maxValue = max(maxValue, getValue([(i, j), (i, j+1), (i+1, j+1), (i+2, j+1)]))
        
        # L자 블록 - 회전
        maxValue = max(maxValue, getValue([(i, j), (i+1, j), (i+1, j+1), (i+1, j+2)]))
        maxValue = max(maxValue, getValue([(i, j), (i, j+1), (i, j+2), (i+1, j)]))
        maxValue = max(maxValue, getValue([(i, j), (i+1, j), (i+1, j-1), (i+1, j-2)]))
        maxValue = max(maxValue, getValue([(i, j), (i, j+1), (i, j+2), (i+1, j+2)]))
        
        # 어긋난 블록
        maxValue = max(maxValue, getValue([(i, j), (i+1, j), (i+1, j+1), (i+2, j+1)]))
        maxValue = max(maxValue, getValue([(i, j), (i+1, j), (i+1, j-1), (i+2, j-1)]))
        maxValue = max(maxValue, getValue([(i, j), (i, j+1), (i+1, j), (i+1, j-1)]))
        maxValue = max(maxValue, getValue([(i, j), (i, j+1), (i+1, j+1), (i+1, j+2)]))
        
        # ㅗ 블록
        maxValue = max(maxValue, getValue([(i, j), (i, j+1), (i, j+2), (i+1, j+1)]))
        maxValue = max(maxValue, getValue([(i, j), (i+1, j), (i+1, j+1), (i+2, j)]))
        maxValue = max(maxValue, getValue([(i, j), (i+1, j), (i+1, j-1), (i+2, j)]))
        maxValue = max(maxValue, getValue([(i, j), (i+1, j), (i+1, j+1), (i+1, j-1)]))
        
print(maxValue)
