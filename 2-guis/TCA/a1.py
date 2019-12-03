from tkinter import *

class Gui(Tk):

    def __init__(self):
        super().__init__()

        # set window properties
        self.geometry("460x280")
        self.title("Currency Converter")
        

        # add components
        self.__add_outer_frame()
        self.__add_heading_label()
        self.__add_instruction_label()
        self.__add_amount_entry()
        self.__add_clear_button()
        self.__add_convert_button()
        self.__add_sys_message_entry()

    def __add_outer_frame(self):
        self.outer_frame = Frame()
        self.outer_frame.grid(row=0, column=0)
        self.outer_frame.configure( #bg="#ffe8e8",
                                    bg="white") 
                                    #padx=10, 
                                    #pady=10)
    
    def __add_heading_label(self):
        #CREATE
        self.heading_label = Label(self.outer_frame)
        self.heading_label.grid(row=1,
                                column=0,
                                columnspan=2)
        

        #STYLE
        self.heading_label.configure (font="Arial 16",
                                      text="Currency Converter",
                                      bg="white",
                                      fg="black")

        #EVENTS

    def __add_instruction_label(self):
        #CREATE
        self.instruction_label = Label(self.outer_frame)
        self.instruction_label.grid(row=2,
                                    column=0,
                                    sticky=W)

        #STYLE
        self.instruction_label.configure (font="Arial 8",
                                          text="Amount",
                                          bg="white",
                                          fg="black",
                                          pady=5)

        #EVENTS

    
    def __add_amount_entry(self):
        #CREATE
        self.amount_entry = Entry (self.outer_frame)
        self.amount_entry.grid(row=3,
                               column=0,
                               columnspan=2,
                               sticky=EW)

        #STYLE
        self.amount_entry.configure (bg="white",
                                     font="Arial 10")

        #EVENTS

    def __add_clear_button(self):
        #CREATE
        self.clear_button = Button (self.outer_frame)
        self.clear_button.grid(row=4,
                               column=1,
                               pady=5,
                               sticky=W)

        #STYLE
        self.clear_button.configure (bg="white",
                                     text="Clear",
                                     font="Arial 10",
                                     padx=10)

        #EVENTS
    

    def __add_convert_button(self):
        #CREATE
        self.convert_button = Button (self.outer_frame)
        self.convert_button.grid(row=4,
                                 column=2,
                                 pady=5,
                                 padx=10)

        #STYLE
        self.convert_button.configure (bg="white",
                                       text="Convert",
                                       font="Arial 10")

        #EVENTS


    def __add_sys_message_entry(self):
        #CREATE
        self.sys_message_entry = Entry (self.outer_frame)
        self.sys_message_entry.grid(row=5,
                                    column=0,
                                    columnspan=2)


        #STYLE
        self.sys_message_entry.configure(bg="white",
                                         font="Arial 10",
                                         text="System Message Displayed Here")



        #EVENTS

        
# the object
if __name__ == "__main__":
    gui = Gui()    
    gui.mainloop()