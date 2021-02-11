from collections import deque

# def BFS(graph,start,visited) :
#     queue = deque([start]) # start가 들어있는 리스트를 queue로 만들어준다.
#     visited[start] = True
    
#     while queue :
#         v = queue.popleft()
#         for i in graph[v] :
#             if not visited[i] :
#                 queue.append(i)
#                 visited[i] = True

def DFS(graph,start,visited) :
    visited[start] = True

    for i in graph[start] :
        if not visited[i] :
            DFS(graph,i,visited)

n = int(input())
m = int(input())
graph = [ [] for _ in range(n+1)]

for i in range (m) :
    a,b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

    
visited = [False] * (n+1)
# BFS(graph,1,visited)
DFS(graph,1,visited)
print(visited)
print(visited.count(True) - 1)