n,m = map(int,input().split())
data = list(map(int,input().split()))

array = [0] * 11
for x in data :
    array[x] +=1
# array 각 인덱스에 맞는 번호의 갯수 구할때 간단하게 구현할 수 있다. 자바스크립트에서 Map함수 has랑 같은 원리

for i in range(1,m+1) :
    n -= array[i]  # 리스트에서 한번 사용했던 볼링공들 제외시킨다. 조합이랑 같음
    result += array[i] * n  # 그리고 
