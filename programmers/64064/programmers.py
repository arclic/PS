def addPermutation(baseList, targetList):
    permutationList = []
    
    for t in targetList:
        for b in baseList:
            if t not in b:
                permutationList.append((b + [t]))
                
    return permutationList 

def solution(user_id, banned_id):
    answer = 0
    answerDict = {}
        
    for i, banData in enumerate(banned_id):
        answerDict[i] = []
        for userData in user_id:
            if len(banData) == len(userData):
                check = True
                for idx, char in enumerate(banData):
                    if char != "*" and userData[idx] != char:
                        check = False
                
                if check:
                    answerDict[i].append(userData)
    
    permutationList = []
        
    for idx, value in enumerate(answerDict.values()):
        if idx == 0:
            for _v in value:
                permutationList.append([_v])
            continue
        permutationList = addPermutation(permutationList, value)
    
    answerList = []
    
    for value in permutationList:
        if len(value) == len(banned_id) and sorted(value) not in answerList:
            answerList.append(sorted(value))
        
    return len(answerList)
