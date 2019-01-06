mystr = input('문자열을 입력하세요: ')

before_char = ''
current_char_cnt = 0
result = ''

for char in mystr:
    # 문자가 서로 다를 경우 
    if(before_char != char):
        # cnt가 1보다 큰 경우 > 유의미한 값 > 저장, 초기화
        if(current_char_cnt > 1):
            result += str(current_char_cnt)
        # result에 새로운 단어 저장하고 카운트 증가
        current_char_cnt = 0
        result += char
        current_char_cnt += 1

    # 같은 문자인 경우 카운트만 증가
    else:
        current_char_cnt += 1
    before_char = char

# 마지막 단어에 대한 cnt 값 체크
if(current_char_cnt > 1):
    result += str(current_char_cnt)

print(result)