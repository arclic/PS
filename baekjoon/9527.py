
# dp[n] : 2^n - 1 까지의 1의 개수의 합
dp = [0 for x in range(100)]

def f(x):
    if x == 0:
        return 0

    binary = bin(x).lstrip('0b')
    next_binary = binary[1:].lstrip('0')
    if not next_binary:
        next_binary = '0'

    return dp[len(binary) - 1] + f(int(next_binary, 2)) + int(next_binary, 2) + 1

def main():
    a, b = list(map(int, input().split()))
    
    for i in range(1, 60):
        dp[i] = dp[i-1] * 2 + 2 ** (i-1)

    print(f(b) - f(a-1))

main()