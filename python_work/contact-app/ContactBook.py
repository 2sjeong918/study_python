from Contact import Contact
from math import ceil   # 올림 함수 임포트
import json

def sort_by_name(contact):
    return contact.get_name()

_COUNT_PER_PAGE = 5

class ContactBook:
    def __init__(self, contact_list = None):
        if contact_list:
            self.contact_list = contact_list
        else:
            self.contact_list = [
                Contact('홍길동', '010-1111-2222', 'hong@naver.com'),
                Contact('고길동', '010-1111-3333', 'gogd@naver.com'),
                Contact('마이콜', '010-1111-4444', 'micol@gmail.com'),
                Contact('도우너', '010-1111-5555', 'donut@naver.com'),
                Contact('홍길동X', '010-1111-2222', 'hong@naver.com'),
                Contact('고길동X', '010-1111-3333', 'gogd@naver.com'),
                Contact('마이콜X', '010-1111-4444', 'micol@gmail.com'),
                Contact('도우너X', '010-1111-5555', 'donut@naver.com'),
                Contact('홍길동Y', '010-1111-2222', 'hong@naver.com'),
                Contact('고길동Y', '010-1111-3333', 'gogd@naver.com'),
                Contact('마이콜Y', '010-1111-4444', 'micol@gmail.com'),
                Contact('도우너Y', '010-1111-5555', 'donut@naver.com'),
                Contact('홍길동Z', '010-1111-2222', 'hong@naver.com'),
                Contact('고길동Z', '010-1111-3333', 'gogd@naver.com'),
                Contact('마이콜Z', '010-1111-4444', 'micol@gmail.com'),
                Contact('도우너Z', '010-1111-5555', 'donut@naver.com'),
            ]
        self.contact_list.sort(key=lambda c: c.get_name())

    def as_dict(self):
        return dict(
            __class__="ContactBook",
            __args__= [self.contact_list],
            __kw__ = {}
        )
    def add_contact(self):
        print('주소록 정보를 입력하세요')
        name = input('이름* : ')
        cell_phone = input('전화번호* : ')
        email = input('email : ')
        address = input('주소 : ')
        birthday = input('생일 : ')
        contact = Contact(name, cell_phone, email, address, birthday)
        self.contact_list.append(contact)

    def print_page(self):
        start = (self.page-1)*_COUNT_PER_PAGE
        end = start + _COUNT_PER_PAGE
        print('----------------------------------------')
        print('No  이름    전화번호      email')
        print('----------------------------------------')
        for ix, contact in enumerate(self.contact_list[start:end]):
            print('%-4d' % (start + ix +1), end='')
            contact.print()
        print('----------------------------------------')
        print('[%d/%d],  총 %d 명' %(self.page, self.total_page, self.total_count))

    def move_previous_page(self):
        if self.page > 1 :
           self.page -= 1
        self.print_page()

    def move_next_page(self):
        if self.page < self.total_page:
            self.page += 1
        self.print_page()

    def move_page(self):
        if self.page < 1 :
            self.page = 1
        elif self.page > self.total_page:
            self.page = self.total_page

        self.print_page()

    def print(self):
        self.page = 1
        self.total_count = len(self.contact_list)
        self.total_page = int(ceil(self.total_count/_COUNT_PER_PAGE))

        self.print_page()
        while True:
            select = input('> ')
            if select == 'P' or select == 'p':  # 이전 페이지
                self.move_previous_page()
            elif select == 'N' or select == 'n':    # 다음 페이지
                self.move_next_page()
            elif select == 'Q' or select == 'q':
                return
            else:   # 숫자 입력인지
                if select.isnumeric():
                    self.page = int(select)
                    self.move_page()



    def search(self):
        name = input('검색할 이름 : ')
        name = name.strip()
        if not name :
            print('검색할 이름이 없습니다.')
            return

        for contact in self.contact_list:
            if name == contact.get_name():
                self.print_detail(contact)
                return # break
        # else:
        print('%s는 주소록에 없습니다.'%name)


    def print_detail(self, contact):
        print('#################################################')
        contact.print_detail()
        print('#################################################')


    def update_contact(self):
        name = input('수정할 이름 : ')
        for contact in self.contact_list:
            if name == contact.get_name():
                break
        else:
            print('%s는 주소록에 없습니다.'%name)
            return

        print('전화번호 : ', contact.get_cell_phone())
        cell_phone = input('새 전화번화 :').strip()
        if cell_phone :
            contact.set_cell_phone(cell_phone)

        print('email : ', contact.get_email())
        email = input('새 email :').strip()
        if email :
            contact.set_email(email)

        print('주소 : ', contact.get_address())
        address = input('새 주소 :').strip()
        if address :
            contact.set_address(address)

        print('생일 : ', contact.get_birthday())
        birthday = input('새 생일 :').strip()
        if birthday :
            contact.set_birthday(birthday)

    def delete_contact(self):
        name = input('삭제할 이름 : ')
        index = -1
        for ix, contact in enumerate(self.contact_list):
            if name == contact.get_name():
                index = ix
                break

        if index != -1:
            self.contact_list.pop(index)
            print('%s 주소록을 삭제했습니다'%name)
        else:
            print('%s은 주소록에 없습니다.'% name)


    def __iter__(self):
        self.current = 0
        return self

    def __next__(self):
        total = len(self.contact_list)
        if self.current < total:
            current = self.current
            self.current += 1
            return self.contact_list[current]
        else:
            raise StopIteration()


