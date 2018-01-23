import score
from def_login import login


students =[
    # 이름, 국, 영, 수, 총점, 평균, 순위
    ['hong', '홍길동', 100, 90, 80, -1, -1, -1],
    ['kim','김세진', 90, 90, 80, -1, -1, -1],
    ['gogo', '고길동', 70, 90, 40, -1, -1, -1],
    ['my','마이콜', 40, 70, 90, -1, -1, -1],
    ['hehe','희동이', 40, 70, 90, -1, -1, -1],
    ['dow','도우너', 30, 70, 90, -1, -1, -1],
]
score.sum(students)
score.average(students)
score.rank(students)

def do_by_student(user_id):
    while True:
        score.print_menu(False)
        select = input('메뉴선택 : ')
        if select == 'p':
            score.print_myscore(students, user_id)
        elif select == 'x':
            print('종료합니다.')
            break
        else:
            print('올바르지 않은 메뉴입니다.')

def do_by_admin():
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


if __name__ == '__main__' :
    user_id = login()

    if user_id :
        if user_id == 'admin':
            do_by_admin()
        else :
            do_by_student(user_id)
    else :
        print('로그인 실패 - 다시 실행 하세요')

