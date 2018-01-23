from tkinter import *

class MyFrame(Frame):
    def __init__(self, master):
        Frame.__init__(self, master)
        self.pack(fill=BOTH, expand=True)

        self.imgOn = PhotoImage(file='light_on.png')
        self.imgOff = PhotoImage(file='light_off.png')
        self.lbl = Label(self, image = self.imgOn)
        self.lbl.pack()

        self.status = Label(self, text='전등이 켜졌습니다')
        self.status.place(x=0, y=100)
        self.status.pack()

        self.buttonControl = Button(self, text='off',
                               command=lambda :self.on_click())
        self.buttonControl.pack()
        self.light_status = True

    def on_click(self):
        self.light_status = not self.light_status
        if self.light_status:
            self.lbl.config(image = self.imgOn)
            self.status.config(text= '전등이 켜졌습니다')
            self.buttonControl.config(text ='off')
        else :
            self.lbl.config(image = self.imgOff)
            self.status.config(text= '전등이 꺼졌습니다')
            self.buttonControl.config(text='on')

def main():
    root = Tk()
    root.title('이미지 보기')
    root.geometry('500x400+10+10')
    myframe = MyFrame(root)
    root.mainloop()

if __name__ == '__main__':
    main()