from tkinter import filedialog
from tkinter import *
from tkinter.ttk import *
import tkinter.messagebox as messagebox
from random import shuffle
import glob
from pygame import mixer
from tinytag import TinyTag
from threading import Thread
import time

_BASE_DIR = 'c:/temp/mp3'

class MP3Frame(Frame):  # Frame - 윈도우 관리 클래스
    def __init__(self, master, base_dir=_BASE_DIR):
        Frame.__init__(self, master)  # master는 부모 윈도우

        self.base_dir = base_dir
        self.master = master
        self.master.title("MP3Player")
        self.pack(fill=BOTH, expand=True)  # 부모 윈도우 크기에 맞게 크기 조정

        self.make_info_frame()

        self.listbox = Listbox(self, height=5)
        self.listbox.pack(fill=BOTH, expand=True)
        self.listbox.bind('<Double-Button-1>',
                          lambda event: self.on_select(event))

        self.progress = Scale(self, from_=0, to=100, orient=HORIZONTAL,
                        command=lambda value: self.on_position(value))

        self.progress.pack(fill=X)
        # self.progress.bind('<Button-1>',
        #                    lambda event: self.start_positioning())
        # self.progress.bind('<ButtonRelease-1>',
        #                    lambda event: self.set_position())
        self.positioning = False

        self.make_position_info()
        self.make_button_frame()

        self.load_list()

        self.current = 0
        self.position = 0
        self.status = False

        mixer.init()
        self.run = True
        Thread(daemon=True, target=lambda : self.update_progress()).start()

    def make_position_info(self):
        frameInfo = Frame(self)
        frameInfo.pack(fill=X)

        Label(frameInfo, text="0").pack(side=LEFT, padx=5, pady=5)
        self.lblCurrent = Label(frameInfo, anchor=CENTER, text='')
        self.lblCurrent.pack(side=LEFT, padx=5, pady=5, fill=X, expand=True)
        self.lblTo = Label(frameInfo, text='100')
        self.lblTo.pack(side=LEFT, padx=5, pady=5)


    def on_position(self, value):
        value = int(float(value) // 100) /10
        self.lblCurrent.config(text=str(value))

    def update_progress(self):
        try :
            while self.run :
                if self.status: # 재생 중일 때만   #  and not self.positioning: #
                    self.position = mixer.music.get_pos()
                    self.progress.set(self.position)
                    # print(self.position)
                time.sleep(0.1)
        except :
            pass
        print('작업스레드 종료')


    def play(self):
        self.position = 0
        mp3 = self.base_dir + '/' + self.listbox.get(self.current)
        mixer.music.load(mp3)
        mixer.music.play()

        self.tag = TinyTag.get(mp3)
        to = int(self.tag.duration*1000)
        self.progress.config(to=to)
        self.lblTo.config(text=str(to//1000))

        self.btnPlay.config(image=self.pause_img)
        self.status = True
        # 재생 정보 갱신
        title = self.listbox.get(self.current)
        self.lblSongTitle.config(text=title)


    def set_position(self):
        pos = int(self.progress.get()/1000)
        # pos = int(self.progress.get())
        print('재생 위치', pos)
        mixer.music.play(0, pos)
        self.positioning = False


    def start_positioning(self):
        self.positioning = True

    def on_select(self, event):
        current = self.listbox.curselection()  # 튜플로 리턴
        if current:
            self.current = current[0]
            self.play()

    def make_button_frame(self):
        self.frameButtons = Frame(self)
        self.frameButtons.pack(fill=X)

        self.play_img = PhotoImage(file='play.png')
        self.pause_img = PhotoImage(file='pause.png')
        self.prev_img = PhotoImage(file='previous.png')
        self.next_img = PhotoImage(file='next.png')
        self.shuffle_img = PhotoImage(file='shuffle.png')
        self.foler_img = PhotoImage(file='folder.png')


        self.btnSelect = Button(self.frameButtons, image=self.foler_img,
                                command=lambda : self.on_change_dir())
        self.btnSelect.pack(side=LEFT,  padx=5, pady=5, fill=X, expand=True)

        self.btnPrev = Button(self.frameButtons, image=self.prev_img,
                                command=lambda : self.on_prev())
        self.btnPrev.pack(side=LEFT, padx=5, pady=5, fill=X, expand=True)

        self.btnPlay = Button(self.frameButtons,image=self.play_img,
                                command=lambda : self.on_play())
        self.btnPlay.pack(side=LEFT, padx=5, pady=5, fill=X, expand=True)

        self.btnNext = Button(self.frameButtons, image=self.next_img,
                                command=lambda : self.on_next())
        self.btnNext.pack(side=LEFT, padx=5, pady=5, fill=X, expand=True)

        self.btnShuffle = Button(self.frameButtons, image=self.shuffle_img,
                                command=lambda : self.on_shuffle())
        self.btnShuffle.pack(side=LEFT, padx=5, pady=5, fill=X, expand=True)

    def make_info_frame(self):
        frameInfo = Frame(self)
        frameInfo.pack(fill=X)

        Label(frameInfo, text="현재 폴더 : ").pack(side=LEFT, padx=5, pady=5)
        self.lblBaseDir = Label(frameInfo, text=self.base_dir)
        self.lblBaseDir.pack(side=LEFT, padx=5, pady=5, fill=X)

        frameInfo = Frame(self)
        frameInfo.pack(fill=X)

        Label(frameInfo, text="현재곡 : ").pack(side=LEFT, padx=5, pady=5)

        self.lblSongTitle = Label(frameInfo, text="----")
        self.lblSongTitle.pack(side=LEFT, padx=5, pady=5, fill=X)



    def on_play(self):
        if self.status : # 재생 중이면 중지로
            self.btnPlay.config(image=self.play_img)
            self.status = False
            self.position = mixer.music.get_pos()
            mixer.music.pause()

        else : # 중지면 재생으로
            self.status = True
            self.btnPlay.config(image=self.pause_img)
            if self.position :
                mixer.music.unpause()
            else:
                self.play()


    def on_prev(self):
        self.listbox.select_clear(self.current)
        if self.current == 0:
            self.current = self.listbox.size()-1
        else:
            self.current -= 1

        self.listbox.select_set(self.current)
        self.play()

    def on_next(self):
        self.listbox.select_clear(self.current)
        self.current = (self.current+1)%self.listbox.size()
        self.listbox.select_set(self.current)

        self.play()

    def on_shuffle(self):
        mp3_list = list(self.listbox.get(0, END))
        title = self.lblSongTitle.cget("text")
        # title = self.lblSongTitle["text"]

        shuffle(mp3_list)
        self.listbox.delete(0, END)
        for file in mp3_list:
            self.listbox.insert(END, file)

        self.current = mp3_list.index(title)
        self.listbox.select_set(self.current)





    def on_change_dir(self):
        dir = filedialog.askdirectory()
        if dir :
            self.base_dir = dir
            self.load_list()

    def load_list(self):
        self.lblBaseDir.config(text=self.base_dir)
        file_list = glob.glob1(self.base_dir, '*.mp3')

        self.listbox.delete(0, END)
        for file in file_list:
            self.listbox.insert(END, file)
        self.current = 0
        self.listbox.select_set(self.current)
        title = self.listbox.get(self.current)
        self.lblSongTitle.config(text=title)


def main():
    root = Tk()  # 메인 윈도우
    root.geometry("500x250+100+100")  # 가로x세로+X위치+Y위치
    app = MP3Frame(root)
    root.mainloop()
    app.run = False

if __name__ == '__main__':
    main()
