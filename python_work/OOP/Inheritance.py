class Base:
    def base_method(self):
        print('base_method')

class Derived(Base):
    pass

derived = Derived()
derived.base_method()

# super()
class A:
    def __init__(self):
        print('A.__init()__')
        self.message = 'HELLO'
        self.__p = 'Private'
    def get_p(self):
        print(self.__p)
        return self.__p

class B(A):
    def __init__(self):
        print('B.__init__()')
        self.msg = 'hello'
        self.message = 'hello'
        super().__init__() # 이때 self 는 b이다.(속성을 상속받고 싶은 경우 사용)
        print("self.message is " + self.message)
        # print("self.message is " + self.__p)

    # def print(self):
    #     print(b.get_p())

    def get_p(self):
        super().get_p()
        print('get_b')

if __name__ == "__main__":
    b = B()
    # print(b.print)
    print(b.get_p())