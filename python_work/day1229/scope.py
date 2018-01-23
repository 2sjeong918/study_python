def plus(a, b) :
    return a+b

def minus(a, b) :
    return a-b

first = [plus, minus]
print(first[0](1, 3))
#
def hello_korean():
    print('안녕하세요')

def hello_english():
    print('hello')

def greet(hello):
    hello()
print(greet(hello_english))
print(greet(hello_korean))
#

names = {
    'mary': 10999,
    'sams': 2334,
    'aimy': 9766,
    'tom': 86657
}
def f1(x) :
    return x[0]
def f2(x) :
    return x[1]

ret2 = sorted(names.items(), key=f1)
ret3 = sorted(names.items(), key=f2)
ret4 = sorted(names.items(), key=f2, reverse=True)
print(ret2)
print(ret3)
print(ret4)

#
def fn_position(x) :
    return x[1]

def fn_name(x) :
    return x[0]

def print_team(what, **players) :
    # print('players', players)
    result = sorted(players.items(), key=what)
    print(result)

def get_sort_fn() :
    stratege = input('선수정렬 방법을 선택하세요 1)이름순 2)포지션순 :')
    if stratege == '1' :
        return fn_name
    elif stratege == '2' :
        return  fn_position
    else :
        return None

# stratege = get_sort_fn()
# print_team(stratege, 카시야스='GK', 호날두='FW', 알론소='MF', 페페='DF', 메시='FW', 박지성="MF", 손흥민="FW")

#
dic = {
    'a': 1,
    'b': 2
}
# print('c', dic['c'])
#  없는 키를 입력하면 에러

#
import math
def stddev(*args):
    def mean():
        return sum(args)/len(args)
    def variance(m):
        total = 0
        for arg in args:
            total += (arg - m ) ** 2
        return total/(len(args)-1)
    v = variance(mean())
    return math.sqrt(v)

print(stddev( 2.3, 1.7, 1.4, 0.7, 1.9))


