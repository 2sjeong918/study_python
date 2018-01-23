from Contact import Contact

class ContactBook :
    def __init__(self):
        self.contact_list=[
            Contact('홍길동', '010-1111-2222', 'hong@gmail.com'),
            Contact('고길동', '010-1111-2222', 'gogo@gmail.com'),
            Contact('마이콜', '010-3333-2222', 'micol@gmail.com'),
            Contact('도우너', '010-2222-2222', 'donut@gmail.com'),
        ]

    def add_contact(self):
        print('주소록 정보를 입력하세요')
        name =input('이름 : ')
        cell_phone = input('전화번호 : ')
        email = input('이메일 : ')
        address = input('주소 : ')
        birthday = input('생일 : ')
        if not name or cell_phone :
            print('이름과 전화번호는 필수입력입니다.')
            return
        contact = Contact(name, cell_phone, email, address, birthday)
        self.contact_list.append(contact)


    def print(self):
        print('------------------------------------------------')
        print('NO   이름   전화번호       이메일')
        print('------------------------------------------------')
        for ix, contact in enumerate(self.contact_list):
            print('%-4d'%(ix+1), end='')
            contact.print()
        print('------------------------------------------------')
        print('총 %d 명'%(len(self.contact_list)))

    def search(self):
        name = input('검색할 이름 : ')
        name = name.strip()
        if not name :
            print('검색할 이름이 없습니다.')
            return
        for contact in self.contact_list:
            if name == contact.get_name():
                self.print_detail(contact)
                break
        # for문을 다 돌고 나서도 break가 되지 않았을 때 실행
        else:
            print('%s는 주소록에 없습니다.'%name)

    def print_detail(self, contact):
        print('###############################')
        contact.print_detail()
        print('###############################')

    def update_contact(self):
        pass

    def delete_contact(self):
        name = input('삭제할 이름 : ')
        index = -1
        for ix, contact in enumerate(self.contact_list):
            if name == contact.get_name():
                # self.contact_list.pop(ix)
                index = ix
                break
        if index != -1:
            self.contact_list.pop(index)
            print('%s 주소록을 삭제했습니다.'%name)
        else:
            print('%s는 주소록에 없습니다.'%name)
