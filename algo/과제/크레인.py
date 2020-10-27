
board = [[0,0,0,0,0],[0,0,1,0,3],[0,2,5,0,1],[4,2,4,4,2],[3,5,1,3,1]]
moves = [1,5,3,5,1,2,1,4]	
def solution(board, moves):
    answer = 0
    stack = []
    for i in range(len(moves)) :
        
        for j in range(len(board)) :
            
            if(board[j][moves[i]-1] != 0) :
                if(len(stack) != 0 and (stack[len(stack)-1] == board[j][moves[i]-1])) :
                    print("팝 전",stack)
                    print("들어가려던 숫자 : ",board[j][moves[i]-1])
                    stack.pop()
                    board[j][moves[i]-1] = 0
                    answer += 2
                    print("팝 후",stack)
                    break
                stack.append(board[j][moves[i]-1])
                board[j][moves[i]-1] = 0    
                print(board)
                break
    return answer      
print(solution(board,moves))