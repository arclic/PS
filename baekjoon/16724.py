import sys

def main():
    N, M = list(map(int, sys.stdin.readline().strip().split()))
    
    MAP = []
    visited = [[False] * M for _ in range(N)]
    MOVE = {
        'D': (1, 0),
        'L': (0, -1),
        'U': (-1, 0),
        'R': (0, 1)
    }

    for _ in range(N):
        line = [x for x in sys.stdin.readline().strip()]
        MAP.append(line)

    ans = 1

    for i in range(N):
        for j in range(M):
            if not visited[i][j]:
                stack = []
                stack.append((i, j))
                visited[i][j] = True
                next_i, next_j = i + MOVE[MAP[i][j]][0], j + MOVE[MAP[i][j]][1]

                while not visited[next_i][next_j]:
                    stack.append((next_i, next_j))
                    visited[next_i][next_j] = True
                    next_i, next_j = next_i + MOVE[MAP[next_i][next_j]][0], next_j + MOVE[MAP[next_i][next_j]][1]

                if MAP[next_i][next_j] not in MOVE.keys():
                    while stack:
                        _i, _j = stack.pop()

                        MAP[_i][_j] = MAP[next_i][next_j]


                else:
                    while stack:
                        _i, _j = stack.pop()

                        MAP[_i][_j] = ans

                    ans += 1

    print(ans - 1)
    


main()