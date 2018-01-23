import score
from login1 import login

from admin import do_by_admin
from student import do_by_student

students = [
    # user_id, 이름, 국어, 영어, 수학, 총점, 평균, 순위
    ['ksg', '김세진', 90, 90, 90, -1, -1, -1],
    ['mikol', '마이콜', 80, 70, 60, -1, -1, -1],
    ['ggd1', '고길동', 70, 90, 40, -1, -1, -1],
    ['ggd2', '고길동', 60, 80, 80, -1, -1, -1],
    ['hong', '홍길동', 100, 90, 80, -1, -1, -1],
]

score.calc_total(students)
score.calc_average(students)
score.calc_rank(students)

if __name__ == '__main__':
    while True:
        user_id = login()

        if user_id: # 로그인 성공
            if user_id == 'admin': # 관리자인 경우
                do_by_admin(students)
            else:   # 학생인 경우
                do_by_student(students, user_id)
        else: # 로그인 실패
            print('로그인 실패 - 다시 실행하세요.')
