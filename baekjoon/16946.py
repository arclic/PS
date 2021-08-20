import sys
import collections

dxdy = [(-1, 0), (1, 0), (0, 1), (0, -1)]

def main():
    N, M = list(map(int, sys.stdin.readline().strip().split()))
    MAP = []
    dp = [[(0, 0)] * M for _ in range(N)]
    visited = [[False] * M for _ in range(N)]
    for _ in range(N):
        line = [int(x) for x in sys.stdin.readline().strip()]
        MAP.append(line)

    division = 1
    for i in range(N):
        for j in range(M):
            if not visited[i][j] and MAP[i][j] == 0:
                bfs = collections.deque()
                visit_stack = []
                count = 1
                
                bfs.appendleft((i, j))
                visit_stack.append((i, j))
                visited[i][j] = True

                while bfs:
                    _i, _j = bfs.pop()

                    for dx, dy in dxdy:
                        if 0 <= _i + dx < N and 0 <= _j + dy < M and not visited[_i + dx][_j + dy] and MAP[_i + dx][_j + dy] == 0:
                            bfs.appendleft((_i + dx, _j + dy))
                            visit_stack.append((_i + dx, _j + dy))
                            visited[_i + dx][_j + dy] = True
                            count += 1

                while visit_stack:
                    _i, _j = visit_stack.pop()

                    dp[_i][_j] = (division, count)

                division += 1

    
    for i in range(N):
        for j in range(M):
            if MAP[i][j] == 0:
                print(0, end="")
            
            else:
                ans = 1
                visit_division = []

                for dx, dy in dxdy:
                    if 0 <= i + dx < N and 0 <= j + dy < M:
                        div, value = dp[i+dx][j+dy]
                        if div not in visit_division:
                            ans += value
                            visit_division.append(div)

                print(ans%10, end="")

        print()

                

main()