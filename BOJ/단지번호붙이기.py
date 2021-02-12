from collections import deque

n = int(input())
graph = []
result = 0
counter = []
for _ in range(n) :
    graph.append(list(map(int,input())))

def bfs(x,y) :
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]  
    queue = deque()
    count = 1
    graph[x][y] =0 # 처음 방문처리...
    queue.append((x,y))
    while queue :
        x,y = queue.popleft()   
        for i in range(4) :
            nx = x + dx[i]
            ny = y + dy[i]
            if nx <= -1 or nx >= n or ny <=-1 or ny >=n :
                continue
            if(graph[nx][ny] == 1) :
                count +=1
                graph[nx][ny] = 0
                queue.append((nx,ny))
    return count

        
for i in range(n) :
    for j in range(n) :
        if graph[i][j] == 1 :
            counter.append(bfs(i,j))
            result += 1

print(result)
for count in sorted(counter) :
    print(count)