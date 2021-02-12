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
        numL = list(map(''.join,permutations(temp,i)))
        for j in list(set(numL)):
            if check(int(j)) :
                if(j[0][0]=='0'):
                    continue
                answer += 1
                    
    return answer