import sys

N = int(input())
M = int(input())

cost = [[0] * (N+1) for _ in range(N+1)]
con = []
minCost = 0

union = [i for i in range(N+1)]

for _ in range(M):
    con.append(list(map(int, sys.stdin.readline().strip().split())))

con = sorted(con, key=lambda x : x[2], reverse = True)

while con:
    a, b, c = con.pop()

    if union[a] != union[b]:
        cost[a][b] = cost[b][a] = c
        minCost += c

        mi = min(union[a], union[b])
        ma = max(union[a], union[b])

        for i in range(1, N+1):
            if union[i] == ma:
                union[i] = mi

    if union.count(1) == N:
        break


print(minCost)
