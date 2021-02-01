def solution(phone_number):
    answer = ''
    temp = len(phone_number) - 4
    last = phone_number[-4:]
    answer += '*'*temp
    answer += last
    return answer