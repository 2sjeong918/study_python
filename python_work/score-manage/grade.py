import score
import admin
import student
from def_login import login


students =[
    # 이름, 국, 영, 수, 총점, 평균, 순위
    ['hong', '홍길동', 100, 90, 80, -1, -1, -1],
    ['kim','김세진', 90, 90, 80, -1, -1, -1],
    ['gogo', '고길동', 70, 90, 40, -1, -1, -1],
    ['my','마이콜', 40, 70, 90, -1, -1, -1],
    ['hehe','희동이', 40, 70, 90, -1, -1, -1],
    ['dou','도우너', 30, 70, 90, -1, -1, -1],
]
score.sum(students)
score.average(students)
score.rank(students)


if __name__ == '__main__' :
    user_id = login()

    if user_id :
        if user_id == 'admin':
            admin.do_by_admin(students)
        else :
            student.do_by_student(students, user_id)
    else :
        print('로그인 실패 - 다시 실행 하세요')

