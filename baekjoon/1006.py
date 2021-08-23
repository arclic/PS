import sys



def main():
    T = int(input())
    for _ in range(T):
        N, W = list(map(int, sys.stdin.readline().strip().split()))
        zone1 = [0] + list(map(int, sys.stdin.readline().strip().split())) # 아래
        zone2 = [0] + list(map(int, sys.stdin.readline().strip().split())) # 위
        ans = 1000000

        # bottom[i]: i번 째에 아래만 점령된 경우
        # top[i]: i번 째에 위에만 점령된 경우
        # both[i]: i 번 째에 위와 아래 모두 점령 된 경우
        bottom = [0 for _ in range(N+1)]
        top = [0 for _ in range(N+1)]
        both = [0 for _ in range(N+1)]

        def clear():
            for i in range(N+1):
                bottom[i] = top[i] = both[i] = 0

        def dp():
            for i in range(2, N+1):
                # 위에서 2개 점유 가능한 경우
                _top = 1 if zone2[i-1] + zone2[i] <= W else 2
                # 밑에서 2개 점유 가능한 경우
                _bottom = 1 if zone1[i-1] + zone1[i] <= W else 2
                # i 번째에서 위 아래로 점유 가능한 경우
                _both = 1 if zone1[i] + zone2[i] <= W else 2

                bottom[i] = min(both[i-1] + 1, top[i-1] + _bottom)
                top[i] = min(both[i-1] + 1, bottom[i-1] + _top)
                both[i] = min(both[i-1] + _both, bottom[i] + 1, top[i] + 1, both[i-2] + _top + _bottom)

        # 위 아래 모두 연락이 되지 않았을 때
        bottom[1] = top[1] = 1
        both[1] = 1 if zone1[1] + zone2[1] <= W else 2

        dp()

        ans = min(ans, both[N])

        # 위에만 끝에와 연결이 되어 있는 경우
        if N > 1 and zone2[N] + zone2[1] <= W:
            clear()

            top[1] = 1
            bottom[1] = 99999 # 불가능
            both[1] = 2

            # 1과 2는 연결될 수 없음
            temp = zone2[1]
            zone2[1] = 99999

            dp()

            zone2[1] = temp

            ans = min(ans, bottom[N])

            pass

        # 아래에만 끝과 연결이 되어 있는 경우
        if N > 1 and zone1[N] + zone1[1] <= W:
            clear()

            bottom[1] = 1
            top[1] = 99999 # 불가능
            both[1] = 2

            # 1과 2는 연결될 수 없음
            temp = zone1[1]
            zone1[1] = 99999

            dp()

            zone1[1] = temp

            ans = min(ans, top[N])

        # 위 아래 모두 끝과 연결이 되어 있는 경우
        if N > 1 and zone2[N] + zone2[1] <= W and zone1[N] + zone1[1] <= W:
            clear()

            bottom[1] = 99999 # 불가능
            top[1] = 99999 # 불가능
            both[1] = 2

            # 1과 2는 연결될 수 없음
            zone1[1] = 99999
            zone2[1] = 99999

            dp()

            ans = min(ans, both[N-1])

        
        print(ans)

        



main()