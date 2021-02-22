from collections import deque
                
n,m = map(int,input().split())
graph = [list(map(int,input().split())) for _ in range(n)]
dx = (-1, -1, -1, 0, 0, 1, 1, 1)
dy = (-1, 0, 1, -1, 1, -1, 0, 1)
queue = deque()

def bfs() :
    while queue :
        x,y = queue.popleft()
        for k in range(8) :
            nx, ny  = x+dx[k] , y+dy[k]
            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                    continue
            if not graph[nx][ny]:
                queue.append((nx, ny))
                graph[nx][ny] = graph[x][y]+1
for i in range(n):
    for j in range(m) :
        if graph[i][j] :
            queue.append((i,j))
bfs()
print(max(map(max,graph))- 1)
print(list(map(max,graph)))