import sys

N, M, B = list(map(int, sys.stdin.readline().strip().split()))

dataMap = []
sumMap = []

for _ in range(N):
    dataMap += list(map(int, sys.stdin.readline().strip().split()))
    
dataMap.sort()
minValue = dataMap[0]
maxValue = dataMap[-1]

for idx, data in enumerate(dataMap):
    if idx == 0:
        sumMap.append(data)
    else:
        sumMap.append(sumMap[-1] + data)

index = 0
time = -1
height = -1
        
for value in range(minValue, maxValue + 1, 1):
    while index < len(dataMap):
        if dataMap[index] <= value:
            index += 1
            
        else:
            index -= 1
            break
    
    if index == len(dataMap):
        index -= 1
    
    
    # 높이를 맞추기 위해 채워야할 블록 수
    needs = (value * (index + 1)) - sumMap[index]
    
    # 높이를 맞추기 위해 빼야할 블록 수
    extracts = (sumMap[-1] - sumMap[index]) - (value * (N*M - index - 1))
    
    # 있는거에 비해 채워야 할게 많다면 return
    if B + extracts < needs:
        break
    
    # Initial
    if time == -1:
        time = (extracts) * 2 + needs
        height = value
    
    else:
        if time >= (extracts) * 2 + needs:
            time = (extracts) * 2 + needs
            height = value
        
print(time, height)
