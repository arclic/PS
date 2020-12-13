import sys

K, N = list(map(int, sys.stdin.readline().strip().split()))

LAN = []
left = 1
right = 0

result = 0

for _ in range(K):
    value = int(sys.stdin.readline().strip())
    LAN.append(value)
    if right < value:
        right = value
        
while left <= right:
    mid = (left + right) // 2
    
    count = 0
    
    for i in range(K):
        count += LAN[i]//mid
    
    if count >= N:
        if result < mid:
            result = mid
            
        left = mid + 1
    
    elif count < N:
        right = mid - 1
    
print(result)
