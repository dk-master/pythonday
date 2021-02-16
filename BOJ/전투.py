def dfs(x,y) :
    global W
    global B
    dx = [-1,1,0,0]
    dy = [0,0,-1,1]
    if(x <= -1 or x>=m or y<-1 or y>=n):
        return False
    for i in range(4) :
        nx = x + dx[i]
        ny = y + dy[i]
        if(graph[nx][ny] == 'W') :
            graph[nx][ny] = 0
            W += 1
        if(graph[nx][ny] == 'B') :
            graph[nx][ny] = 0
            B += 1
        dfs(nx,ny)
    return True 
        


n , m = map(int, input().split())
first = 0
last = 0
graph = []
for _ in range(m) :
    graph.append(list(map(str,input())))

for i in range(m) :
    for j in range(n) :
        if(dfs(i,j)==True) :
            first = W*W
            W = 0
            last = B*B
            B = 0

print(first,last)
            