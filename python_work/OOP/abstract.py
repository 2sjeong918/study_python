from abc import ABCMeta
from abc import abstractmethod

class Sender(metaclass=ABCMeta):
    def __init__(self, to =''):
        self.to =to

    @abstractmethod
    def send(self, msg):
        pass

    def set_to(self, to):
        self.to = to

    def sent_to(self, to, msg):
        self.to = to
        self.send(msg)


class Fax(Sender) :
    def __init__(self, to = ''):
        super().__init__(to)

    def send(self, msg):
        print('=================================')
        print('수신:', self.to)
        print('---------------------------------')
        print('fax 내용 : ')
        print(msg)
        print('=================================')

class SMS(Sender) :
    def __init__(self, to = ''):
        super().__init__(to)

    def send(self, msg):
        print('=================================')
        print('수신:', self.to)
        print('-----------------------------------------')
        print('sms 내용 : ')
        print(msg)
        print('=================================')

class Email(Sender) :
    def __init__(self, to = ''):
        super().__init__(to)

    def send(self, msg):
        print('=================================')
        print('수신:', self.to)
        print('-----------------------------------------')
        print('email 내용 : ')
        print(msg)
        print('=================================')

def send(s):
    msg = input('내용 : ')
    s.send(msg)
    print('전송했습니다.')

if __name__ == '__main__':
    to = input('수신자 : ')
    fax = Fax(to)
    send(fax)

    email = Email()
    email.sent_to('lsj918@naver.com', 'hello')
