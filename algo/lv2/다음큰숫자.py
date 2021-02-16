def solution(n):
    answer = 0
    #조건 1 n 보다 커야한다.
    #조건 2 n의 다음 숫자는 2진수 변환했는데 1의 갯수가 같다
    #조건 3 n의 다음 숫자는 조건 1,2를 만족하는수중 가장 작은 수여야한다.
    i = n
    while True :
        before = format(i,'b')
        after = format(n+1,'b')
        if(str(before).count('1') == str(after).count('1')) :
            answer = n+1
            break
        n +=1
    return answer