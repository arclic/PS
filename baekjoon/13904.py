import sys

N = int(sys.stdin.readline().strip())

scores = []

for _ in range(N):
    scores.append(list(map(int, sys.stdin.readline().strip().split())))
    
scores.sort(key=lambda x : x[1], reverse = True)
scores.sort(key=lambda x : x[0], reverse = True)

days = scores[0][0]

maxScore = 0

for d in range(days, 0, -1):
    
    curScore = -1
    curDay = -1
    
    for day, score in scores:
        if day >= d and score >= curScore:
            curScore = score
            curDay = day
    
    if curScore != -1:
        maxScore += curScore
        scores.remove([curDay, curScore])
    
print(maxScore)
