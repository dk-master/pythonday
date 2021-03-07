import sys
t = int(sys.stdin.readline())
i =0
result = []
while True:
    if i == t :
        break
    n = int(sys.stdin.readline())
    answer = 1
    graph = []
    for _ in range(n):
        graph.append(list(map(int,sys.stdin.readline().split())))
    graph1 = sorted(graph,key = lambda x : x[0])
    min = graph1[0][1]
    for j in range(1,n):
        if graph1[j][1] < min :
            answer +=1
            min = graph1[j][1]

# 이것은 커밋용

    i += 1
    result.append(answer)



for i in result :
    print(i)