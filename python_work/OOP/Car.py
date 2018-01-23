class Car :
    def __init__(self, color=0xFFFF, wheel_size= 16, displacement=2000):
        self.color = color
        self.wheel_size = wheel_size  # 바퀴의 크기
        self.displacement = displacement # 엔진 배기량
    def change_color(self, new_color):
        self.color = new_color
    def forward(self):  # 전진
        pass
    def backward(self): # 후진
        pass
    def turn_left(self): # 좌회전
        pass
    def turn_right(self): # 우회전
        pass
    def print(self):
        print('0x{:02X}'.format(self.color))
        print(self.wheel_size)
        print(self.displacement)


if __name__=='__main__' :
    my_car = Car(0xFFFFFF, 20, 3000)

    my_car.print()
    my_car.forward()
    my_car.backward()
    my_car.turn_left()
    my_car.turn_right()

if __name__=='__main__' :
    your_car = Car()

    print('0x{:02X}'.format(your_car.color))
    print(your_car.wheel_size)
    print(your_car.displacement)

    your_car.forward()
    your_car.backward()
    your_car.turn_left()
    your_car.turn_right()