import sys

def check(data, number, numberDict):
    value = 1
    for i in range(12):
        for j in range(6):
            if data[i][j] != "." and number[i][j] == 0:
                count = 1
                queue = []
                queue.append((i, j))
                number[i][j] = value
                
                while queue:
                    (x, y) = queue.pop()
                    
                    # 상, 하, 좌, 우 확인
                    if x - 1 >=0 and data[x][y] == data[x-1][y] and number[x-1][y] == 0:
                        number[x-1][y] = value
                        count += 1
                        queue.append((x-1, y))
                    
                    if x + 1 < 12 and data[x][y] == data[x+1][y] and number[x+1][y] == 0:
                        number[x+1][y] = value
                        count += 1
                        queue.append((x+1, y))
                    
                    if y - 1 >=0 and data[x][y] == data[x][y-1] and number[x][y-1] == 0:
                        number[x][y-1] = value
                        count += 1
                        queue.append((x, y-1))
                        
                    if y + 1 < 6 and data[x][y] == data[x][y+1] and number[x][y+1] == 0:
                        number[x][y+1] = value
                        count += 1
                        queue.append((x, y+1))
                numberDict[value] = count
                value += 1

dataMap = []

for _ in range(12):
    dataMap.append([x for x in sys.stdin.readline().strip()])
    
stop = False
result = 0

while not stop:
    
    numberMap = [[0] * 6 for i in range(12)]
    numberDict = {}
    check(dataMap, numberMap, numberDict)
    
    stop = True
    
    for k in numberDict.keys():
        if numberDict[k] >= 4:
            stop = False
            for i in range(12):
                for j in range(6):
                    if numberMap[i][j] == k:
                        dataMap[i][j] = '.'
    if stop:
        break
                        
    for _ in range(6):
        col = [a[_] for a in dataMap]
        col = [x for x in "".join(col).replace(".", "").zfill(12).replace("0", ".")]
        for i in range(12):
            dataMap[i][_] = col[i]
            
    result += 1
    
print(result)
