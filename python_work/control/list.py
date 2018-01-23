list = ['첫번째', '두번째', '세번째', '네번째']

print('index를 입력해주세요')
index = int(input())

if 0 <= index < len(list) :
    print(list[index])

else :
    print('유효하지 않은 인덱스 입니다.')
    print('0~{0} 사이의 값을 입력하세요', format(len(list)-1))