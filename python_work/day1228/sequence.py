# def myfunc():
#     print('안녕하세요')
#
# list4 = [1, 3, myfunc]
#
# list4[2]()
#
# list3 = [1, 'a', 'abc', [1,2,3,4,5], ('a', 'b', 'c')]
#
# list3[3].append('abc')
# # list3[4][1] = 't'
# #  튜플은 수정불가
# print(list3)

# tuple = (1, 'a', 'abc', [1,2,3,4,5])
# tuple[3][1] = 0
# # 튜플 내의 리스트의 내부는 변경할 수 있다(리스트 자체는 변경불가)
# print(tuple)

# dic = {'a': 1,
#        'b': 2,
#        'c': {
#            'name' : 'sojeong',
#            'age' : '20'
#        }
#        }
# print(dic)
# dic['c']['age'] = 25
# print(dic)

# strdata = 'Time is money'
# listdata = [1, 2, [1, 2, 3]]
# # print(strdata[5])
# # print(listdata[2][-1])
# print(strdata[0:5: -1])

# artist = '빅뱅'
# sing = '뱅~'
# dispdata = artist +'이 부르는 '+ sing*3
# print(dispdata)

# txt = 'python'
#
# for i in range(len(txt)) :
#     print(txt[:i+1])

# txt = 'abcdefg'
# ret = txt[-2::-2]
# print(ret)

txt = 'A lot of Things occur each day.'
spelling = txt.lower()
# output = {}
# for i in spelling :
#     if not i in output.keys() :
#         if i == ' ' or i == '.' :
#             continue
#         output[i] = 0
#
#     output[i] = output[i] + 1
# print(output)

# output = []
#
# for i in range(26) :
#     output.append(0)
# start = ord('a')
#
# for i in spelling :
#     if i.isalpha() :
#         j = ord(i) - start
#
#         output[j] = output[j] + 1
# print(output)


# url = 'http://www.naver.com/news/today=20160831'
# log = 'name:홍길동 age:17 sex:남자 nation:조선'
#
# url = url.split('/')
#
# log = log.split(' ')
# for i in log :
#     d1, d2 = i.split(':')
#     print('{0} > {1}'.format(d1, d2))

# loglist = ['2016/08/26 10:12:11', '200', 'OK', '이 또한 지나가리라']
#
# # print(' '.join(loglist) )
# print('\n'.join(loglist) )

text = input( '문장을 입력하세요:' )

ret = ''
for i in range(len(text)) :
    if i != len(text)-1 :
        ret += text[i+1]
    else :
        ret +=text[0]
print(ret)
