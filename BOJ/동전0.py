n,k = map(int,input().split())
coins = []
for _ in range(n) :
    coins.append(int(input()))
answer = 0
coins.sort(reverse = True)
for coin in coins :
    if k // coin > 0 :
        answer += (k // coin)
        k = k % coin
print(answer)
