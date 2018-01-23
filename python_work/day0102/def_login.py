
user = {
    'admin': '0000',
    'hong': '1234',
    'kim': '1111',
    'gogo': '0000',
    'my': '2222',
    'hehe': '3333',
    'dow': '4444'
}

def login() :
    id = None
    for tryCount in range(3) :
        if id == None :
            id = input('아이디를 입력해주세요: ' )

        pw = input('비밀번호를 입력해주세요: ' )

        if id in user.keys() :
            if pw == user[id] :
                return id
            else :
                print('비밀번호가 틀렸습니다.')
        else :
            return False

print(__name__)
if __name__ == '__main__':
    result = login()
    if result:
        print('로그인 성공')
    else :
        print('로그인 실패')