from itertools import combinations

def solution(numbers):
    answer = []
    for a,b in combinations(numbers,2) :
        temp = a + b
        if temp not in answer:
            print(temp)
            answer.append(temp)

    return answer
        
    

print(sorted(solution([2,1,3,4,1])))