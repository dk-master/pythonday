def solution(s):
    answer = []
    temp_list = s.split(" ")
    for temp in temp_list :
        s = ""
        for i in range (len(temp)) :
            if i%2 == 0 :
                s += temp[i].upper()
            else :
                s += temp[i].lower()
        answer.append(s)
    answer =' '.join(answer)
    return answer