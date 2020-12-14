# array = [1,5,2,4,5,6,8];
# target = 6

# def binary_search(array,target,start,end) :
#     array.sort()
#     mid = (start+end) // 2
#     if(array[mid] == target) :
#         return mid
#     elif(array[mid] > target) :
#         return binary_search(array,target,start,mid-1)
#     elif(array[mid] < target) :
#         return binary_search(array,target,mid+1,end)

# print(binary_search(array,target,0,6))
from sys import stdin
n,m = map(int, stdin.readline().rstrip().split())
tteoks = list(map(int, stdin.readline().rstrip().split()))

start = 0
end = max(tteoks)

result =0
while start< end:
    total = 0
    mid = (start + end) // 2

    #자른떡 길이 구하기