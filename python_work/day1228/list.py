# solarsys = ['태양', '수성', '금성', '지구', '화성', '목성', '토성', '천왕성', '해왕성']
#
# search = input('행성이름을 입력하세요: ' )
# new = input('새로운 이름을 입력하세요: ' )
#
# for i in range(len(solarsys)) :
#     if solarsys[i] == search :
#         solarsys[i] = new
#         break
#     else :
#         print('등록되지 않은 행성입니다.')
#         break
# print(solarsys)

# listdata = []
# for i in range(3) :
#     txt = input('리스트에 추가할 값을 입력하세요[%d/3]: ' %(i+1))
#     listdata.append(txt)
#     print(listdata)

# namelist = ['Mary', 'Sams', 'Aimy', 'Tom', 'Michale', 'Bob', 'Kelly']
#
# namelist.sort()
# print(namelist)
# print(sorted(namelist, reverse=True))
# print(namelist)


from random import shuffle

listdata = list(range(1, 11))

for i in range(3) :
    shuffle(listdata)
    print(listdata)

# min = listdata[0]
#
# for i in listdata :
#     for j in range(len(listdata)) :
#         if i <= listdata[j] and i <= int(min)  :
#             min = i
# print(min)

# max = listdata[0]
#
# for i in listdata :
#     if i > max :
#         max = i
#
# print(max)
# print(listdata.index(max))
#
# indexlistdata = list(enumerate(listdata))
#
# max = listdata[0]
# maxindex = 0
#
# for i, value in indexlistdata :
#     if value > max :
#         max = value
#         maxindex = i
#
# print(max, maxindex)

# result = []
#
# while listdata:
#     min = listdata[0]
#     minindex = 0
#     for i, value in enumerate(listdata) :
#         if value < min :
#             min = value
#             minindex = i
#     result.append(min)
#     listdata.pop(minindex)
# print(result)
#
# solar1 = ['태양', '수성', '금성', '지구', '화성', '목성', '토성', '천왕성', '해왕성']
# solar2 = ['Sun', 'Mercury', 'Venus', 'Earth', 'Mars', 'Jupiter', 'Saturn', 'Uranus', 'Neptune']
# solardic = {}
# for i, v in enumerate(solar1) :
#     val = solar2[i]
#     solardic[v] = val
#
# print(solardic)
#
# names = {
#     'Mary':10999, 'Sams':2111, 'Aimy':9778, 'Tom':20245, 'Michale':27115, 'Bob':5887, 'Kelly':7855
# }
# sort = sorted(names)
# print(sort)

