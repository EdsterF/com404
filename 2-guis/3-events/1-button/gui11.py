from tkinter import *
from tkinter import messagebox

class Gui(Tk):
    def __init__(self):
        super().__init__()
        self.title("Tickets")
        self.configure()

        self.__add_heading_label()
        self.__add_instruction_label()
        self.__add_tickets_entry()
        self.__add_buy_button()

    def __add_heading_label(self):
        self.heading_label = Label()
        self.heading_label.grid(row=0, column=0, rowspan=4)

        self.heading_label.configure(font="Arial 20",
                                    text="Tickets")

    def __add_instruction_label(self):
        self.instruction_label = Label()
        self.instruction_label.grid(row=1, column=0, sticky=W)

        self.instruction_label.configure(font="Arial 12",
                                    text="Enter the amount of tickets you want to buy below!")

    def __add_tickets_entry(self):
        self.tickets_entry = Entry()
        self.tickets_entry.grid(row=2, column=0)



    def __add_buy_button(self):
        self.buy_button = Button(height=1, width=10)
        self.buy_button.grid(row=3, column=0, pady=20, padx=20)


        self.buy_button.configure(font="Arial 12", text="BUY!")

        self.buy_button.bind("<ButtonRelease-1>", self.__buy_button_clicked)

    def __buy_button_clicked(self, event):
        if (self.tickets_entry.get() == "1"):
            messagebox.showinfo("Purchased!", "You have purchased 1 ticket!")

        elif (int(self.tickets_entry.get()) > 1):
            messagebox.showinfo("Purchased!", "You have purchased " + self.tickets_entry.get() + " tickets!")
        
        else:
            messagebox.showinfo("Not Purchased!", "You have entered an invalid number of tickets!")