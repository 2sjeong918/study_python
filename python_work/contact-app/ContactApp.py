from ContactBook import ContactBook
from Contact import Contact
from deco import PerformanceDecorator
from deco import NotificationDecorator
import json

# contact_book = ContactBook()
contact_book = None

def contact_decode(obj):
    if set(obj.keys()) == set(['__class__', '__args__', '__kw__']):
        cls = eval(obj['__class__'])
        return cls(*obj['__args__'], **obj['__kw__'])
    else:
        return obj
def load():
    global contact_book
    with open('contact.dat', 'r') as file:
        try:
            json_str = file.read()
            contact_book = json.loads(json_str, object_hook=contact_decode)
        except Exception as err:
            # print('contact.dat파일 읽기 에러: %s'%err)
            contact_book = ContactBook()
# def contact_encode(obj) :
#     return obj.as_dict()

def save():
    json_str = json.dumps(contact_book, indent=4, default=lambda obj: obj.as_dict())
    with open('contact.dat', 'w') as file:
        try:
            file.write(json_str)
        except Exception as err:
            print('contact.dat 파일 저장 에러 : %s'%err)

# for contact in contact_book:
#     # contact.print()
#     print(contact)

def print_menu():
    print('출력(P) | 추가(A) | 검색(S) | 수정(U) | 삭제(D) | 종료(X)')

def select_menu():
    select = input('메뉴를 선택하세요. > ')
    return select.upper()


@PerformanceDecorator
@NotificationDecorator
def main():
    load()
    while True:
        print_menu()
        command = select_menu()
        if(command == 'P'):
            contact_book.print()
        elif(command == 'A'):
            contact_book.add_contact()
        elif (command == 'S'):
            contact_book.search()
        elif (command == 'U'):
            contact_book.update_contact()
        elif (command == 'D'):
            contact_book.delete_contact()
        elif (command == 'X'):
            save()
            print('종료합니다.')
            break
        else:
            print('잘못된 메뉴입니다. 다시 입력하세요')

if __name__ =='__main__':
    main()