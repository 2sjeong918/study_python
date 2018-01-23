import score

def do_by_student(students, user_id):
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