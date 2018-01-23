from os.path import getsize

def copy_file(src, dest):
    bufsize = 1024
    fin = open(src, 'rb')
    fout = open(dest, 'wb')

    file_size = getsize(src)

    data = fin.read(bufsize)
    read_size = len(data)

    while data:
        fout.write(data)
        rate = read_size / file_size * 100
        print('복사 진행률: %.2f%%'%rate)
        data = fin.read(bufsize)
        read_size += len(data)

    print('%d 바이트 복사 완료'%file_size)
    fin.close()
    fout.close()

src_file =[
    'test1.txt',
    'test2.txt',
    'test3.txt'
]

dest_dir = 'C:/python-work/pycharm/day0108/copy/'

def get_filename(fpath):
    ix = fpath.rfind('/')

    if ix != -1:
        return fpath
    else:
        return fpath[ix+1:]

for src in src_file:
    dest = dest_dir +get_filename(src)
    print(dest)
    copy_file(src, dest)

print('총 %d개의 파일을 복사했습니다.'%(len(src_file)))


#
import os, glob

folder = 'C:/python-work/pycharm/day0108/copy'

file_list = os.listdir(folder)
print(file_list)

files = 'C:/python-work/pycharm/day0108/copy/*.txt'
file_list = glob.glob(files)
print(file_list)

#
import os
from os.path import getsize

def print_file_info(dir_path, file_list):
    total_size = 0
    print('-------------------------------')
    print('No\t파일명\t크기')
    print('-------------------------------')
    for ix, file in enumerate(file_list):
        size = getsize(dir_path + '/' + file)
        total_size += size
        print('%d\t%s\t%d' % (ix + 1, file, size))
    print('-------------------------------')
    print('총 %d개 파일, 총 %d 바이트' % (len(file_list), total_size))


def dir(dir_path, filter=None):

    if filter :
        file_list = glob.glob1(dir_path, filter)
    else:
        file_list = os.listdir(dir_path)

    print_file_info(dir_path, file_list)
    select_file = int(input('선택 >'))

    return file_list[select_file-1]

song = dir('C:/Temp/mp3', '*.mp3')
print(song)




dir('C:/Temp', '*.mp3')

