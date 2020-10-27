n = 5
lost = [2,4]
reserve = [1,3,5]

def solution(n, lost, reserve):
    answer = 0
    answer = n-len(lost)
    reserve.sort()
    
    con = len(reserve)
    for k in range (con) :
        if(reserve[k]) in lost:
            del lost[lost.index(reserve[k])]
            del reserve[k]
            answer += 1
    print(reserve)
    for i in range (len(reserve)) :
        if((reserve[i] -1) in lost):
            del lost[lost.index(reserve[i]-1)]
            answer += 1

        elif((reserve[i] + 1) in lost):
            del lost[lost.index(reserve[i]+1)]
            answer += 1

    return answer

print(solution(n,lost,reserve))