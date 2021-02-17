def solution(numbers, hand):
    answer = ''
    phone = {1 : (0,0) ,2 : (0,1) ,3 : (0,2),
            4 : (1,0), 5 : (1,1), 6 : (1,2),
            7 : (2,0) ,8 : (2,1), 9 : (2,2),
            '*' : (3,0) , 0 : (3,1), '#' : (3,2)}
    left = '*'
    right = '#'
    for i in numbers :
        if i in [1,4,7]:
            answer += 'L'
            left = i
        elif i in [3,6,9]:
            answer += 'R'
            right = i
        elif i in [2,5,8,0] :
            if((abs(phone[i][0] - phone[left][0]) + abs(phone[i][1] - phone[left][1]))
            > (abs(phone[i][0] - phone[right][0]) + abs(phone[i][1] - phone[right][1]))):
                answer += 'R'
                right = i
            elif((abs(phone[i][0] - phone[left][0]) + abs(phone[i][1] - phone[left][1]))
            < (abs(phone[i][0] - phone[right][0]) + abs(phone[i][1] - phone[right][1]))):
                answer += 'L'
                left = i
            else :
                if(hand == 'left') :
                    answer += 'L'
                    left = i
                else :
                    answer += 'R'
                    right = i
                                                            
    return answer
