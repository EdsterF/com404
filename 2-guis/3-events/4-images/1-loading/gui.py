from tkinter import *

class Gui(Tk):

    def __init__(self):
        super().__init__()
        
        # load resources
        self.ambulance_image = PhotoImage(file="U:\\com404\\2-guis\\3-events\\4-images\\1-loading\\ambulance.gif")
        self.bike_image = PhotoImage(file="U:\\com404\\2-guis\\3-events\\4-images\\1-loading\\bike.gif")
        self.plane_image = PhotoImage(file="U:\\com404\\2-guis\\3-events\\4-images\\1-loading\plane.gif")
        # set window attributes
        self.title("Gui")
        
        # add components
        self.__add_heading_label()
        self.__add_ambulance_image_label()
        self.__add_bike_image_label()
        self.__add_plane_image_label()
    
    def __add_heading_label(self):
        self.heading_label = Label()
        self.heading_label.grid (row=0, column=0, columnspan=3, sticky=EW)
        self.heading_label.configure (text="TRANSPORT",
                                      font="Arial 20")
        
    def __add_ambulance_image_label(self):
        self.ambulance_image_label = Label()
        self.ambulance_image_label.grid(row=1, column=0)
        self.ambulance_image_label.configure(image=self.ambulance_image,
                                             height=60,
                                             width=60)

    def __add_bike_image_label(self):
        self.bike_image_label = Label()
        self.bike_image_label.grid(row=1, column=1)
        self.bike_image_label.configure(image=self.bike_image,
                                             height=60,
                                             width=60)
 
    def __add_plane_image_label(self):   #if get too many positional parameters error comes up, make sure the self in brackets is put
        self.plane_image_label = Label()
        self.plane_image_label.grid(row=1, column=2)
        self.plane_image_label.configure(image=self.plane_image,
                                             height=60,
                                             width=60)
 
    
# Create an object of the Gui class when this module is executed
if (__name__ == "__main__"):
    gui = Gui()
    gui.mainloop()