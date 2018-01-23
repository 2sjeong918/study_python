# file = open('C:/Temp/test.txt', 'w')
# file.write('hello')
# file.close()

file = open('C:/Temp/test.txt', 'r')
str = file.read()
print(str)
file.close()

with open('C:/Temp/test.txt', 'r') as file:
    str = file.read()
    print(str)

with open('C:/Temp/test_utf8.txt', 'r', errors='ignore') as file:
    str = file.read()
    print(str)