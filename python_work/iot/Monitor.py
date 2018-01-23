#! /usr/bin/python3
from tkinter import *
from tkinter.ttk import *
from actor.light import Light
import paho.mqtt.client as mqtt

class MainFrame(Frame):
    def __init__(self, master, category='', location='', value=0):
        Frame.__init__(self, master)  # master는 부모 윈도우

        self.master = master
        self.master.title('Iot 모니터')
        self.pack(fill=BOTH, expand=True)  # 부모 윈도우 크기에 맞게 크기 조정

        Grid.columnconfigure(self, 1, weight=1)
        Grid.columnconfigure(self, 3, weight=1)

        # 온도 센서
        self.temperature1 = Scale(self, from_=0, to=100, orient=VERTICAL)
        self.temperature1.set(50)
        self.temperature2 = Scale(self, from_=0, to=100, orient=VERTICAL)
        self.temperature2.set(50)

        # 조명
        self.light1 = Light(self)
        self.light2 = Light(self)

        # 상태 출력
        self.lblTemp1 = Label(self, text=str(value))
        self.set_info(self.lblTemp1)
        self.lblTemp2 = Label(self, text=str(value))
        self.set_info(self.lblTemp2)
        self.lblLight1 = Label(self, text=str(value))
        self.set_info(self.lblLight1)
        self.lblLight2 = Label(self, text=str(value))
        self.set_info(self.lblLight2)

        # 배치
        self.temperature1.grid(row=0,column=0)
        self.lblTemp1.grid(row=0,column=1)
        self.temperature2.grid(row=0, column=2)
        self.lblTemp2.grid(row=0, column=3)

        self.light1.grid(row=1, column=0)
        self.lblLight1.grid(row=1, column=1)
        self.light2.grid(row=1, column=2)
        self.lblLight2.grid(row=1, column=3)

    def set_info(self, lbl, str = '종류 : \n위치 : \n상태 : \n측정시간 :'):
        lbl.config(text = str)




def main():
    root = Tk()								# 메인 윈도우
    root.geometry("500x250+100+100")	# 가로x세로+X위치+Y위치
    app = MainFrame(root)
    root.mainloop()

if __name__ == '__main__':
    main()

