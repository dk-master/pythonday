def solution(arr):
    result = [i for i in arr if(i>min(arr))]
    if(len(result) == 0) :
        result.append(-1)
    
    return result