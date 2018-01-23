members = {
  'admin' : '1234',
  'hong' : '1234',
  'mikol' : '1234',
  'ggd1' : '1234',
  'ggd2' : 'abcd',
  'ksg' : 'abcd'
}

def check_user_password(user_id, password):
    if(members[user_id] == password):
        return True
    else:
        return False


def set_user_info(user_id, password):
    members[user_id] = password

def login():
    userId = None
    for tryCount in range(3):
        if userId == None:
            print('사용자 ID를 입력하세요 : ', end='>')
            userId = input()

        print('비밀번호를 입력하세요 : ', end='>')
        userPassword = input()

        if userId in members.keys():
            password = members[userId]
            if userPassword == password:
                return userId
            else:
                print('비밀번호가 일치하지 않습니다.')
        else:
            print('%s는 존재하지 않은 사용자 ID 입니다.'%(userId))
            userId = None
    return None


if __name__ == '__main__':
    result = login()
    if result:
        print('로그인 성공')
    else:
        print('로그인 실패')








