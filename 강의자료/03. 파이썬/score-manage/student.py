import score
import login1 as login

def print_menu():
    print('성적관리 메뉴')
    print('출력(P) | 비밀번호 변경(M) | ID 변경(I) | 종료(X)')

def change_password(user_id):
    old_password = input('이전 비밀번호 : ')
    new_password = input('새로운 비밀번호 : ')
    new_password2 = input('새로운 비밀번호 확인: ')

    # 이전 비밀번호 확인
    if login.check_user_password(user_id, old_password):
        if new_password == new_password2:
            login.set_user_info(user_id, new_password)
        else:
            print('새로운 비빌번호가 일치하지 않습니다.')
    else :
        print('이전 비빌번호가 일치하지 않습니다.')



def do_by_student(students, user_id):
    while True:
        print_menu()
        select = input('메뉴 선택 : ')
        if select == 'P':
            score.print_myscore(students, user_id)
        elif select == 'M':
            change_password(user_id)
        elif select == 'I':
            pass
        elif select == 'X':
            print('종료합니다.')
            break
        else:
            print('올바르지 않은 입력입니다.')

