import sys
from collections import deque

F, S, G, U, D = list(map(int, sys.stdin.readline().strip().split()))

queue = deque()
visited = [0] * (F + 1)
visited[S] = 1
queue.appendleft((S, 0))

while queue:
    now, numButton = queue.pop()
    
    if now == G:
        print(numButton)
        break
    
    if now + U <= F and visited[now + U] == 0:
        visited[now + U] = 1
        queue.appendleft((now + U, numButton + 1))
        
    if now - D >= 1 and visited[now - D] == 0:
        visited[now - D] = 1
        queue.appendleft((now - D, numButton + 1))
        
if now != G:
    print("use the stairs")
