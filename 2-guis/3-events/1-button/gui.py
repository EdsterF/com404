from tkinter import *

class Gui(Tk):

    def __init__(self):
        super().__init__()

        #set window attributes
        self.title("Tickets")

        #add components
        self.__add_heading_label()
        self.__add_instruction_label()
        self.__add_tickets_entry()
        self.__add_buy_button()
    
    def __add_heading_label(self):
        # CREATE
        self.heading_label = Label(self)
        self.heading_label.grid(row=0, column=0)  #sticky="ew") #sticky="ew" extends the label horizontally (this resolved
                                                              #the issue where the background was only covering the text 
                                                              #and not either side when using the grid)

        # STYLE
        self.heading_label.configure (font="Arial 16", #configure allows to configure multiple attributes in one go
                                      text= "Entrance Ticket",
                                      bg= "white",#bg=background
                                      fg="black",#fg=foreground
                                      pady=10) #pady moves the message down on the y axis
        # EVENTS
        
    
    def __add_instruction_label(self):

        #CREATE
        self.instruction_label = Label(self)
        self.instruction_label.grid(row=1, column=0, sticky=W)

        #STYLE
        self.instruction_label.configure (font="Arial 12",
                                          text="How many tickets are needed?",
                                          bg="white",
                                          fg="black")
    def __add_tickets_entry(self):
        #crete
        self.tickets_entry = Entry (self)
        self.tickets_entry.grid(row=2, column=0)
        
        #style
        self.tickets_entry.configure (bg="white",
                                      font="Arial 12") 

    def __add_buy_button(self):
        #crete
        self.buy_button = Button (self)
        self.buy_button.grid(row=3, column=0)
        
        #style
        self.buy_button.configure (bg="white",
                                   text="Buy",
                                   font="Arial 12",
                                   ipadx=10)