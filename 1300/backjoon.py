import sys

N = int(input())
K = int(input())

nleft = 1
nright = N*N

while nleft <= nright:
    number = (nleft + nright) // 2
    
    nsame = 0
    nless = 0
    
    for i in range(1, N+1):
        if number % i == 0:
            if number / i <= N:
                nsame += 1
                nless += min((number / i) - 1, N)
            
            else:
                nless += N
        
        else:
            nless += min((number // i), N)
            
    if nsame and nless + 1 <= K <= nless + nsame:
        print(number)
        break
    
    if K > nsame + nless:
        nleft = number + 1
        
    else:
        nright = number - 1
    
