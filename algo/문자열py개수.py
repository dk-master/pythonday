def solution(s):
    answer = True
    p = 0
    y = 0
    for i in range (len(s)) :
        if(s[i] == 'p' or s[i] == 'P'):
            p += 1
        if(s[i] == 'y' or s[i] == 'Y'):
            y += 1
    if (y != p) :
        answer = False
    return answer