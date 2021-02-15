from collections import deque
def bfs (numbers,target) :
    #완전탐색
    #bfs,dfs
    answer = 0
    queue = deque([(0,0)])
    while queue :
        c_sum,n_idx=queue.popleft()
        if(n_idx == len(numbers)) :
            if(c_sum == target) :
                answer +=1
        else:
            queue.append((c_sum+numbers[n_idx], n_idx+1))
            queue.append((c_sum-numbers[n_idx], n_idx+1))
    return answer    

def solution(numbers, target):
    answer = bfs(numbers,target)

    return answer