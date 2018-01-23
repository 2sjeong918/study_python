import sys
from tkinter import *
from actor.light import Light
import paho.mqtt.client as mqtt
from datetime import datetime

class LightFrame(Frame):
    def __init__(self, master, category='', location='', value=0):
        Frame.__init__(self, master, bg='black')

        self.client = mqtt.Client()
        self.client.connect('localhost', 1883)
        self.client.loop(1)
        self.topic = 'C:\python-work\pycharm\iot'

        self.master = master
        self.master.title('전등 : ' + category)
        self.pack(fill=BOTH, expand=True)

        self.light = Light(self)
        self.light.pack(side=LEFT, expand=True )

        self.lightButton = Button(self, text="전등 켜기",
                                  command=lambda: self.on_light_btn_click())
        self.lightButton.pack(side=LEFT, expand=True)

    def on_light_btn_click(self):
        self.light.status = not self.light.status
        if self.light.status:
            self.turn_on()
            self.client.publish(self.topic, 'ON')
        else:
            self.turn_off()
            self.client.publish(self.topic, 'OFF')

    def turn_on(self):
        self.light.turn_on()
        self.lightButton.config(text="전등 끄기")
        self.config(bg="yellow")

    def turn_off(self):
        self.light.turn_off()
        self.lightButton.config(text="전등 켜기")
        self.config(bg="black")

    def get_status(self):
        return self.light.status

def main():
    root = Tk()
    root.geometry('300x200+100+100')
    location = 'livingroom'


    if len(sys.argv) > 1 :
        location = sys.argv[1]

    app = LightFrame(root, location)
    root.mainloop()


if __name__ == '__main__':
    main()