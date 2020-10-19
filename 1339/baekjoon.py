# 주영
import sys

N = int(sys.stdin.readline().strip())

# Input Data들
rawInput = []

# 알파벳 - 숫자 쌍
alphabet = {}
matching = {}

for _ in range(N):
    inChar = sys.stdin.readline().strip()
    rawInput.append(inChar)
    for idx, dt in enumerate(reversed(inChar), 1):
        if dt not in alphabet.keys():
            alphabet[dt] = 10**(idx-1)
        else:
            alphabet[dt] += 10**(idx-1)
        
res = sorted(alphabet.items(), key=lambda x: x[1], reverse=True)

value = 9

for key, _ in res:
    matching[key] = value
    value -= 1

SUM = 0
    
for inputData in rawInput:
    for key, value in matching.items():
        inputData = inputData.replace(key, str(value))
    
    SUM += int(inputData)

print(SUM)
