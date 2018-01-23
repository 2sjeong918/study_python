print('수를 입력하세요 : ')
num = int(input())
if num > 10 :
    if num % 2 == 0 :
        print('10보다 큰 짝수')
    else :
        print('10보다 큰 홀수')
else :
    if num % 2 == 0 :
        print('10보다 작은 짝수')
    else :
        print('10보다 작은 홀수')