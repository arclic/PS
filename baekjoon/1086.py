import sys
import math

def main():
    N = int(input())
    numbers = []
    for _ in range(N):
        numbers.append(int(sys.stdin.readline().strip()))
    K = int(input())

    # dp[n][m]: n 순열으로 만들 수 있는 수들 중 K로 나누었을 때 나머지가 m인 수들
    dp = [[-1] * K for _ in range(1 << N)]
    length = [0] * (1 << N)
    MASK = (1 << N) - 1

    for i in range(1 << N):
        bin_i = bin(i).lstrip('0b').zfill(N)

        _len = 0
        for j in range(N):
            if bin_i[j] == "1":
                _len += len(str(numbers[j]))

        length[i] = _len

    mod_10_k = [1] * (max(length) + 1)

    for i in range(1, max(length) + 1):
        mod_10_k[i] = mod_10_k[i-1] * 10 % K

    for i in range(N):
        for j in range(K):
            dp[1 << (N-i-1)][j] = 0

        dp[1 << (N-i-1)][numbers[i]%K] = 1

    def calc(n, m):
        if dp[n][m] != -1:
            return dp[n][m]

        ans = 0 
        for i in range(N):
            if n & (1 << (N-i-1)):
                rest = n & (MASK ^ (1 << (N-i-1)))

                mod = mod_10_k[length[rest]] * numbers[i] % K

                ans += calc(rest, (m-mod)%K)
        
        dp[n][m] = ans
        return ans

    correct = calc((1 << N) - 1, 0)
    total = 1
    for i in range(1, N+1):
        total *= i

    gcd = math.gcd(correct, total)

    print("{0}/{1}".format(correct//gcd, total//gcd))

main()