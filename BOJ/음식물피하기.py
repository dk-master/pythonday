# from collections import deque
# n,m,k = map(int,input().split())
# graph = []

# def bfs(x,y) :
#     queue = deque()
#     queue.append((x,y))
#     dx = [-1,1,0,0]
#     dy = [0,0,1,1]
#     count = 1
#     while queue :
#         x, y = queue.popleft()
#         for i in range(4) :
#             nx = x + dx[i]
#             ny = y + dy[i]
#             if nx <= -1 or nx >= n or ny <= -1 or ny >= m :
#                 continue
#             if(graph[nx][ny] == 1) :
#                 graph[nx][ny] = 0
#                 queue.append((nx,ny))
#                 count += 1
#     return count




# for i in range(n) :
#     temp = []
#     for j in range(m) :
#         temp.append(0)
#     graph.append(temp)
# for _ in range(k) :
#     x,y = map(int,input().split())
#     graph[x-1][y-1] = 1
# print(graph)

# result = []
# for i in range(n) :
#     for j in range(m) :
#         if(graph[i][j] == 1) :
#             temp = bfs(i,j)
#             result.append(temp)

# print(max(result))


import sys
sys.setrecursionlimit(10000)

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def dfs(x, y):
    visited[x][y] = 1
    global cnt
    cnt += 1
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 1 <= nx < n + 1 and 1 <= ny < m + 1:
            if visited[nx][ny] == 0 and aisle[nx][ny] == 1:
                dfs(nx, ny)


n, m, k = map(int, sys.stdin.readline().split())
aisle = [[0] * (m + 1) for _ in range(n + 1)]
visited = [[0] * (m + 1) for _ in range(n + 1)]

for _ in range(k):
    r, c = map(int, sys.stdin.readline().split())
    aisle[r][c] = 1

max_ = 0
for i in range(1, n + 1):
    for j in range(1, m + 1):
        if aisle[i][j] == 1 and visited[i][j] == 0:
            cnt = 0
            dfs(i, j)
            max_ = max(max_, cnt)

print(max_)
