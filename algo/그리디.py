# n = 1260
# count = 0

# coin_types = [500,100,50,10]

# for coin in coin_types :
#     count += n // coin # 해당 화폐로 거슬러 줄 수 있는 동전의 개수 세기
#     n %= coin

# print(count)

# 큰 수의 법칙 (이렇게 하면 m의 갯수가 커지게 되면 시간초과 일어난다.)

# n,m,k = map(int, input().split())

# data = list(map(int,input().split()))

# data.sort()
# first = data[n-1];
# second = data[n-2]

# result = 0

# while True :
#     for i in range(k) :
#         if m ==0 :
#             break
#         result += first
#         m -= 1
#     if m ==0 :
#         break
#     result += second
#     m -= 1

# print(result)



# n,m = map(int, input().split())

# result = 0

# for i in range(n) :
#     data = list(map(int,input().split()))

#     min_value = min(data)
#     result = max(result,min_value)

# print(result)

# n,m = map(int, input().split())
# result = 0
# for i in range(n) :
#     data = list(map(int,input().split()))
#     min_value = 10000
#     for k in range(m) :
#         if(data[k] < min_value) :
#             min_value = data[k]
#     if(result < min_value):
#         result = min_value

# print(result)

n,k = map(int, input().split())
answer = 0

while n > 1 :
    answer += 1
    if(n % k == 0 ) : n = n // k

    else: n -= 1

print(answer)
