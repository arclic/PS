import sys

CONSTANT = 1000000007

def calc(base, index):

    if index <= 2:
        return base ** index

    value = calc(base, index//2)
    if index % 2 == 0:
        return value * value % CONSTANT

    else:
        return value * value * base % CONSTANT


def main():
    M = int(input())
    ans = 0
    
    for _ in range(M):
        b, a = list(map(int, sys.stdin.readline().strip().split()))
        ans += (a * calc(b, CONSTANT-2)) % CONSTANT

    print(ans% CONSTANT)

main()