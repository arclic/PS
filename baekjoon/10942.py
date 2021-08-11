import sys

def main():
    N = int(input())
    numbers = [0] + list(map(int, sys.stdin.readline().strip().split()))
    M = int(input())

    # is_palindrome[S][E] : S부터 시작해서 E까지가 palindrome인가?
    is_palindrome = [ [False] * (N+1) for _ in range(N+1)]

    for jump in range(N+1):
        for start in range(1, N+1 - jump):
            if jump == 0:
                is_palindrome[start][start] = True
            
            elif jump == 1 and numbers[start] == numbers[start+jump]:
                is_palindrome[start][start+jump] = True

            elif is_palindrome[start+1][start+jump-1] and numbers[start] == numbers[start+jump]:
                is_palindrome[start][start+jump] = True

    for _ in range(M):
        S, E = list(map(int, sys.stdin.readline().strip().split()))
        ans = 1 if is_palindrome[S][E] else 0

        print(ans)

main()