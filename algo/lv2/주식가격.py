def solution(prices):
    answer = []
    for i in range(len(prices)) :
        for j in range(i,len(prices)) :
            if(prices[i] - prices[j] > 0) :
                answer.append(j-i)
                break
            if(j == (len(prices) - 1)):
                answer.append(j-i)
                break
                
    return answer