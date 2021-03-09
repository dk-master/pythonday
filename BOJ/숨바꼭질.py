from collections import deque
visited = [0] * 100001
def bfs(x,y) :
    queue = deque()
    queue.append((x,y))
    while queue :
            x,y = queue.popleft()
            if x == k :
                return y
            y += 1
            a = x + 1
            if a <= 100000 and visited[a] == 0 :
                queue.append((a,y))
                visited[a] = 1
            b = x - 1
            if b >= 0 and visited[b] == 0:
                queue.append((b,y))
                visited[b] = 1
            c = 2 * x
            if visited[c] and c <= 100000 :
                queue.append((c,y))
                visited[c] = 1


n,k = map(int,input().split())
print(bfs(n,0))



