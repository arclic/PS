import sys

def find(root):
    while root != tree[root]:
        root = tree[root]
        
    return root

G = int(sys.stdin.readline().strip())
P = int(sys.stdin.readline().strip())

tree = [0] * (G+1)

for i in range(1, G+1):
    tree[i] = i

count = 0
    
for _ in range(P):
    g_i = int(sys.stdin.readline().strip())
    
    root = find(tree[g_i])
    tree[g_i] = root
    
    if root < 1:
        break
        
    else:
        tree[root] = tree[root - 1]
        count += 1
    
        
print(count)
