# # 리스트 컴프리헨션
# array= [i for i in range(20) if i % 2 == 1]
# print(array)

# # 제곱값을 포함한 리스트
# array = [i * i for i in range(1,10)]
# print(array)

# # 2차원 리스트 초기화하기
# n = 3
# m = 4
# array = [[0] * m for _ in range(3)]
# array[1][1] = 5
# print(array)


# # remove_set에 포함되지 않은 값만을 지정
# a = [1,2,3,3,4,5,5,5,6]
# remove_set = {3,5}
# result = [i for i in a if i not in remove_set]
# print(result)


# a= "dk-master"
# print(a[1:3])

# # 튜플 () 은 최단경로 알고리즘에서 사용된다.

# #사전 자료형
# data = dict()
# data["사과"] = 'Apple'
# data["바나나"] = 'Banana'
# data["코코넛"] = 'coconut' 

# print(data)

# # 원소 in 사전
# if '사과' in data :
#     print("'사과'를 키로 가지는 데이터가 존재합니다.")



# def solution(n):
#     answer = 0
#     nam = []
#     mok = 0
#     while True:
#         nam.append(n%3)
#         mok = n // 3
#         if(mok <= 0) :
#             break
#         n = mok
#     print(nam)
#     for i in range(len(nam)) :
#         answer=answer+(nam[-(i+1)] * pow(3,i))
#     return answer

# print(solution(125))


# from itertools import combinations

# def solution(numbers):
#     answer = []
#     for a,b in combinations(numbers,2) :
#         temp = a + b
#         if temp not in answer:
#             print(temp)
#             answer.append(temp)

#     return answer
        
    

# print(sorted(solution([2,1,3,4,1])))


#크레인 인형뽑기 게임
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