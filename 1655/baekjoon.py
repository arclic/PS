import sys
import heapq

N = int(sys.stdin.readline().strip())

# Heap을 median 기준으로 2개로 분할
upperHeap = []
lowerHeap = [] #maxHeap
median = -11111

for idx in range(N):
    value = int(sys.stdin.readline().strip())
    
    if median == -11111:
        median = value
        print(median)
        
    else:
        if value > median:
            heapq.heappush(upperHeap, value)
        else:
            heapq.heappush(lowerHeap, (value * (-1), value))
            
        if len(lowerHeap) - len(upperHeap) == 2:
            heapq.heappush(upperHeap, median)
            median = heapq.heappop(lowerHeap)[1]
        
        elif len(upperHeap) - len(lowerHeap) == 2:
            heapq.heappush(lowerHeap, (median * (-1), median))
            median = heapq.heappop(upperHeap)
            
        if (idx + 1) % 2 == 0:
            if len(lowerHeap) > len(upperHeap):
                print(lowerHeap[0][1])
            
            else:
                print(median)
        
        else:
            print(median)
        

