def solution(A,B):
    answer = 0
    result = []
    A.sort()
    B.sort(reverse = True)
    for a,b in zip(A,B) :
        answer += (a*b)
    result.append(answer)
    A.sort(reverse = True)
    B.sort()
    answer = 0
    for c,d in zip(A,B) :
        answer += (c*d)
    result.append(answer)
    return min(result)