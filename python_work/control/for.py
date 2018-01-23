# for i in (1, 2, 3) :
#     print(i)

# for s in ['뇌를', '자극하는', '파이썬'] :
#     print(s)

# for s in '뇌를 자극하는 파이썬' :
#     print(s)

# for i in range(0, 10, 2) :
#     print(i)

# for i in range(1, 6) :
#     for j in range(i) :
#         print('*', end = "" )
#     print()

# for i in range(1, 10) :
#     for j in range(1, i+1) :
#         print('{0} x {1} = {2}'.format(i, j, i*j))
#     print()

# for i in range(1, 10) :
#     for j in range(1, i+1) :
#         print('{0} x {1} = {2}'.format(i, j, i*j))
#         if i == j :
#             break
#     print()

# dic = {
#     'a' : 'aaa',
#     'b' : 'bbb',
#     'c' : 'ccc'
# }
#
# for k, v in dic.items() :
#     print('{0} : {1}'. format(k, v))

# for i in range(10) :
#     if i % 2 == 1 :
#         continue
#     print(i)


# a = None
# for i in range(3) :
#     dic = {'hong': '1234',
#            'kim': '1111',
#            'park': '0000',
#            'song': '2222',
#            'lee': '3333'}
#     if a == None :
#         print('아이디를 입력하세요: ')
#         a = input()
#     print('비밀번호를 입력하세요: ')
#     b = input()
#
#     if a in dic.keys():
#         if b == dic[a]:
#             print('로그인에 성공하였습니다.')
#             break
#         else:
#             print('비밀번호가 틀렸습니다.')
#     else:
#         print('존재하지 않는 아이디 입니다.')
#         a = None

# list = [1,2,3]
# for i in list :
#     print(i)
#     break
# else :
#     print('perfect')

print('수를 입력하세요')
num = int(input())

total = 0
count = 1
while True :
    total = total + count
    print(num)
    print(total)
    if count > num :
        break
    count = count + 1
