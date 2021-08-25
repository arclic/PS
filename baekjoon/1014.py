import sys

def main():
    C = int(input())
    for _ in range(C):
        N, M = list(map(int, sys.stdin.readline().strip().split()))
        room = []
        dp = [[-1] * (2 ** M) for _ in range(N+1)]
        ans = 0
        for __ in range(N):
            room.append([x for x in sys.stdin.readline().strip()])

        for i in range(2 ** M):
            bin_i = bin(i).lstrip("0b").zfill(M)
            possible = True
            for j in range(M):
                if bin_i[j] == "1":
                    if room[0][j] == "x" or (j-1 >= 0 and bin_i[j-1] == "1") or (j+1 < M and bin_i[j+1] == "1"):
                        possible = False
                        break

            if possible:
                dp[0][i] = bin_i.count('1')

        for i in range(1, N):
            for top in range(2 ** M):
                if dp[i-1][top] == -1:
                    continue
                bin_top = bin(top).lstrip("0b").zfill(M)
                for cur in range(2 ** M):
                    bin_cur = bin(cur).lstrip("0b").zfill(M)
                    possible = True
                    for cur_index in range(M):
                        if bin_cur[cur_index] == "1":
                            if room[i][cur_index] == "x" or (cur_index-1 >= 0 and bin_cur[cur_index-1] == "1") or (cur_index-1 >= 0 and bin_top[cur_index-1] == "1") or (cur_index+1 < M and bin_top[cur_index+1] == "1") or (cur_index+1 < M and bin_cur[cur_index+1] == "1"):
                                possible = False
                                break

                    if possible:
                        dp[i][cur] = max(dp[i][cur], dp[i-1][top] + bin_cur.count('1'))

        print(max(dp[N-1]))



main()