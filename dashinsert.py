# 숫자로 된 문자열을 입력받음
mystr = input('숫자를 입력하세요: ')

# 홀수가 연속되면 두 수 사이에 -를 추가하고
# 짝수가 연속되면 두 수 사이에 *를 추가함
before_num_state = False    # 짝: True, 홀: False
is_first = True
result = ''
for num in mystr:
    current_num_state = (int(num) % 2 == 0)
    if(not is_first):
        # 현재 수의 짝, 홀 판별
        if (before_num_state and current_num_state):
            result += '*'
        elif ((not before_num_state) and (not current_num_state)):
            result += '-'
    else:
        is_first = False
    
    result += num
    before_num_state = current_num_state

print(result)