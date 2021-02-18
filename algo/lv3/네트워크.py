from collections import deque
def solution(n, computers):
    answer = 0
    visited = [0 for i in range(n)]
    # def dfs(computers, visited, start):
    #     # stack = [start]
    #     # while stack:
    #         if visited[start] == 0:
    #             visited[start] = 1
    #         for i in range(0, len(computers)):
    #             if computers[start][i] ==1 and visited[i] == 0:
    #                 dfs(computers,visited,i)
    
    def bfs(computers,visited,start) :
        queue = deque()
        queue.append(start)
        while queue :
            x = queue.popleft()
            for i in range(len(computers)) :
                if(computers[x][i] == 1 and visited[i] == 0) :
                    visited[x] = 1
                    queue.append(i)
    i = 0
    while 0 in visited:
        if visited[i] ==0:
            bfs(computers, visited, i)
            answer +=1
        i+=1
    return answer