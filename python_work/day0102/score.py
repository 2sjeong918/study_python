_USER_ID_IX = 0
_NAME_IX = 1
_KOR_IX = 2
_ENG_IX = 3
_MATH_IX = 4
_TOTAL_IX = 5
_AVG_IX = 6
_RANK_IX = 7
_SUBJECT_COUNT = 3

def sum(student) :
    for i in student :
        i[_TOTAL_IX] = i[_KOR_IX]+i[_ENG_IX]+i[_MATH_IX]

def average(student) :
    sum(student)
    for i in student :
        i[_AVG_IX] = i[_TOTAL_IX]/_SUBJECT_COUNT

def sort_total(x) :
    return x[_TOTAL_IX]

def sort_name(x) :
    return x[_NAME_IX]

def rank(students) :
    average(students)
    students.sort(key=sort_total, reverse= True)
    rank = 0
    old_score = -1
    for i, student in enumerate(students) :
        if old_score != student[_TOTAL_IX] :
            rank = i+1
            old_score =  student[_TOTAL_IX]

        students[i][_RANK_IX] = rank

def class_average(students) :
    total = 0
    for i in students :
        total=total+i[_AVG_IX]
    return total/len(students)

def print_student(scores):
    print('------------------------------------------------------')
    print(' 이름      국어    영어    수학    총점    평균  순위')
    print('------------------------------------------------------')
    for score in scores:
        print('%-5s  %5d  %5d  %5d     %5d    %.2f %5d' % (
            score[_NAME_IX], score[_KOR_IX],
            score[_ENG_IX], score[_MATH_IX],
            score[_TOTAL_IX], score[_AVG_IX], score[_RANK_IX]))
    #     - 가 붙으면 왼쪽부터 5칸 출력해라
    #     .2 가 붙으면 소수점 둘째까지
    print('------------------------------------------------------')

def print_score(scores, sort_fn = sort_name):
    avg = class_average(scores)
    scores.sort(key=sort_fn)
    print_student(scores)
    print('전체 평균 : %.2f'%avg)


def find_by_name(scores, name):
    result = []
    for score in scores :
        if name == score[_NAME_IX] :
            result.append(score)
    return result

def search(scores):
    name = input('이름: ')
    search_students = find_by_name(scores, name)
    if search_students :
        print_student(search_students)
    else:
        print('%s 학생이 없습니다.' %name)

def find_by_user_id(scores, id):
    for score in scores :
        if id == score[_USER_ID_IX] :
            return score
    return None

def print_myscore(scores, user_id):
    myscore = find_by_user_id(scores, user_id)
    print_student([myscore])

def print_menu(admin_mode=True) :
    print('성적관리 메뉴')
    if admin_mode:
        print('출력(p), 검색(s), 종료(x)')
    else :
        print('출력(p), 종료(x)')