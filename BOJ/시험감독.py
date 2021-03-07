import math
n = int(input())
graph = list(map(int,input().split()))
answer = 0
b , c = map(int,input().split())

for i in graph :
    if (i-b) <= 0 :
        answer += 1
    else :
        answer += 1
        answer += math.ceil((i-b) / c)
print(answer)
            