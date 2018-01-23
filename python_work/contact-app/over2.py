from Contact import Contact

hong = Contact('홍길동', '010-1111-2222', 'hong@naver.com')
hong2 = Contact('홍길동', '010-1111-2222', 'hong@naver.com')
hong3 = hong
hong4 = Contact('홍길동4', '010-1111-2222', 'hong@naver.com')
go = Contact('고길동', '010-1111-3333', 'gogd@naver.com')

if hong == go:
    print('hong과 go는 동일한 인스턴스입니다.')
else:
    print('hong과 go는 다른 인스턴스입니다.')

if hong == hong2:
    print('hong과 hong2는 동일한 인스턴스입니다.')
else:
    print('hong과 hong2는 다른 인스턴스입니다.')

if hong == hong3:
    print('hong과 hong3는 동일한 인스턴스입니다.')
else:
    print('hong과 hong3는 다른 인스턴스입니다.')

if hong == hong4:
    print('hong과 hong4는 동일한 인스턴스입니다.')
else:
    print('hong과 hong4는 다른 인스턴스입니다.')

if hong == 'hong':
    print('hong과 "hong"는 동일한 인스턴스입니다.')
else:
    print('hong과 "hong"는 다른 인스턴스입니다.')
