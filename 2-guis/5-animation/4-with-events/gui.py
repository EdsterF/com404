from tkinter import *
import time

# the class
class AnimatedGui(Tk):
    def __init__(self):
        super().__init__()
        
        # load resources
        self.elicopter_image = PhotoImage(file="U:\\com404\\2-guis\\5-animation\\4-with-events\\elicopter.gif")
        
        # set window attributes
        self.configure(height=500,
                       width=500)

        # set animation attributes
        self.num_ticks = 0
        
        self.elicopter_x_pos = 15 
        self.elicopter_y_pos = 250
        self.elicopter_x_change = 10
        self.elicopter_y_change = 0
        
        # add components
        self.add_elicopter_image_label()
        
        # start the timer
        self.tick()
        
    # the timer tick function    
    def tick(self):

        self.elicopter_x_pos += self.elicopter_x_change
        self.elicopter_y_pos += self.elicopter_y_change
        self.elicopter_image_label.place(x=self.elicopter_x_pos,
                                     y=self.elicopter_y_pos)
        
        self.after(100, self.tick)

    # the person images
    def add_elicopter_image_label(self):
        self.elicopter_image_label = Label()
        self.elicopter_image_label.place(x=self.elicopter_x_pos,
                                     y=self.elicopter_y_pos)
        self.elicopter_image_label.configure(image=self.elicopter_image)

    def add_up_button(self):
        self.add_up_button = Button()
        self.add_up_button.place(x=100, y=450)
        self.add_up_button.configure(text="Up")

    def add_down_button(self):
        self.add_down_button = Button()
        self.add_down_button.place(x=200, y=450)
        self.add_down_button.configure(text="Down")
  
# the object
if __name__ == "__main__":
    gui = AnimatedGui()    
    gui.mainloop()