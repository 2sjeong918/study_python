from ContactBook import ContactBook
from deco import PerformanceDecorator
from deco import NotificationDecorator
contact_book = ContactBook()


for contact in contact_book:
    # contact.print()
    print(contact)

def print_menu():
    print('출력(P) | 추가(A) | 검색(S) | 수정(U) | 삭제(D) | 종료(X)')

def select_menu():
    select = input('메뉴를 선택하세요. > ')
    return select.upper()


@PerformanceDecorator
@NotificationDecorator
def main():
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
            # contact_book.save()
            print('종료합니다.')
            break
        else:
            print('잘못된 메뉴입니다. 다시 입력하세요')

if __name__ =='__main__':
    main()