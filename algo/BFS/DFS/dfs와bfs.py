from collections import deque

# BFS 메서드 정의
def bfs(real_graph, start,visited) :
    # 큐(Queue) 구현을 위해 deque 라이브러리 사용
    queue = deque([start])
    # 현재 노드를 방문 처리
    visited[start] = True
    #큐가 빌 때까지 반복
    while queue : 
        # 큐에서 하나의 원소를 뽑아 출력
        v = queue.popleft()
        print(v, end = " ")
        # 해당 원소와 연결된, 아직 방문하지 않은 원소들을 큐에 삽입
        for i in real_graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True
    
def dfs(real_graph,v,visited) :
    # 현재 노드를 방문 처리
    visited[v] = True
    print(v,end =' ')
    # 현재 노드와 연결된 다른 노드를 재귀적으로 방문
    for i in real_graph[v] :
        if not visited[i] :
            dfs(real_graph, i, visited)

n,m,v = map(int, input().split())
 # n - 정점  m - 간선  v - 탐색시작번호 ex) 1
graph = [[],]
for i in range(m) :
    graph.append(list(map(int,input().split())))
print(graph)
real_graph = [[],]
for i in range(1,n+1) :
    temp = []
    for k in range(1,m+1):
        if i in graph[k]:
            if graph[k].index(i) == 0 :
                temp.append(graph[k][1])
            else :
                temp.append(graph[k][0])
    temp.sort()
    real_graph.append(temp)
    temp = []
print(real_graph)
    # 각 노드가 방문된 정보를 리스트 자료형으로 표현(1차원 리스트)

visited = [False] * 9
dfs(real_graph,v,visited)
visited = [False] * 9    
bfs(real_graph,v,visited)



