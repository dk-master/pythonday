def solution(x):
    answer = True
    return x % sum([int(i) for i in str(x)]) == 0