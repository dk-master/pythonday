import math
def solution(progresses, speeds):
    answer = []
    temp = []
    front = 0
    for i,v in list(zip(progresses,speeds)) :
        temp.append(math.ceil((100-i) / v))
    print (temp)
    
    for i in range(len(temp)) :
        if(temp[i] > temp[front]) :
            answer.append(i-front)
            front = i
    answer.append(len(temp) - front)
        

    return answer