n = 5
lost = [2,4]
reserve = [1,3,5]

def solution(n, lost, reserve):
    set_reserve = set(reserve)-set(lost)
    set_lost = set(lost)-set(reserve)
    reserve = sorted(list(set_reserve))
    print(reserve)
    lost = sorted(list(set_lost))
    answer = 0
    answer = n-len(lost)
    print(answer)
    reserve.sort()
    for i in range (len(reserve)) :
        if(reserve[i]) in lost:
            del lost[lost.index(reserve[i])]
            answer += 1
        elif((reserve[i] -1) in lost):
            del lost[lost.index(reserve[i]-1)]
            answer += 1

        elif((reserve[i] + 1) in lost):
            del lost[lost.index(reserve[i]+1)]
            answer += 1


    return answer

print(solution(n,lost,reserve))
