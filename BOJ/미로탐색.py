from collections import deque

def bfs(x,y) :
    queue = deque()
    queue.append((x,y))
    dx = [-1,1,0,0]
    dy = [0,0,1,1]
    while queue :
        x, y = queue.popleft()
        for i in range(4) :
            nx = x + dx[i]
            ny = y + dy[i]
            if nx <= -1 or nx >= n or ny <= -1 or ny >= m :
                continue
            if(graph[nx][ny] == 1) :
                graph[nx][ny] +=graph[x][y]
                queue.append((nx,ny))


n,m = map(int, input().split())
graph = []
for i in range(n) :
    graph.append(list(map(int,input())))  

bfs(0,0)

print(graph[n-1][m-1])