def print_string(text, count) :
    for i in range(count) :
        print(text)
print_string('text', 3)

#  가변 매개변수

#  * 0개 이상 > 매개변수가 결정이 안되는 경우 사용
#  + 1개 이상
#  ? 0개 또는 1개

#  함수내에서 전역번슈를 쓰는 것은 권장되지 않음
#  써야할 일이 있을 경우 매개변수로 전역변수를 전달하는 것을 권장함
result = ''
def merge_string(*text_list) :
    global result
    # 전역변수를 사용하고 싶을 때 global을 붙이면 됨(권장되지는 않음)
    for i in text_list :
        result = result + i
    return result

def merge_string2(*text_list) :
    result = ''
    for i in text_list :
        result = result + i
    return result

merge_string('첫번째', '두번째', '세번째')
print(merge_string2('첫번째2', '두번째2', '세번째2'))
merge_string('첫번째', '두번째', '세번째')
print(result)

# def print_position(position) :
#     role = ''
#     if position == 'GK':
#         role = '골키퍼'
#     if position == 'FW':
#         role = '공격수'
#     if position == 'MF':
#         role = '미드필더'
#     if position == 'DF':
#         role = '수비수'
#     return role

def print_position(role) :
    return {
        'GK' : '골키퍼',
        'FW' : '공격수',
        'MF' : '미드필드',
        'DF' : '수비수'
    }[role]

def print_team(*players) :
    result = sorted(*players)
    print(result)

print_team(카시야스='GK', 호날두='FW', 알론소='MF', 페페='DF', 메시='FW', 박지성="MF", 손흥민="FW")
# 매개 변수 명이기 때문에 ''로 감싸지 않아도 됨

result = ''

def m_string(sep, *text_list) :
    global result
    for s in text_list :
        result = result + sep + s
        # print(sep, s)
    return result
def m_string2(sep, *text_list) :
    result = ''
    for s in text_list :
        result = result + sep + s
        # print(sep, s)
    return result

print(m_string('-', '아버지가', '방에', '들어가신다.'))
print(m_string2('*', '아버지가', '방에', '들어가신다.'))

def ogamdo(num) :
    for i in range(1, num+1) :
        print('제 {0}의 아해'.format(i))
        if i == 5:
            return

print(ogamdo(2))

#
def min_num(*arg) :
    min = arg[0]
    for i in arg :
        if i < min :
            min = i
    return min

print('최소갑: ',min_num(10,9,8,222,4,555,6,476))

def max_num(*arg) :
    max = arg[0]
    for i in arg :
        if i > max :
            max = i
    return max

print('최대갑: ',max_num(10,9,8,222,4,555,6,476))

# 여러개의 데이터를 리턴해야하는 경우
def min_max(*arg) :
    return min_num(*arg), max_num(*arg)

min_num, max_num = min_max(10,9,8,222,4,555,6,476)
print('최소, 최대', min_num, max_num)

def sum(*arg) :
    sum = 0
    for i in arg :
        sum += i
    return sum

print('합: ', sum(10,9,8,222,4,555,6,476))

def average(*arg) :
    # sum = 0
    # for i in arg :
    #     sum += i
    return sum(*arg)/len(arg)

data = [10,9,8,222,4,555,6,476]
print('평균: ', average(*data))



