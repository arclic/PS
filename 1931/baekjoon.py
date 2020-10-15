import sys

N = int(sys.stdin.readline().strip())
data = []
for _ in range(N):
    data.append(list(map(int, sys.stdin.readline().strip().split())))
    
data.sort(key=lambda x : x[0])
data.sort(key=lambda x : x[1])

maxEndTime = data[-1][1]

mem = [0] * (maxEndTime + 1)

cnt = 0

for value in range(maxEndTime + 1):
    if cnt < len(data) and value == data[cnt][1]:
        while cnt < len(data) and value == data[cnt][1]:
            if value > 0:
                mem[value] = max(mem[value], mem[value - 1])
            mem[value] = max(mem[value], mem[data[cnt][0]] + 1)
            cnt += 1
    
    else:
        if value != 0:
            mem[value] = max(mem[value], mem[value - 1])
            
print(mem[maxEndTime])
