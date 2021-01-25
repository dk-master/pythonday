input_data = input()
row = int(input_data[1]) # 처음으로 받는 좌표의 위치를 아스키코드를 사용해서 숫자로 바꾼다.
column = int(ord(input_data[0])) - int(ord('a')) + 1

steps = [(-2,-1),(-1,-2),(1,-2),(2,-1),(2,1),(1,2),(-1,2),(-2,1)] # 기본 상하좌우에 해당하는 스텝들을 한번에 모아놨다.
result = 0
for step in steps :
    next_row  = row + step[0]
    next_column = column + step[1]
    if next_row >= 1 and next_row <=8 and next_column >=1 and next_column <=8 :
        result += 1
print(result)
