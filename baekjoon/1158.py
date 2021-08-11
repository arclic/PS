import sys

n, m = map(int, sys.stdin.readline().split())

dataQueue = [ (x + 1) for x in range(n)]

cnt = 0
currentIndex = 0
deadMan = []

while cnt < n:
    nextIndex = (currentIndex + m - 1) % len(dataQueue)
    
    deadMan.append(str(dataQueue.pop(nextIndex)))
        
    cnt += 1
    currentIndex = nextIndex

print("<{0}>".format(", ".join(deadMan)))
