import score
from login1 import set_user_info


def get_user_id(students):
    while True:
        name = input('새로운 사용자 ID :')
        name = name.strip()
        if name == 'c' or name == 'C':
            return None
        elif name=='':
            continue

        student = score.find_by_user_id(students, name)
        if student:
            print('%s는 이미 사용중인 ID 입니다', name)
        else:
            return name

def find_user_id(students):
    while True:
        name = input('사용자 ID :')
        name = name.strip()
        if name == 'c' or name == 'C':
            return None
        elif name=='':
            continue

        student = score.find_by_user_id(students, name)
        if student:
            return name
        else:
            print('%s는 존재하지 않는 ID 입니다', name)


def get_user_name():
    while True:
        name = input('사용자 이름 :')
        name = name.strip()
        if name=='':
            continue
        return name


def get_password():
    while True:
        password1 = input('비밀번호 : ')
        password2 = input('비밀번호 확인 : ')
        if password1 == password2:
            return password1
        print('비밀번호가 일치하지 않습니다. 다시 입력하세요')

def get_score(title):
    while True:
        score = input(title)
        if(score.isnumeric()):
            return int(score)
        print('숫자만 입력하세요')


def get_scores():
    kor = get_score('국어 점수 : ')
    eng = get_score('영어 점수 : ')
    math = get_score('수학 점수 : ')
    return kor, eng, math


def add_student(students):
    user_id = get_user_id(students)
    if not user_id :
        return

    user_name = get_user_name()     # 사용자 이름 입력
    password = get_password()       # 패스워드 입력
    kor, eng, math = get_scores()   # 점수 입력

    data = [user_id, user_name, kor, eng, math, -1, -1, -1]
    students.append(data)

    set_user_info(user_id, password)
    # members[user_id] = password     # 사용자 ID, 비밀번호 설정

    # 총점, 평균 계산, 등수 조정
    score.calc_total(students)
    score.calc_average(students)
    score.calc_rank(students)
    

def modify_score(students):
    user_id = find_user_id(students)
    if not user_id:
        return

    print('새로운 점수를 입력하세요')
    kor, eng, math = get_scores()  # 점수 입력

    # 수정은 어떻게?
    score.modify_score(students, user_id=user_id, kor=kor, math=math, eng=eng)

    score.calc_rank(students)


def print_menu():
    print('성적관리 메뉴')
    print('출력(P) | 사용자 추가(A) | 점수 수정(M)  | 검색 (S) | 종료(X)')


def do_by_admin(students):
    while True:
        print_menu()
        select = input('메뉴 선택 : ')
        if select == 'P':
            score.print_score(students)
        elif select == 'A':
            add_student(students)
        elif select == 'M':
            modify_score(students)
        elif select == 'S':
            score.search(students)
        elif select == 'X':
            print('종료합니다.')
            break
        else:
            print('올바르지 않은 입력입니다.')

