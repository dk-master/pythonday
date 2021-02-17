def solution(s):
    # temp = list(filter(lambda x : max(s.split()) == x or min(s.split()) == x, s.split()))
    temp = list(map(int,s.split()))
    answer = ''
    answer += str(min(temp))
    answer += ' '
    answer += str(max(temp))
    return answer