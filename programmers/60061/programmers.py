frames = {}

def checkFrame(x, y, a):
    # 기둥인경우
    if a == 0:
        # 바닥인경우
        if y == 0:
            return True
        
        # 보의 한 쪽 끝 위에 있는 경우
        if (x-1, y, 1-a) in frames.keys() or (x,y, 1-a) in frames.keys():
            return True
        
        # 다른 기둥 위에 있는 경우
        if (x, y-1, a) in frames.keys():
            return True
        
    # 보인경우
    else:
        # 한 쪽 끝 부분이 기둥 위에 있는경우
        if (x, y-1, 1-a) in frames.keys() or (x+1, y-1, 1-a) in frames.keys():
            return True
        
        # 양쪽 끝 부분이 다른 보와 동시에 연결되어 있는경우
        if (x-1, y, a) in frames.keys() and (x+1, y, a) in frames.keys():
            return True
        
    return False

def solution(n, build_frame):
    answer = []
    
    for x, y, a, b in build_frame:
        # 삭제
        if b == 0:
            del frames[(x, y, a)]
            for tx, ty, ta in frames.keys():
                if not checkFrame(tx, ty, ta):
                    frames[(x, y, a)] = 1
                    break
                    
        # 설치
        if b == 1:
            if checkFrame(x, y, a):
                frames[(x, y, a)] = 1
    
    for x, y, a in frames.keys():
        answer.append([x, y, a])
    
    answer.sort(key = lambda x : x[2])
    answer.sort(key = lambda x : x[1])
    answer.sort(key = lambda x : x[0])
    
    return answer
