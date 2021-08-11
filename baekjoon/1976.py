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


n = int(input())
m = int(input())

tree = [0] * (n+1)

for i in range(1, n+1):
    tree[i] = i

count = 1
    
for _ in range(n):
    cities = list(map(int, sys.stdin.readline().strip().split()))
    
    for idx, city in enumerate(cities, 1):
        if city == 1:
            union(count, idx)
    
    count +=1
    
plans = list(map(int, sys.stdin.readline().strip().split()))

plans = list(map(find, plans))

if len(set(plans)) == 1:
    print("YES")

else:
    print("NO")
    
