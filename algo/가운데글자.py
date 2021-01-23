def solution(s):
    temp = len(s)
    answer = ''
    if(temp%2 == 0) :
        answer = s[(temp//2)-1 : (temp//2) + 1]
    else :
        answer = s[temp//2]
    
    return answer