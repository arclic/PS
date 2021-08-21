import sys

sys.setrecursionlimit(6 * 10 ** 6)

def main():
    n, m = list(map(int, sys.stdin.readline().strip().split()))
    points = [x for x in range(n)]
    lines = []
    ans = 0

    def find_root(root):
        if points[root] == root:
            return root

        points[root] = find_root(points[root])
        return points[root]

    for i in range(1, m+1):
        x, y = list(map(int, sys.stdin.readline().strip().split()))

        if ans == 0:
            root_x = find_root(x)
            root_y = find_root(y)
            if root_x == root_y:
                ans = i

            else:
                points[root_y] = root_x

    print(ans)




main()