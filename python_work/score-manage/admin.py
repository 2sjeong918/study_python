import score
from def_login import members

# 사용자 추가
# 학생 정보입력, 아이디 중복확인
def get_user_id(students) :
    while True :
        id = input('새로운 사용자의 아이디 : ')
        id = id.strip()
        if id == 'c' or id == 'C':
            return
        elif id=='' :
            continue

        student = score.find_by_user_id(students, id)
        if student :
            print('%s는 이미 등록된 사용자 아이디입니다.', id)
        else:
            return id

def get_user_name() :
    while True :
        name = input('새로운 사용자의 이름 : ')
        name = name.strip()
        if name =='':
            continue
        return name

def get_password():
    while True :
        password1 = input('비밀번호 : ')
        password2 = input('비밀번호 확인 : ')
        if  password1 == password2 :
            return password1

        print('비밀번호가 일치하지 않습니다. 다시 입력하세요')

def get_score(title):
    while True :
        score = input(title)
        if(score.isnumeric()):
            return int(score)
        print('숫자만 입력하세요')

def get_scores():
    kor = get_score('국어 점수 : ')
    eng = get_score('영어 점수 : ')
    math = get_score('수학 점수 : ')
    return kor, eng, math

def add_student(students) :
    user_id = get_user_id(students)
    if not user_id:
        return
    user_name = get_user_name() # 이름입력
    password = get_password() # 패스워드
    kor, eng, math = get_scores() # 점수입력

    data = [user_id, user_name, kor, eng, math, -1, -1, -1]
    students.append(data)

    members[user_id] = password  #사용자 아이디, 비밀번호 추가

    # 총점, 평균, 등수
    score.sum(students)
    score.average(students)
    score.rank(students)

def do_by_admin(students):
    while True:
        score.print_menu()
        select = input('메뉴선택 : ')
        if select == 'p':
            score.print_score(students)
        elif select == 's':
            score.search(students)
        elif select == 'x':
            print('종료합니다.')
            break
        else:
            print('올바르지 않은 메뉴입니다.')
