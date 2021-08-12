import collections

def main():
    n = int(input())

    queue = collections.deque()
    queue.appendleft((n, [n]))
    visited = [False] * (n+1)

    while queue:
        num, array = queue.pop()

        if num < 1:
            return

        if num == 1:
            print(len(array) - 1)
            print(*array)
            return

        if num%3 == 0 and not visited[num//3]:
            queue.appendleft((num//3, array + [num//3]))
            visited[num//3] = True

        if num%2 == 0 and not visited[num//2]:
            queue.appendleft((num//2, array + [num//2]))
            visited[num//2] = True
        
        if not visited[num - 1]:
            queue.appendleft((num - 1, array + [num - 1]))
            visited[num - 1] = True

main()