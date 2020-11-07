
people = [70,50,80,50]
# 50 50 70 80
limit = 100
def solution(people, limit):
    answer = 0
    people_sort = sorted(people)
    print(people_sort)
    temp = []
    boat = []
    for i in range (len(people_sort)) :
        if(sum(boat) < limit) :
            boat.append(people_sort[i])
            if(sum(boat) > limit) :
                
        elif(sum(boat) >= limit):
            temp.append(boat)
            boat = []
            boat.append(people_sort[i])
    answer = len(temp)
    print(temp)
    return answer

print(solution(people,limit))
