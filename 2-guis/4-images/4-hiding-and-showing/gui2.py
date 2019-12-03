from tkinter import *
from tkinter import messagebox

class Gui(Tk):
    def __init__(self):
        super().__init__()

        self.tickbox_image = PhotoImage(file="C:\\Users\\eduardo franco\\Documents\\Python\\VisualStudioGIT\\com404\\2-guis\\3-events\\4-images\\4-hiding-and-showing\\tick.gif")
        self.crossbox_image = PhotoImage(file="C:\\Users\\eduardo franco\\Documents\\Python\\VisualStudioGIT\\com404\\2-guis\\3-events\\4-images\\4-hiding-and-showing\\cross.gif")

        self.title("Hotel Check In")
        self.configure()

        

        self.__add_heading_label()

        self.__add_name_label()
        self.__add_name_entry()
        self.__add_name_checkbox_label()

        self.__add_passport_label()
        self.__add_passport_entry()
        self.__add_passport_checkbox_label()

        self.__add_nights_label()
        self.__add_nights_entry()
        self.__add_nights_checkbox_label()

        self.__add_check_in_button()



    def __add_heading_label(self):
        self.heading_label = Label()
        self.heading_label.grid(row=0, column=0)

        self.heading_label.configure(font="Arial 20", text="Hotel Check In")

        #---------

    def __add_name_label(self):
        self.name_label = Label()
        self.name_label.grid(row=1, column=0)

        self.name_label.configure(font="Arial 12", text="Name:")

    def __add_name_entry(self):
        self.name_entry = Entry()
        self.name_entry.grid(row=1, column=1)

        self.name_entry.bind("<FocusOut>", self.__name_checkbox_leave)

    def __add_name_checkbox_label(self):
        self.name_checkbox_label = Label()
        self.name_checkbox_label.grid(row=1, column=2)
        self.name_checkbox_label.configure(image=self.crossbox_image)

    def __name_checkbox_leave(self, event):
        if (self.name_entry.get() == ""):
            self.name_checkbox_label.configure(image=self.crossbox_image)

        else:
            self.name_checkbox_label.configure(image=self.tickbox_image)


        #-----------


    def __add_passport_label(self):
        self.passport_label = Label()
        self.passport_label.grid(row=2, column=0)

        self.passport_label.configure(font="Arial 12", text="Passport No.")

    def __add_passport_entry(self):
        self.passport_entry = Entry()
        self.passport_entry.grid(row=2, column=1)

        self.passport_entry.bind("<FocusOut>", self.__passport_checkbox_leave)

    def __add_passport_checkbox_label(self):
        self.passport_checkbox_label = Label()
        self.passport_checkbox_label.grid(row=2, column=2)
        self.passport_checkbox_label.configure(image=self.crossbox_image)


    def __passport_checkbox_leave(self, event):
        if (self.passport_entry.get() == ""):
            self.passport_checkbox_label.configure(image=self.crossbox_image)
        else:
            self.passport_checkbox_label.configure(image=self.tickbox_image)


        #----------------


    def __add_nights_label(self):
        self.nights_label = Label()
        self.nights_label.grid(row=3, column=0)

        self.nights_label.configure(font="Arial 12", text="No. Of Nights")

    def __add_nights_entry(self):
        self.nights_entry = Entry()
        self.nights_entry.grid(row=3, column=1)

        self.nights_entry.bind("<FocusOut>", self.__nights_checkbox_leave)

    def __add_nights_checkbox_label(self):
        self.nights_checkbox_label = Label()
        self.nights_checkbox_label.grid(row=3, column=2)
        self.nights_checkbox_label.configure(image=self.crossbox_image)

    def __nights_checkbox_leave(self, event):
        if (self.nights_entry.get() == ""):
            self.nights_checkbox_label.configure(image=self.crossbox_image)
        else:
            self.nights_checkbox_label.configure(image=self.tickbox_image)

    def __add_check_in_button(self):
        self.check_in_button = Button()
        self.check_in_button.grid(row=4, column=0, columnspan=2)
        
        self.check_in_button.configure(text="Check In")

        self.check_in_button.bind("<ButtonRelease-1>", self.__check_in_button_clicked)

    def __check_in_button_clicked(self, event):

        if (int(self.nights_entry.get()) <= 0 or int(self.nights_entry.get()) >= 365):
                messagebox.showinfo("ERROR", "You must enter a value between 1-365")


if (__name__ == "__main__"):
    gui = Gui()
    gui.mainloop()