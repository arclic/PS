import sys

def minHeapify(heap):
    index = len(heap) - 1
    
    while index > 1:
        if heap[index] < heap[index//2]:
            heap[index//2], heap[index] = heap[index], heap[index//2]
        
        else:
            break
        
        index = index // 2
        
def findMedian(heap):
    newHeap = []
    for _ in heap:
        newHeap.append(_)
    
    length = len(heap) - 1
    
    cnt = 1
    
    while cnt <= (len(heap)-1)//2:
        newHeap[1], newHeap[-1] = newHeap[-1], newHeap[1]
        
        newHeap.pop()
        length -= 1
        
        index = 1
        
        while index <= length//2:
            minValue = 0
            minIndex = 0
            
            if index*2 <= length and index*2 + 1 <= length and newHeap[index*2 + 1] < newHeap[index*2]:
                minValue = newHeap[index*2 + 1]
                minIndex = index*2 + 1
            
            else:
                minValue = newHeap[index*2]
                minIndex = index*2
                
            if minValue < newHeap[index]:
                newHeap[index], newHeap[minIndex] = newHeap[minIndex], newHeap[index]
                index = minIndex
            
            else:
                break
        
        cnt += 1
                
    return newHeap[1]
                

T = int(input().strip())

for _ in range(T):
    M = int(input().strip())
    
    numbers = []
    
    for __ in range(M//10 + 1):
        numbers += (sys.stdin.readline().strip().split())
    
    heap = [0]
    result = []
    
    for idx, num in enumerate(numbers, 1):
        heap.append(int(num))
        minHeapify(heap)
        if idx%2 == 1:
            result.append(str(findMedian(heap)))
    
    print(len(result))
    print(" ".join(result))
