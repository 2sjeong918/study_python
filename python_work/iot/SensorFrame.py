#! /usr/bin/python3

import sys

# print(sys.argv)
# 첫번째 값은 실행시킨 파일명

from tkinter import *
from sensor.temperature import TemperatureSensor

class SensorFrame(Frame):
    def __init__(self, master, category = '', location='', value=0):
        Frame.__init__(self, master)

        self.master = master
        self.master.title('센서 : '+ category)
        self.pack(fill=BOTH, expand=True)

        self.text = category + ' \n ' + location

        self.scale = Scale(self, from_=0, to=100, orient=VERTICAL)
        self.scale.pack(ipadx=10, ipady=0, side=LEFT)

        self.lblValue = Label(self, text=self.text)
        self.lblValue.pack(side=LEFT, fill=X, padx=10, expand=True)

        self.sensor = TemperatureSensor(value,
                                        on_change=lambda v:self.on_change(v))
        self.sensor.start()
        self.set_value(self.sensor.measure())

    def set_value(self, value):
        self.lblValue.config(text= self.text +" : " + str(value))
        self.scale.set(50-value)

    def on_change(self, value):
        self.set_value(value)

def main():
    value = 10
    category = 'temperature'
    location = 'livingroom'
    if len(sys.argv) > 3 :
        category =  sys.argv[1]
        location =  sys.argv[2]
        value =  int(sys.argv[3])

    root = Tk()
    root.geometry("200x100+100+100")
    SensorFrame(root, category, location, value)
    root.mainloop()

if __name__ == '__main__':
    main()