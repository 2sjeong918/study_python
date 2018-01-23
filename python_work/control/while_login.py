
a = None
limit = 3
count = 0
while count < limit :
    count = count + 1
    dic = {'hong': '1234',
           'kim': '1111',
           'park': '0000',
           'song': '2222',
           'lee': '3333'}
    if a == None :
        print('아이디를 입력하세요: ')
        a = input()
    print('비밀번호를 입력하세요: ')
    b = input()

    if a in dic.keys():
        if b == dic[a]:
            print('로그인에 성공하였습니다.')
            break
        else:
            print('비밀번호가 틀렸습니다.')
    else:
        print('존재하지 않는 아이디 입니다.')
        a = None