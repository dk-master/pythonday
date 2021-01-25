data = input()
result = []
value = 0

for x in data:
    if x.isalpha():
        result.append(x)
    else:
        value += int(x)
result.sort()
if value != 0: # 숫자가 하나이상 존재한다면
    result.append(str(value))
print(''.join(result)) # 리스트를 문자열로 변환해서 출력