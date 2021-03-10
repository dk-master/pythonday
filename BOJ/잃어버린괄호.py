graph = list(map(str,input()))
answer = ''
plus = []
minus = []
print(graph)
for i in graph :
    if i.isdigit() :
        answer += i
    elif i == '-' :
        minus.append(int(answer))
        anaswer = ''
    elif i == '+' :
        plus.append(int(answer))
        answer = ''
print(sum(minus) - sum(plus))