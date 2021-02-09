import math
def solution(n):
    answer = [True] * (n+1)
    
    for i in range(2,int(math.sqrt(n))+1) :
        if answer[i] :
            j = 2
            while i * j <= n :
                answer[i * j] = False
                j+=1
            
    result = 0
    for i in range(2,n+1) :
        if answer[i] :
            result += 1
    return result