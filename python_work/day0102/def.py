def swap2(listdata):
    t = listdata[0]
    listdata[0] = listdata[1]
    listdata[1] = t
    print(listdata)

numbers =[10, 20]
print(numbers)
swap2(numbers)
print(numbers)

numbers = [10, 20]
p = numbers
p[0] = 30
print(numbers)