# 완전탐색  딱히 별다른 방법이 없다
def solution(n):
    answer = 1
    for i in range(1,n//2 + 1) :
        cnt = 0 
        for j in range(i,n+1) :
            cnt += j
            if cnt == n :
                answer += 1
                break
            elif cnt > n : break
    return answer