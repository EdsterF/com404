from tkinter import *

#window backgroud color that can be referenced by all functions in the class
background_color = "grey"

class Gui(Tk):
    #constructor
    def __init__(self):
        super().__init__()#super is a call to the parent

        #set window attributes

        self.geometry("360x180") #sets the window size of the gui
        self.title("Newsletter") #sets window title name
        
        #add window components
        self.__add_outer_frame()
        self.__add_top_frame()
        self.__add_heading_label()
        self.__add_message_label()
        self.__add_email_frame()
        self.__add_email_label()
        self.__add_user_email()
        self.__add_bottom_frame()
        self.__add_user_button()
        

        # style
        border_color = "light grey"
        self.configure(bg=background_color, 
                       bd=0,) #window backgroud color
        
        #events
        pass #pass allows for the code to be skipped when executed, it can
        #useful when there is unfinished code
    def __add_outer_frame(self):
        self.outer_frame = Frame()
        self.outer_frame.pack()
        self.outer_frame.configure (bg= "light grey",
                                    bd=10)

    def __add_top_frame(self):
        self.top_frame = Frame(self.outer_frame)
        self.top_frame.pack()
        self.top_frame.configure (bg="grey")

    def __add_heading_label(self):
        # CREATE
        self.heading_label = Label(self.top_frame)
        self.heading_label.pack(side=TOP, fill=BOTH)

        # STYLE
        self.heading_label.configure (font="Arial 16", #configure allows to configure multiple attributes in one go
                                      text= "RECEIVE OUR NEWSLETTER",
                                      bg= "light grey",
                                      pady=10) #pady moves the message down on the y axis
        # EVENTS
        pass

    def __add_message_label(self):
        # create
        self.message_label = Label (self.top_frame)
        self.message_label.pack (side=BOTTOM, fill=BOTH)
        
        # style
        self.message_label.configure (font="Arial 10",
                                      text="Please enter your email below to receive our newsletter.",
                                      bg= "light grey",
                                      pady=10)

        # events
        pass
    
    def __add_email_frame(self):
        self.email_frame = Frame()
        self.email_frame.pack()
        self.email_frame.configure(bg= "light grey")

    def __add_email_label(self):
        #create
        self.email_label = Label (self.email_frame)
        self.email_label.pack (side=LEFT, fill=BOTH)

        #style
        self.email_label.configure (font="Arial 10",
                                    text="Email:",
                                    bg= "light grey")

        #events
        pass

    def __add_user_email(self):
        #crete
        self.user_email = Entry (self.email_frame)
        self.user_email.pack (side=RIGHT, fill=BOTH)
        
        #style
        self.user_email.configure (font="Arial 10",
                                   width= "28",
                                   relief=SUNKEN)

        #events
        pass
    
    def __add_bottom_frame(self):
        self.bottom_frame = Frame()
        self.bottom_frame.pack()

    def __add_user_button(self):
        #create
        self.user_button = Button (self.bottom_frame)
        self.user_button.pack (side=TOP)

        #style
        self.user_button.configure (font="Arial 12",
                                    text="Subscribe",
                                    background="antique white",
                                    width= 38,
                                    relief=RAISED)       