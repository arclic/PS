import sys
import collections

def ccw(x1, y1, x2, y2, x3, y3):
    return x1*y2 + x2*y3 + x3*y1 - x2*y1 - x3*y2 - x1*y3

def is_connect(line1, line2):
    x1, y1, x2, y2 = line1
    x3, y3, x4, y4 = line2

    ab = ccw(x1, y1, x2, y2, x3, y3) * ccw(x1, y1, x2, y2, x4, y4)
    cd = ccw(x3, y3, x4, y4, x1, y1) * ccw(x3, y3, x4, y4, x2, y2)

    if ab == 0 and cd == 0:
        if min(x1, x2) <= max(x3, x4) and min(x3, x4) <= max(x1, x2) and min(y1, y2) <= max(y3, y4) and min(y3, y4) <= max(y1, y2):
            return True

        else:
            return False

    elif ab <= 0 and cd <= 0:
        return True

    else:
        return False


def find_root(groups, root):
    while root != groups[root]:
        root = groups[root]

    return root

def main():
    n = int(input())
    lines = [0]
    groups = [x for x in range(n+1)]
    for _ in range(n):
        x1, y1, x2, y2 = list(map(int, sys.stdin.readline().strip().split()))
        lines.append((x1, y1, x2, y2))

    for i in range(1, n+1):
        for j in range(i+1, n+1):
            if is_connect(lines[i], lines[j]):
                i_root = find_root(groups, i)
                j_root = find_root(groups, j)
                groups[i] = groups[j] = groups[i_root] = groups[j_root] = min(i_root, j_root)

    group_dict = collections.defaultdict(int)

    for i in range(1, n+1):
        group_dict[find_root(groups, i)] += 1

    print(len(group_dict))
    print(max(group_dict.values()))

main()