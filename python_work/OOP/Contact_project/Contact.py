class Contact:
    def __init__(self, name, cell_phone, email = '', address = '', birthday = ''):
        self.name = name
        self.cell_phone = cell_phone
        self.email = email
        self.address = address
        self.birthday = birthday

    def get_name(self):
        return self.name

    def set_name(self, new_name):
        self.name = new_name

    def get_cell_phone(self):
        return self.cell_phone

    def set_cell_phone(self, cell_phone):
        self.cell_phone = cell_phone

    def get_email(self):
        return self.email

    def set_email(self, email):
        self.email = email

    def get_address(self):
        return self.address

    def set_address(self, address):
        self.address = address

    def get_birthday(self):
        return self.birthday

    def set_birthday(self, birthday):
        self.birthday = birthday

    def print(self):
        print('%-5s %-15s %-20s'%(self.name, self.cell_phone, self.email))

    def print_detail(self):
        print('이름 : ', self.name)
        print('전화번호 : ', self.cell_phone)
        print('이메일 : ', self.email)
        print('주소 : ', self.address)
        print('생일 : ', self.birthday)
