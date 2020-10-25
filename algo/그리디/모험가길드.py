
n = int(input())

data = list(map(int,input().split()))

data.sort()

temp = []
count = 0

for i in range (n) :
    temp.append(data[i])
    if (len(temp) >= data[i] ) :
        count += 1
        temp = []

print(count)