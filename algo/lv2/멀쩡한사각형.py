import math
def solution(w,h):
    answer = 1
    return w*h - (w+h -(math.gcd(w,h)))