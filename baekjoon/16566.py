import sys
import bisect

def main():
    N, M, K = list(map(int, sys.stdin.readline().strip().split()))
    cards = list(map(int, sys.stdin.readline().strip().split()))
    given_cards = list(map(int, sys.stdin.readline().strip().split()))

    root_cards = [x for x in range(M)]
    cards.sort()

    def find_root(index):
        update_roots = []
        while root_cards[index] != index:
            update_roots.append(index)
            index = root_cards[index]

        for root in update_roots:
            root_cards[root] = index
        
        return index

    for _card in given_cards:
        i = bisect.bisect_right(cards, _card)
        root = find_root(i)

        print(cards[root])

        root_cards[root] += 1

main()