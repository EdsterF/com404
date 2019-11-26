from tkinter import *

class Gui(Tk):

    def __init__(self):
        super().__init__()
        
        # load resources
        self.cactus_image = PhotoImage(file="U:\\com404\\2-guis\\3-events\\4-images\\2-swapping\\cactus.gif")
        self.cactus_with_name_image = PhotoImage(file="U:\\com404\\2-guis\\3-events\\4-images\\2-swapping\\cactus_with_name.gif")
        
        # set window attributes
        self.title("Gui")
        
        # add components
        self.__add_heading_label()
        self.__add_cactus_image_label()
        self.__add_flip_button()
       
    
    def __add_heading_label(self):
        self.heading_label = Label()
        self.heading_label.grid (row=0, column=0, sticky=EW)
        self.heading_label.configure (text="Cactus Leaves",
                                      font="Arial 20")
        
    def __add_cactus_image_label(self):
        self.cactus_image_label = Label()
        self.cactus_image_label.grid(row=1, column=0)
        self.cactus_image_label.configure(image=self.cactus_image,
                                             height=200,
                                             width=200)

    def __add_flip_button(self):
        self.flip_button = Button()
        self.flip_button.grid(row=2, column=0)
        self.flip_button.configure(text="Flip",
                                   font="Arial 16")
        #events
        self.flip_button.bind("<ButtonRelease-1>", self.__left_flip_button_clicked)
        self.flip_button.bind("<ButtonRelease-3>", self.__right_flip_button_clicked)
 
    def __left_flip_button_clicked(self, event):
        print("Hello")
        self.cactus_image_label.configure(image=self.cactus_with_name_image)
    
    def __right_flip_button_clicked(self, event):
        self.cactus_image_label.configure(image=self.cactus_image)
    

# Create an object of the Gui class when this module is executed
if (__name__ == "__main__"):
    gui = Gui()
    gui.mainloop()