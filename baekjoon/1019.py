def main():
    N = int(input())

    numbers = [0] * 10

    def calc_numbers(num, steps):
        nonlocal numbers
        while num:
            numbers[num%10] += steps
            num //= 10

    def solve(A, B, steps):
        while A%10 != 0 and A <= B:
            calc_numbers(A, steps)
            A += 1

        if A > B:
            return

        while B%10 != 9 and A <= B:
            calc_numbers(B, steps)
            B -= 1

        for i in range(10):
            numbers[i] += (B//10 - A//10 + 1) * steps

        solve(A//10, B//10, steps * 10)

    solve(1, N, 1)

    print(*numbers)


main()