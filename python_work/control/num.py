# 3, 4의 배수 찾기

print('숫자를 입력해주세요')
num = int(input())

if num % 3 == 0 or num % 4 == 0 :
    print('3 또는 4의 배수가 맞습니다.')
else :
    print('3, 4의 배수가 아닙니다.')