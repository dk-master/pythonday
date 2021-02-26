import sys
sys.setrecursionlimit(10**7)
cache = [0] * 100002
def fibo(n):
    if n == 2:
        return 1

    if n ==  1:
        return 1
    if cache[n] != 0 :
        return cache[n]
    cache[n] = fibo(n-2)+fibo(n-1)
    return cache[n]

def solution(n):
    return fibo(n)%1234567