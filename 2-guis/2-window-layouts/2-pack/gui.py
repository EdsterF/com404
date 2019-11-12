from tkinter import *

class Gui(Tk):
    def __init__(self):
        super().__init__()

        #set window attributes

        self.geometry("350x190") #sets the window size of the gui
        self.title("Newsletter") #sets window title name
        
        #add window components
        self.__add_frame()
        self.__add_heading_label()
        self.__add_message_label()
        self.__add_email_label()
        self.__add_user_email()
        self.__add_user_button()
        

    def __add_frame(self):
        #create
        self.add_frame = Frame ()
        self.add_frame.pack (fill=BOTH)

        #style
        self.add_frame.configure (background="blue")

    def __add_heading_label(self):
        # CREATE
        self.heading_label = Label(self.add_frame) #Label is a class in the tkinter library
        self.heading_label.pack()

        # STYLE
        self.heading_label.configure (font="Arial 16", #configure allows to configure multiple attributes in one go
                                      text= "RECEIVE OUR NEWSLETTER") 
        # EVENTS

    def __add_message_label(self):
        # create
        self.message_label = Label (self.add_frame)
        self.message_label.pack()
        
        # style
        self.message_label.configure (font="Arial 10",
                                      text="Please enter your email below to receive our newsletter.")

        # events
    
    def __add_email_label(self):
        #create
        self.email_label = Label (self.add_frame)
        self.email_label.pack (side=LEFT)

        #style
        self.email_label.configure (font="Arial 10",
                                      text="Email")

        #events

    def __add_user_email(self):
        #crete
        self.user_email = Entry (self.add_frame)
        self.user_email.pack ()
        
        #style
        #self.user_email.configure (geometry="10x50")
    
    def __add_user_button(self):
        #create
        self.user_button = Button (self.add_frame)
        self.user_button.pack (side=BOTTOM)

        #style
        self.user_button.configure (font="Arial 12",
                                    text="Subscribe",
                                    background="Pink")