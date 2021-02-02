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
            print(arr1[i])
            print(arr2[j])
            print(arr1[i][j] == '1' or arr2[i][j] == '1')
            if(arr1[i][j] == '1' or arr2[i][j] == '1' ):
                temp += '#'
            else :
                temp += ' '
        answer.append(temp)
    return answer