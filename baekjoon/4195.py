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
    
    if parentA != parentB:
        tree[parentB] = parentA
        network[parentA] += network[parentB]


numCase = int(input())
    
for _ in range(numCase):
    friends = {}
    count = 1
    tree = [0]
    network = [0]
    
    numFriends = int(sys.stdin.readline().strip())
    
    for __ in range(numFriends):
        A, B = sys.stdin.readline().strip().split()
        
        if A not in friends.keys():
            friends[A] = count
            tree.append(count)
            network.append(1)
            count += 1
        
        if B not in friends.keys():
            friends[B] = count
            tree.append(count)
            network.append(1)
            count += 1
        
        union(friends[A], friends[B])
        
        print(network[find(friends[A])])
        
