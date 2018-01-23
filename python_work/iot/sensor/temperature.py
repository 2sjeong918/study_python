#! /usr/bin/python3

import time

def temperature(value, displacement=None):
    if not displacement:
        displacement = (0, 1, 1, 2, -1, -1, -2, 0, -1, -1, -2, 2, 2, 0)
    current = 0;

    while True:
        value += displacement[current]
        current = (current+1)%len(displacement)
        yield value
#     yield는 제너레이터 함수로 만들어줌 / 다시 실행하면 이곳에서 실행 시작

# if __name__ == '__main__':
    # for value in temperature(5):
    #     print(value)
    #     time.sleep(1)
    # print(temperature)
    # t = temperature(5)
    # print(t.__next__())
    # print(t)


#
from threading import Thread

class TemperatureSensor(Thread):
    def __init__(self, value=0, displacement=None, interval=1, on_change=None):
        Thread.__init__(self)

        self.sensor = temperature(value, displacement)
        self.value = value
        self.interval = interval
        self.on_change = on_change

    def measure(self):
        return self.value

    def run(self):
        # while True :
        #     time.sleep(self.interval)
        #     value = self.sensor.__next__()
        #     if self.on_change:
        #         self.on_change(value)
        try:
            for value in self.sensor :
                time.sleep(self.interval)
                if self.on_change:
                    self.on_change(value)
        except Exception as err:
            print('에러 : %s'%err)
            print('센서 스레드가 종료합니다.')

if __name__ == '__main__':
    ts = TemperatureSensor(on_change=lambda v:print(v))
    ts.start()
    print('센서 가동')