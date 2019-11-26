from tkinter import *

class Gui(Tk):
    def __init__(self):
        super().__init__()
        self.title("Song Maker")
        self.configure()

        self.__add_heading_label()
        self.__add_instruction_label1()
        self.__add_lyric_frame()
        self.__add_lyric_entry()
        self.__add_song_button()
        self.__add_instruction_label2()
        self.__add_lyric_listbox()


    def __add_heading_label(self):
        self.heading_label = Label()
        self.heading_label.grid(row=0, column=0)

        self.heading_label.configure(font="Arial 20", text="Song Maker")


    def __add_instruction_label1(self):
        self.instruction_label1 = Label()
        self.instruction_label1.grid(row=1, column=0, sticky=W)

        self.instruction_label1.configure(font="Arial 14", text="Lyric to Add:")

    def __add_lyric_frame(self):
        self.lyric_frame = Frame()
        self.lyric_frame.grid(row=2, column=0)
        #self.lyric_frame.configure()

    def __add_lyric_entry(self):
        self.lyric_entry = Entry(self.lyric_frame)
        self.lyric_entry.pack(side=LEFT)

    def __add_song_button(self):
        self.song_button = Button(self.lyric_frame)
        self.song_button.pack(side=RIGHT)
        

        self.song_button.configure(text="Add")

        self.song_button.bind("<ButtonRelease-1>", self.__song_button_clicked)

    def __add_instruction_label2(self):
        self.lyric_instruction_label2 = Label()
        self.lyric_instruction_label2.grid(row=3, column=0, sticky=W)

        self.lyric_instruction_label2.configure(font="Arial 14", text="Lyrics:")

    def __add_lyric_listbox(self):
        self.lyric_listbox = Listbox()
        self.lyric_listbox.grid(row=4, column=0)

    def __song_button_clicked(self, event):
        self.lyric_listbox.insert(END, self.lyric_entry.get())