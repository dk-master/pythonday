# d= [0] * 100

# def fibo(x) :
#     if x == 1 or x == 2:
#         return 1
#     if d[x] != 0:
#         return d[x]
#     d[x] = fibo(x-1) + fibo(x-2)
#     return d[x]
# print(fibo(99))
# # topDown
# d[1]
# d[1] = 1
# d[2] = 1
# n = 99

# for i in range(3,n+1) :
#     d[i] = d[i-1] + d[i-2]

# #bottomUP
# 일반 재귀를 이용한 피보나치 수열
result = 0
def fibo(x) :

    if x <= 1 :
        return x
    else :
        return fibo(x-1) + fibo(x-2)
for i in range(1,10) :
    print(fibo(i),end = " ")

# 동적 프로그래밍을 이용한 피보나치 수열
fibo = []
for i in range(0,10) :
    if x < 2 :
        fibo.append(1)
    else :
        fibo.append(fibo[i-2] + fibo[i-1])