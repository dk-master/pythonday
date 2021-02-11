import sys
sys.setrecursionlimit(10000)
from collections import deque 
# def dfs(x,y) :
#     dx = [1, -1, 0, 0, 1, -1, -1, 1]
#     dy = [0, 0, -1, 1, 1, 1, -1, -1]

#     for i in range(8):
#         nx = x+dx[i]
#         ny = y+dy[i]
#         if nx <= -1 or nx >= m or ny <=-1 or ny >=n :
#             continue
#         if graph[nx][ny] == 1:
#             graph[nx][ny] = 0
#             dfs(nx,ny)
def bfs(x,y) :
     dx = [1, -1, 0, 0, 1, -1, -1, 1]
     dy = [0, 0, -1, 1, 1, 1, -1, -1]   
     queue = deque()
     queue.append((x,y))
     while queue :
         x,y = queue.popleft()
         for i in range(8):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx <= -1 or nx >= m or ny <=-1 or ny >=n :
              continue
            if(graph[nx][ny] == 1) :
                graph[nx][ny] = 0
                queue.append((nx,ny))
         


while(True):
    n,m = map(int,input().split())
    if(n == 0 and m == 0):
        break
    graph = []
    result = 0
    for _ in range(m):
        graph.append(list(map(int,input().split())))

    for i in range(m):
        for j in range(n):
            if graph[i][j] == 1:
                bfs(i,j)
                result +=1

    print(result)


