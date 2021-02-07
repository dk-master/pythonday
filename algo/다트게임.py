def solution(dartResult):
    answer = 0
    beforeRecord = 0
    record = 0
    dartResult = dartResult.replace("10", "K")
    for i in range (len(dartResult)) :
        if(dartResult[i].isdigit() or dartResult[i]== 'K') :
            beforeRecord = record
            answer += record
            if dartResult[i] == 'K':
                record = 10
            else :
                record = int(dartResult[i])
        elif(dartResult[i] == 'S'):
            record = record * 1
        elif(dartResult[i] == 'D') :
            record = record ** 2
        elif(dartResult[i] == 'T') :
            record = record ** 3
        elif(dartResult[i] == '*') :
            answer = beforeRecord + answer
            record *= 2
        elif(dartResult[i] == '#') :
            record *= -1
    
    answer += record  
    return answer