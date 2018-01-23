class MyDecorator :
    def __init__(self, f):
        print('initializing mydecorator...')
        self.func = f

    def __call__(self):
        print('begin : {0}'.format(self.func.__name__))
        self.func()
        print('end : {0}'.format(self.func.__name__))

import time
class PerformanceDecorator :
    def __init__(self, f):
        print('initializing performance...')
        self.func = f

    def __call__(self):
        start_time = time.time()
        self.func
        print(time.time() - start_time )

# print_hello = MyDecorator(print_hello)

@PerformanceDecorator
@MyDecorator
def print_hello():
    print('hello')

print_hello()