_USER_ID_IX = 0
_NAME_IX = 1
_KOR_IX = 2
_ENG_IX = 3
_MATH_IX = 4
_TOTAL_IX = 5
_AVG_IX = 6
_RANK_IX = 7
_SUBJECT_COUNT = 3  # 과목 수

def calc_total(scores):
    for score in scores:
        score[_TOTAL_IX] = score[_KOR_IX] + score[_ENG_IX] + score[_MATH_IX]
        # score[_TOTAL_IX] = sum(score[_KOR_IX:_TOTAL_IX])

def calc_average(scores):
    for score in scores:
        score[_AVG_IX] = score[_TOTAL_IX] / _SUBJECT_COUNT

def sort_total(x):
    return x[_TOTAL_IX]

def sort_name(x):
    return x[_NAME_IX]

def calc_rank(scores):
    scores.sort(key=sort_total, reverse=True)
    rank = 0
    old_score = -1
    for ix, score in enumerate(scores):
        if old_score != score[_TOTAL_IX]: # 이전값과 다른 경우에만 rank 수정
            rank = ix+1
            old_score = score[_TOTAL_IX]

        scores[ix][_RANK_IX] = rank



def get_average(scores):
    total = 0
    for score in scores:
        total += score[_AVG_IX]
    return total/len(scores)


def find_by_name(scores, name):
    result = []
    for score in scores:
        if name == score[_NAME_IX]:
            result.append(score)
    return result


def find_by_user_id(scores, user_id):
    for score in scores:
        if user_id == score[_USER_ID_IX]:
            return score
    return None


def find_index(scores, user_id):
    for ix, score in enumerate(scores):
        if user_id == score[_NAME_IX]:
            return ix
    return -1


def modify_score(scores, **args):
    ix = find_index(scores, args["user_id"])
    if ix == -1:
        print('%s는 존재하지 않습니다.'%args["user_id"])
        return

    score = scores[ix]
    # scores[ix][_KOR_IX] = args["kor"]

    score[_KOR_IX] = args["kor"]
    score[_ENG_IX] = args["eng"]
    score[_MATH_IX] = args["math"]

    score[_TOTAL_IX] = score[_KOR_IX] + score[_ENG_IX] + score[_MATH_IX]
    score[_AVG_IX] = score[_TOTAL_IX] / _SUBJECT_COUNT


# 지정한 user_id의 성적 데이터를 출력하는 함수
# 매개변수
#   scores : 전체 성적 리스트
#   user_id : 출력하고자하는 사용자 ID
# 리턴값 : 없음
def print_myscore(scores, user_id):
    myscore = find_by_user_id(scores, user_id)
    print_student([myscore])


def search(scores):
    name = input('검색할 이름 : ')
    search_students = find_by_name(scores, name)
    if search_students:
        print_student(search_students)
    else:
        print('%s 학생이 없습니다.'%name)


def print_student(scores):
    print('---------------------------------------------------------')
    print('이름    국어   영어   수학   총점    평균   순 위')
    print('---------------------------------------------------------')
    for score in scores:
        print('%-5s %5d %5d %5d  %5d  %.2f %5d'%(
                    score[_NAME_IX], score[_KOR_IX],
                    score[_ENG_IX], score[_MATH_IX],
                    score[_TOTAL_IX], score[_AVG_IX], score[_RANK_IX]))
    print('---------------------------------------------------------')


def print_score(scores, sort_fn=sort_name):
    avg = get_average(scores)
    scores.sort(key=sort_fn)
    print_student(scores)
    print('전체 평균 : %.2f'%avg)


