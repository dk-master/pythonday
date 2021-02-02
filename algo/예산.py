def solution(d, budget):
    answer = 0
    d.sort()
    hab = 0
    for i in d :
        hab += i
        if(hab > budget) :
            break
        answer += 1
    return answer