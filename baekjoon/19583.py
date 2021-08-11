import sys

def compareTwoTime(time1, time2):
    time1 = time1.split(":")
    time2 = time2.split(":")
    
    # time1 >= time2 return 1
    if int(time1[0]) > int(time2[0]):
        return 1
    
    elif int(time1[0]) == int(time2[0]) and int(time1[1]) >= int(time2[1]):
        return 1
    
    else:
        return 0

inputText = []
checkList = {}
cnt = 0

inputText = sys.stdin.readlines()

S, E, Q = inputText[0].strip().split()

for idx, line in enumerate(inputText):
    if idx == 0 or line == "\n":
        continue
    
    time = line.split()[0]
    name = line.split()[1]
    
    if compareTwoTime(S, time):
        checkList[name] = 1
    
    if compareTwoTime(time, E) and compareTwoTime(Q, time):
        if name in checkList.keys() and checkList[name] == 1:
            cnt += 1
            checkList[name] += 1
              
print(cnt)
