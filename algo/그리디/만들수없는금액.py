from itertools import combinations

n = int(input())
answer = []
data = list(map(int,input().split()))
def solution(numbers):
    for i in range (numbers) :
        combi = list(combinations(data,i+1))
        for k in range (len(combi)) :
            answer.append(sum(combi[k]))
    return answer

result_set = set(solution(n))
result = list(result_set)
print(result)
dab = 0
for i in range(len(result)) :
    if (i+1 != result[i]) :
        dab = i+1
        break
    else :
        dab = len(result) + 1

print(dab)