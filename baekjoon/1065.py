import sys

N = int(sys.stdin.readline())

cnt = 0 

for i in range(1, 10, 1):
    number = []
    if i <= N:
        cnt += 1
    else:
        break
    for j in range(0, 10, 1):
        number = [str(i), str(j)]
        diff = j - i
        while True:
            if int("".join(number)) <= N:
                cnt += 1
            else:
                break
                
            if (int(number[-1]) + diff) < 0 or (int(number[-1]) + diff) > 9:
                break
            else:
                number.append(str(int(number[-1]) + diff))
                
print(cnt)
