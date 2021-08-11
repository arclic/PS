import sys

BIG_NUM = 9999999999

def main():
    N = int(input())
    matrix = []

    for _ in range(N):
        a, b = list(map(int, sys.stdin.readline().strip().split()))
        matrix.append((a, b))

    min_memo = [[BIG_NUM] * N for _ in range(N)]

    def find_min(left, right):
        if min_memo[left][right] != BIG_NUM:
            return min_memo[left][right] 

        if left == right:
            return 0

        ans = BIG_NUM
        for start in range(left, right):
            ans = min(ans, find_min(left, start) + find_min(start + 1, right) + matrix[left][0] * matrix[start][1] * matrix[right][1])

        min_memo[left][right] = ans
        return ans

    print(find_min(0, N-1))

main()