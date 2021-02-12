# import math
# def solution(n):
#     answer = [True] * (n+1)
    
#     for i in range(2,int(math.sqrt(n))+1) :
#         if answer[i] :
#             j = 2
#             while i * j <= n :
#                 answer[i * j] = False
#                 j+=1
            
#     result = 0
#     for i in range(2,n+1) :
#         if answer[i] :
#             result += 1
#     return result

from itertools import permutations
import math

def check(n) :
    if (n < 2) :
        return False
    for i in range(2,int(math.sqrt(n))+1):
        if(n%i == 0) :
            return False
    return True

def solution(numbers):
    answer = 0
    temp = list(numbers)
    for i in range(1,len(numbers)+1) :
        numL = list(map(''.join,permutations(temp,i))
        for j in list(set(numL)) :
            if check(int(j)) :
                answer += 1
                    
    return answer

print(solution('17'))