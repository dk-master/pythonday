# 특정원소가 속한 집합을 찾기
def find_parent(parent,x) :
    if parent[x] != x :
        parent[x] = find_parent(parent,parent[x])
    return parent[x]


def union_parent(parent,a,b) :
    a = find_parent(parent,a)
    b = find_parent(parent,b)
    if a< b :
        parent[b] = a
    else :
        parent[a] = b

v, e = map(int, input().split())
parent = [0] * (v + 1) # 부모 테이블 초기화


for i in range(1, v + 1) :
    parent[i] = i

for i in range(m) :
    oper,a,b = map(int, input().split())
    # 합집합 연산인 경우
    if oper == 0 :
        union_parent(parent,a,b)
    # 찾기연산인 경우
    elif oper == 1 :
        if find_parent(parent,a) == find_parent(parent,b):
            print("Yes")
        else:
            print("No")