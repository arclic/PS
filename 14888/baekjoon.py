import sys

def operation(a, b, operator):
    if operator == 0:
        return a + b
    elif operator == 1:
        return a - b
    elif operator == 2:
        return a * b
    else:
        if a < 0:
            return (abs(a)//b) * (-1)
        else:
            return a // b

def calculate(numbers, operators):
    result = 0
    
    for idx, operator in enumerate(operators):
        if idx == 0:
            result = operation(numbers[0], numbers[1], operator)
        else:
            result = operation(result, numbers[idx + 1], operator)
            
    return result
        

N = int(sys.stdin.readline().strip())
A = list(map(int, sys.stdin.readline().strip().split()))
operator = list(map(int, sys.stdin.readline().strip().split()))

# 연산자 queue
queue = []

minValue = 2e9
maxValue = -2e9

for idx in range(4):
    if operator[idx] != 0:
        queue.insert(0, [idx])

while queue:
    poped = queue.pop()
    
    # 모든 연산자가 다 있을 경우
    if len(poped) == N-1:
        result = calculate(A, poped)
        if result < minValue:
            minValue = result
        
        if result > maxValue:
            maxValue = result
        
    else:
        for idx in range(4):
            if poped.count(idx) < operator[idx]:
                queue.insert(0, poped + [idx])
                
print(maxValue)
print(minValue)
