from collections from deque

def bfs(x,y) :
    count = 1
    queue = deque((x,y))
    dx = [-1,1,0,0]
    dy = [0,0,1,1]
    while queue :
        x, y = queue.popleft()
        for i in range(4) :
            nx = x + dx[i]
            ny = y + dy[i]
            if nx <= -1 or nx >= m or ny <= -1 or ny >= n :
                continue
            if(graph[nx][ny] == 'W') :
                graph[nx][ny] = 0
                count += 1
                queue.append((nx,ny))
            if(graph[nx][ny] == 'B') :
                graph[nx][ny] = 0
                count += 1
                queue.append((nx,ny))
    return count

n,m = map(int, input().split())
graph = []
teamW = 0
teamB = 0
for i in range(m) :
    graph.append(list(map(str,input().split())))  

for i in range(m)
    for j in range(n) :
        if(graph[i][j] == 'W') :
            bfs(i,j)