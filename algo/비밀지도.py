def solution(n, arr1, arr2):
    answer = []
    for i in range (n) :
        arr1[i] = format(arr1[i],'b')
        arr2[i] = format(arr2[i],'b')
        if(len(arr1[i]) != n) :
            arr1[i] = '0' *(n-len(arr1[i])) + arr1[i]
        if(len(arr2[i]) != n) :
            arr2[i] = '0' *(n-len(arr2[i])) + arr2[i]
        temp = ''
        for j in range (len(arr1[i])):
            if(int(arr1[i][j]) or int(arr2[i][j]) == True):
                temp += '#'
            else :
                temp += ' '
        answer.append(temp)
    return answer