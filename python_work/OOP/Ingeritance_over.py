class A:
    def method(self):
        print("A")

class B(A):
    def method(self):
        print("B")

class C(A):
    def method(self):
        print("C")

def my_print(obj):
    obj.method()

a = A(); b = B(); c = C()

my_print(a)
my_print(b)
my_print(c)