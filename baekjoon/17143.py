import sys
import copy

def main():
    move_dir = [(0,0), (-1, 0), (1, 0), (0, 1), (0, -1)]
    R, C, M = list(map(int, sys.stdin.readline().strip().split()))
    MAP = [[-1] * (C+1) for _ in range(R+1)]
    shark_info = []
    index = 0
    for _ in range(M):
        r, c, s, d, z = list(map(int, sys.stdin.readline().strip().split()))
        shark_info.append((r, c, s, d, z))
        MAP[r][c] = index
        index += 1
    
    current_king_pos = 1
    ans = 0

    while current_king_pos <= C:
        new_MAP = [[-1] * (C+1) for _ in range(R+1)]
        for i in range(1, R+1):
            if MAP[i][current_king_pos] != -1:
                ans += shark_info[MAP[i][current_king_pos]][-1]
                shark_info[MAP[i][current_king_pos]] = (-1, -1, 0, 0, 0)
                MAP[i][current_king_pos] = -1
                break


        # Move All
        for idx, (r, c, s, d, z) in enumerate(shark_info):
            if r == -1 and c == -1:
                continue

            new_r, new_c = r, c

            for _ in range(s):
                new_r, new_c = new_r + move_dir[d][0], new_c + move_dir[d][1]

                if new_r <= 0:
                    new_r = 2
                    d = 2

                if new_r > R:
                    new_r = R-1
                    d = 1

                if new_c <= 0:
                    new_c = 2
                    d = 3

                if new_c > C:
                    new_c = C-1
                    d = 4

            if 0 <= new_MAP[new_r][new_c] < idx:
                if shark_info[new_MAP[new_r][new_c]][-1] < z:
                    shark_info[new_MAP[new_r][new_c]] = (-1, -1, 0, 0, 0)
                    new_MAP[new_r][new_c] = idx
                    shark_info[idx] = (new_r, new_c, s, d, z)

                else:
                    shark_info[idx] = (-1, -1, 0, 0, 0)

            else:
                new_MAP[new_r][new_c] = idx
                shark_info[idx] = (new_r, new_c, s, d, z)
                
        current_king_pos += 1

        MAP = copy.deepcopy(new_MAP)

    print(ans)

main()