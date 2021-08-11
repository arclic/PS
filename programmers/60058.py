def partitionString(string):
    u = ""
    v = ""
    
    openBracket = 0
    closeBracket = 0
    
    for char in string:
        if openBracket != 0 and openBracket == closeBracket:
            v += char
        else:
            u += char
            if char == "(":
                openBracket += 1
            
            else:
                closeBracket += 1
                
    return u, v

def checkCorrect(string):
    stack = []
    
    for char in string:
        if char == ")":
            if len(stack) == 0 or stack[-1] != "(":
                return False
            else:
                stack.pop()
        
        else:
            stack.append(char)
            
    if len(stack) != 0:
        return False
    
    return True

def reverseString(string):
    newString = ""
    
    for idx, char in enumerate(string):
        if idx == 0 or idx == len(string) - 1:
            continue
        
        if char == "(":
            newString += ")"
        
        else:
            newString += "("
            
    return newString

def balanceString(u, v):
    if not u and not v:
        return ""
    
    _u, _v = partitionString(v)
    
    if checkCorrect(u):    
        return u + balanceString(_u, _v)
    
    else:
        return '(' + balanceString(_u, _v) + ')' + reverseString(u)

def solution(p):
    answer = ''
    
    u, v = partitionString(p)
    
    answer = balanceString(u, v)
    
    return answer
