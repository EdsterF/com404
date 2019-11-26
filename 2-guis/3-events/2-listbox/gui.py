from tkinter import *

class Gui(Tk):
    def __init__(self):
        super().__init__()

        #set window attributes
        self.title("Song Maker")
        
        #add components
        #0 row
        self.__add_heading_label()
        #1 row
        self.__add_instruction_label()
        #2row
        self.__add_lyric_frame1()
        self.__add_lyric_entry1()
        self.__add_song_button()
        #3row
        self.__add_instruction_label2()
        #4row
        self.__add_lyric_frame2()
        self.__add_lyric_listbox()

    def __add_heading_label(self):
        #CREATE
        self.heading_label = Label()
        self.heading_label.grid(row=0, 
                                column=0, 
                                columnspan=2)

        #STYLE
        self.heading_label.configure(text="Song Maker",
                                     font="Arial 20")

        #EVENTS
        pass

    def __add_instruction_label(self):
        #CREATE
        self.instruction_label = Label()
        self.instruction_label.grid(row=1,
                                    column=0,
                                    sticky=W)
        
        #STYLE
        self.instruction_label.configure(text="Lyric to Add:",
                                         font="Arial 12",
                                         padx=0,
                                         pady=10)
        
        #EVENTS
        pass

    def __add_lyric_frame1(self):
        #CREATE
        self.lyric_frame = Frame()
        self.lyric_frame.grid(row=2,
                              column=0)
        
        #STYLE
        pass

        #EVENTS
        pass

    def __add_lyric_entry1(self):
        #CREATE
        self.lyric_entry = Entry (self.lyric_frame)
        self.lyric_entry.pack(side=LEFT)

        #STYLE
        pass

        #EVENT
        pass

    def __add_song_button(self):
        #CREATE
        self.song_button = Button (self.lyric_frame)
        self.song_button.pack(side=RIGHT)

        #STYLE
        self.song_button.configure(text="Add")

        #EVENT
        self.song_button.bind("<ButtonRelease-1>", self.__song_button_clicked)

    def __add_instruction_label2 (self):
        #CREATE
        self.instruction_label2 = Label ()
        self.instruction_label2.grid (row=3,
                                      column=0,
                                      sticky=W)
        
        #STYLE
        self.instruction_label2.configure (font="Arial 12",
                                           text="Lyrics:")
        
        #EVENT
        pass

    def __add_lyric_frame2 (self):
        #CREATE
        self.lyric_frame2 = Frame()
        self.lyric_frame2.grid(row=4,
                              column=0,
                              padx=5,
                              pady=5)
        
        #STYLE
        pass

        #EVENTS
        pass

    def __add_lyric_listbox(self):
        #CREATE
        self.lyric_listbox = Listbox (self.lyric_frame2)
        self.lyric_listbox.grid(columnspan=2)                             

        #STYLE
        
        self.lyric_listbox.configure(width=30)
        
        #EVENTS
        pass

    def __song_button_clicked (self, event):
        self.lyric_listbox.insert(END, self.lyric_entry.get())