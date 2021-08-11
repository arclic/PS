import sys

inputText, bombText = list(map(lambda x:x.strip(),sys.stdin.readlines()))

inputStack = [0]*1000010

cnt = 0
head = 0

lenBombText = len(bombText)
bombList = [x for x in bombText]

while cnt < len(inputText):
    inputStack[head] = inputText[cnt]
    head += 1
    cnt += 1
    
    # 끝에가 동일 할 경우
    if inputStack[head-1] == bombText[-1]:
        if head < lenBombText:
            continue
        else:
            if inputStack[head - lenBombText:head] == bombList:
                head -= lenBombText
                
if head:
    print("".join(inputStack[:head]))

else:
    print("FRULA")
