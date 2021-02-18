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
    graph[x][y] =0 # 처음 1로 방문처리
    queue.append((x,y)) # 큐에 넣고 처음엔 들어가있는 상태여야하니까~
    while queue :
        x,y = queue.popleft()   # 그리고 꺼낸다.방문처리해준노드의 자식노드들 다 방문 (상하좌우)
        for i in range(4) :
            nx = x + dx[i]
            ny = y + dy[i]
            if nx <= -1 or nx >= n or ny <=-1 or ny >=n :
                continue
            if(graph[nx][ny] == 1) :
                count +=1 `# 단지갯수 세기
                graph[nx][ny] = 0 # 방문처리 
                queue.append((nx,ny)) # 상하좌우에 해당하는 노드를 큐에 삽입 
    return count

        
for i in range(n) :
    for j in range(n) :
        if graph[i][j] == 1 :
            counter.append(bfs(i,j))
            result += 1

print(result)
for count in sorted(counter) :
    print(count)