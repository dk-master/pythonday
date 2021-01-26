def solution(n):
    answer = ''
    watermelon = "수박"
    for i in range (n) :
        answer += watermelon[i%2]
    return answer