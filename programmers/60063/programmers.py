from collections import deque

def checkNewPosition(board, checked, n, newPos1, newPos2):
    if 0 <= newPos1[0] < n and 0 <= newPos1[1] < n and 0 <= newPos2[0] < n and 0 <= newPos2[1] < n and (newPos1, newPos2) not in checked.keys() and board[newPos1[0]][newPos1[1]] == 0 and board[newPos2[0]][newPos2[1]] == 0:
        return True
    
    else:
        return False

def solution(board):
    answer = 0
    
    n = len(board)
    
    pos1 = (0, 0)
    pos2 = (0, 1)
    
    checked = {}
    
    queue = deque()
    queue.appendleft((pos1, pos2, 0))
    checked[pos1, pos2] = checked[pos2, pos1] = 1
    
    while queue:
        pos1, pos2, numMove = queue.pop()
        
        if pos1 == (n-1, n-1) or pos2 == (n-1, n-1):
            return numMove
        
        # 순서대로 상, 하, 좌, 우 이동
        for x, y in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            newPos1 = (pos1[0] + x, pos1[1] + y)
            newPos2 = (pos2[0] + x, pos2[1] + y)
            
            if checkNewPosition(board, checked, n, newPos1, newPos2):
                queue.appendleft((newPos1, newPos2, numMove + 1))
                checked[newPos1, newPos2] = checked[newPos2, newPos1] = 1
        
        
        # 반시계 회전, 시계회전
        # [0 -1], [0  1]
        # [1  0], [-1 0]
        # pos1을 축으로 pos2를 회전
        newPos1 = pos1
        offset = (pos2[0] - pos1[0], pos2[1] - pos1[1])
        counterClockNewPos2 = (-1 * offset[1] + pos1[0], offset[0] + pos1[1])
        clockNewPos2 = (offset[1] + pos1[0], -1 * offset[0] + pos1[1])
        if checkNewPosition(board, checked, n, newPos1, counterClockNewPos2):
            spin = (counterClockNewPos2[0] - pos2[0]) * (counterClockNewPos2[1] - pos2[1])
            # 회전하면서 아무것도 안 겹치는 경우
            if (spin == 1 and board[counterClockNewPos2[0]][pos2[1]] == 0) or (spin == -1 and board[pos2[0]][counterClockNewPos2[1]] == 0):
                queue.appendleft((newPos1, counterClockNewPos2, numMove + 1))
                checked[newPos1, counterClockNewPos2] = checked[counterClockNewPos2, newPos1] = 1
                
        if checkNewPosition(board, checked, n, newPos1, clockNewPos2):
            spin = (clockNewPos2[0] - pos2[0]) * (clockNewPos2[1] - pos2[1])
            # 회전하면서 아무것도 안 겹치는 경우
            if (spin == 1 and board[pos2[0]][clockNewPos2[1]] == 0) or (spin == -1 and board[clockNewPos2[0]][pos2[1]] == 0):
                queue.appendleft((newPos1, clockNewPos2, numMove + 1))
                checked[newPos1, clockNewPos2] = checked[clockNewPos2, newPos1] = 1
                
        # pos2을 축으로 pos1를 회전
        newPos2 = pos2
        offset = (pos1[0] - pos2[0], pos1[1] - pos2[1])
        counterClockNewPos1 = (-1 * offset[1] + pos2[0], offset[0] + pos2[1])
        clockNewPos1 = (offset[1] + pos2[0], -1 * offset[0] + pos2[1])
        if checkNewPosition(board, checked, n, counterClockNewPos1, newPos2):
            spin = (counterClockNewPos1[0] - pos1[0]) * (counterClockNewPos1[1] - pos1[1])
            # 회전하면서 아무것도 안 겹치는 경우
            if (spin == 1 and board[counterClockNewPos1[0]][pos1[1]] == 0) or (spin == -1 and board[pos1[0]][counterClockNewPos1[1]] == 0):
                queue.appendleft((counterClockNewPos1, newPos2, numMove + 1))
                checked[counterClockNewPos1, newPos2] = checked[newPos2, counterClockNewPos1] = 1
        
        if checkNewPosition(board, checked, n, clockNewPos1, newPos2):
            spin = (clockNewPos1[0] - pos1[0]) * (clockNewPos1[1] - pos1[1])
            # 회전하면서 아무것도 안 겹치는 경우
            if (spin == 1 and board[pos1[0]][clockNewPos1[1]] == 0) or (spin == -1 and board[clockNewPos1[0]][pos1[1]] == 0):
                queue.appendleft((clockNewPos1, newPos2, numMove + 1))
                checked[clockNewPos1, newPos2] = checked[newPos2, clockNewPos1] = 1
                
    
    return answer
