import sys

N = int(sys.stdin.readline().strip())


# 양수, 음수, 0
plus = []
minus = []
zero = False

for _ in range(N):
    num = int(sys.stdin.readline().strip())
    if num > 0:
        plus.append(num)
    
    elif num < 0:
        minus.append(num)
    
    else:
        zero = True
    
plus.sort(reverse = True)
minus.sort()
            
maxSum = 0
tied = False

for idx, num in enumerate(plus):
    if tied:
        tied = False
        continue
    
    if idx == len(plus) - 1:
        maxSum += num
    
    else:
        if num > 1 and plus[idx + 1] > 1:
            maxSum += (num * plus[idx + 1])
            tied = True
        
        else:
            maxSum += num
        
for idx, num in enumerate(minus):
    if tied:
        tied = False
        continue
    
    if idx == len(minus) - 1:
        if not zero:
            maxSum += num
    
    else:
        maxSum += (num * minus[idx + 1])
        tied = True
            
print(maxSum)
        
