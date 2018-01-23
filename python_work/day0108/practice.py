from os.path import getsize

bufsize = 104;
fin = open('C:/Temp/test.jpg', 'rb')
fout = open('C:/Temp/test_copy.jpg', 'wb')

data = fin.read(bufsize)
while data:
    fout.write(data)
    data = fin.read(bufsize)


fin.close()
fout.close()

#
position = 100
size = 500

fin = open('article.txt', 'r')
fout = open('article_copy.txt', 'w')

fin.seek(position)
data = fin.read(size)

fout.seek(100)
fout.write(data)
# print(data)

file_size = getsize('article_copy.txt')
print(file_size)

fin.close()
fout.close()