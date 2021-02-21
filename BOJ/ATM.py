n = int(input())
atm = list(map(int,input().split()))
atm.sort()
result = []
answer = 0
for num in atm :
    result.append(num)
    answer += sum(result)
print(answer)

