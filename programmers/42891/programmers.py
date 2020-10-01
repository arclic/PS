def solution(food_times, k):
    answer = 0
    
    heap = []
    length = len(food_times)
    totalCount = 0
    outCount = 0
    
    import heapq
    
    for idx, times in enumerate(food_times):
        heapq.heappush(heap, (times, idx))
        
    while True:
        minValue = heap[0][0]
        minIndex = heap[0][1]
        
        if k - (minValue - totalCount) * (length - outCount) >= 0:
            if minValue > totalCount:
                k -= (minValue - totalCount) * (length - outCount)
                totalCount += (minValue - totalCount)
                
            outCount += 1
            food_times[minIndex] = 0
            heapq.heappop(heap)
        
        else:
            break
            
        if len(heap) == 0:
            return -1
    
    possible = (k // (length - outCount))
    k %= (length - outCount)
    
    for idx, value in enumerate(food_times):
        if k == 0 and (value - possible) > 0:
            answer = idx + 1
            break
        
        if value == 0:
            continue
        else:
            k -= 1
    
    return answer
