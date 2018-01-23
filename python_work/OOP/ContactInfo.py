class ContactInfo :
    def __init__(self, name, email):
        self.name = name
        self.email = email

    def print_info(self):
        print('{0} : {1}'.format(self.name, self.email))

if __name__ == '__main__' :
    sojeong = ContactInfo('sojeong', '2sjeong918@gmail.com')
    lee = ContactInfo('Lee', 'lee@naver.com')

    sojeong.print_info()
    lee.print_info()