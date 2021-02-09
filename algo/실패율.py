def solution(N,stages) :
    result = {}
    denominator = len(stages)
    
    for stage in range(1,N+1) :
        if denominator != 0:
            count = stages.count(stage)
            result[stage] = count / denominator
            denominator -= count
        else :
            result[stage] = 0
    return sorted(result, key=lambda x : result[x], reverse = True)
            