from tkinter import filedialog
from tkinter import *
from tkinter.ttk import *
from random import shuffle
import glob
from pygame import mixer
import tinytag
import time

_BASE_DIR = 'C:/Temp/mp3'

class MP3Frame(Frame) :
    def __init__(self, master, base_dir = _BASE_DIR):
        Frame.__init__(self, master)

        self.base_dir = base_dir
        self.master = master
        self.master.title("MP3Player")
        self.pack(fill=BOTH, expand=True)
        self.make_info_frame()

        self.listbox = Listbox(self, height=5)
        self.listbox.pack(fill=BOTH, expand=True)
        self.listbox.bind('<Double-Button-1>',
                          lambda event:self.on_select(event))


        self.progress = Scale(self, from_=0, to=100, orient=HORIZONTAL,
                              command=lambda value: self)
        # self.scale = Scale(self, from_=0, to=100, orient=HORIZONTAL)
        # self.scale.pack(fill=X, padx=10, pady=10)

        self.make_button_frame()

        self.load_list()

        self.current = 0
        self.position = 0
        self.status = False

        mixer.init()

    def load_list(self):
        self.lblBaseDir.config(text=self.base_dir)
        file_list = glob.glob1(self.base_dir, '*.mp3')

        self.listbox.delete(0, END)
        for file in file_list:
            self.listbox.insert(END, file)

        self.current = 0
        self.listbox.select_set(self.current)
        title = self.listbox.get(self.current)

    def make_info_frame(self):
        frameInfo = Frame(self)
        frameInfo.pack(fill=X)

        Label(frameInfo, text="현재폴더: ").pack(side=LEFT, padx=5, pady=5)
        self.lblBaseDir = Label(frameInfo, text=self.base_dir)
        self.lblBaseDir.pack(side= LEFT, padx=5, pady=5, fill=X)

        frameInfo = Frame(self)
        frameInfo.pack(fill=X)

        Label(frameInfo, text = "현재곡 : ").pack(side=LEFT, padx = 5, pady=5)
        self.lblSongTitle = Label(frameInfo, text="--------")
        self.lblSongTitle.pack(side=LEFT, padx=5, pady=5, fill=X)

    def on_select(self, event):
        current = self.listbox.curselection()
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
        self.folder_img = PhotoImage(file='folder.png')

        self.btnSelect = Button(self.frameButtons, image=self.folder_img,
                                command = lambda : self.on_change_dir())
        self.btnSelect.pack(side=LEFT, padx=5, pady=5, fill=X, expand=True)
        self.btnPrev = Button(self.frameButtons, image=self.prev_img,
                              command=lambda  : self.on_prev())
        self.btnPrev.pack(side=LEFT, padx=5, pady=5, fill=X, expand=True)
        self.btnPlay = Button(self.frameButtons, image=self.play_img,
                              command=lambda: self.on_play())
        self.btnPlay.pack(side=LEFT, padx=5, pady=5, fill=X, expand=True)
        self.btnNext = Button(self.frameButtons, image=self.next_img,
                              command=lambda: self.on_next())
        self.btnNext.pack(side=LEFT, padx=5, pady=5, fill=X, expand=True)
        self.btnShuffle = Button(self.frameButtons, image=self.shuffle_img,
                              command=lambda: self.on_shuffle())
        self.btnShuffle.pack(side=LEFT, padx=5, pady=5, fill=X, expand=True)

    def play(self):
        self.position = 0
        mp3 = self.base_dir + '/' + self.listbox.get(self.current)
        mixer.music.load(mp3)
        mixer.music.play()

        tag = tinytag.TinyTag.get(mp3)
        print(tag.artist)
        print(tag.duration)

        self.status = True
        self.btnPlay.config(image=self.pause_img)

        title = self.listbox.get(self.current)
        self.lblSongTitle.config(text=title)

    def update_progress(self):
        while True:
            if self.status:
                self.position = mixer.music.get_pos()
                self.progress.set(self.position)
            time.sleep(0.1)

    def on_position(self, event):
        pos = self.progress.get()



    def on_change_dir(self):
        # 디렉토리 선택 대화상자 띄우기
        dir = filedialog.askdirectory()
        if dir:
            self.base_dir = dir
        self.load_list()

    def on_prev(self):
        self.listbox.select_clear(self.current)  # 선택 해제
        if self.current == 0:
            self.current = self.listbox.size() - 1
        else:
            self.current -= 1
        self.listbox.select_set(self.current)  # 새로운 선택 설정
        self.play()

    def on_play(self):
        if self.status :
            self.btnPlay.config(image=self.play_img)
            self.status = False
            self.position = mixer.music.get_pos()
            print(self.position)
            mixer.music.pause()

        else:
            self.btnPlay.config(image=self.pause_img)
            self.status = True
            if self.position :
                mixer.music.unpause()
            else:
                self.play()

    def on_next(self):
        self.listbox.select_clear(self.current)
        self.current = (self.current + 1) % self.listbox.size()
        self.listbox.select_set(self.current)

        self.play()

    def on_shuffle(self):
        # 목록 가져오기
        mp3_list = list(self.listbox.get(0, END))
        title = self.lblSongTitle.cget('text')
        shuffle(mp3_list)
        # 이전 목록 지우기
        self.listbox.delete(0, END)
        # 새로운 목록 넣기
        for file in mp3_list:
            self.listbox.insert(END, file)

        self.current = mp3_list.index(title)
        self.listbox.select_set(self.current)


def main():
    root = Tk() # 메인 윈도우
    root.geometry("500x300+100+100") # 가로x세로+X위치+Y위치
    MP3Frame(root)
    root.mainloop()
if __name__ == '__main__':
    main()