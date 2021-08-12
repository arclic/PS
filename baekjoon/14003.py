import sys
import bisect

BIG_INT = 9000000000
SMALL_INT = -BIG_INT

def main():
    n = int(input())
    nums = list(map(int, sys.stdin.readline().strip().split()))
    dp = [SMALL_INT] + [BIG_INT] * n
    dp_index = [-1] * n
    ans = 0
    
    for index, num in enumerate(nums):
        i = bisect.bisect_left(dp, num)
        dp[i] = num
        dp_index[index] = i
        if i > ans:
            ans = i
        
    ans_array = []

    for index in range(n-1, -1, -1):
        if dp_index[index] == ans - len(ans_array):
            ans_array.append(nums[index])

    print(ans)
    print(*ans_array[::-1])

main()