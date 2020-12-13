def solution(stones, k):
    answer = 0
    
    minStone = 1
    maxStone = max(stones)
    
    while minStone <= maxStone:
        mid = (minStone + maxStone) // 2
        
        possible = False
        
        position = 0
        
        for idx, data in enumerate(stones, 1):
            if data - mid > 0 and idx - position <= k:
                position = idx
                
        if position > len(stones) - k:
            possible = True
            
        if possible:
            answer = (mid + 1)
            minStone = mid + 1
            
        else:
            maxStone = mid - 1
        
    return answer
