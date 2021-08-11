import sys

def calcScore(scoreStack, score):
    if scoreStack[-1] == 0:
        scoreStack[-1] = score
    
    else:
        temp = 0
        while True:
            if scoreStack[-1] == 0:
                scoreStack[-1] = temp * score
                break
                
            else:
                temp += scoreStack.pop()

inputStr = sys.stdin.readline().strip()

totalScore = 0
scoreStack = []
charStack = []

for char in inputStr:
    charStack.append(char)

    if char == ")":
        charStack.pop()
        if len(charStack) == 0 or charStack.pop() != "(":
            totalScore = -1
            break

        else:
            calcScore(scoreStack, 2)

    elif char == "]":
        charStack.pop()
        if len(charStack) == 0 or charStack.pop() != "[":
            totalScore = -1
            break

        else:
            calcScore(scoreStack, 3)

    else:
        scoreStack.append(0)

if totalScore == -1 or len(charStack) != 0:
    print("0")

else:
    for _v in scoreStack:
        totalScore += _v

    print(totalScore)
