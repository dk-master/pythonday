a,b = map(int,input().split())
i = 0
answer = True
while b != a :
    if b % 2 == 0 :
        b = b // 2
    elif((b % 2 != 0 and int(str(b)[-1]) != 1) or (a>b)) :
        answer = False
        break
    else :
        b = int(str(b)[:-1])
    i += 1
if answer :
    print(i+1)
else :
    print(-1)