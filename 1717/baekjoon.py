import sys

def find(a):
    if a == tree[a]:
        return a
    
    else:
        b = find(tree[a])
        tree[a] = b
        return b

def union(a, b):
    parentA = find(a)
    parentB = find(b)
    
    tree[parentB] = parentA


n, m = list(map(int, input().split()))

tree = [0] * (n+1)

for i in range(1, n+1):
    tree[i] = i

for _ in range(m):
    t, a, b = list(map(int, sys.stdin.readline().strip().split()))
    
    if t == 0:
        union(a, b)
        
    else:
        if find(a) == find(b):
            print("YES")
        else:
            print("NO")
