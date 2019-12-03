from tkinter import *
import time

# the class
class AnimatedGui(Tk):
    def __init__(self):
        super().__init__()
        
        # load resources
        self.cat_image = PhotoImage(file="U:\\com404\\2-guis\\5-animation\\2-multiple-components\\cat.gif")
        self.mouse_image = PhotoImage(file="U:\\com404\\2-guis\\5-animation\\2-multiple-components\\mouse.gif")
        
        # set window attributes
        self.configure(height=500,
                       width=500)

        # set animation attributes
        self.cat_x_pos = 250
        self.cat_y_pos = 30
        self.cat_x_change = 10
        self.cat_y_change = 10

        self.mouse_x_pos = 30
        self.mouse_y_pos = 250
        self.mouse_x_change = 10
        self.mouse_y_change = 10
        
        # add components
        self.add_cat_image_label()
        self.add_mouse_image_label()
        
        # start the timer
        self.tick()
        
    # the timer tick function    
    def tick(self):
        self.cat_x_pos = self.cat_x_pos + self.cat_x_change
        self.cat_y_pos = self.cat_y_pos + self.cat_y_change
        self.cat_image_label.place(x=self.cat_x_pos,
                                    y=self.cat_y_pos)
        if self.cat_x_pos >= 450:
            self.cat_x_change *= -1
        if self.cat_y_pos >= 450:
            self.cat_y_change *= -1
        if self.cat_x_pos <= 5:
            self.cat_x_change *= -1
        if self.cat_y_pos <= 5:
            self.cat_y_change *= -1
            
        self.mouse_x_pos = self.mouse_x_pos + self.mouse_x_change
        self.mouse_y_pos = self.mouse_y_pos + self.mouse_y_change
        self.mouse_image_label.place(x=self.mouse_x_pos,
                                      y=self.mouse_y_pos)
        if self.mouse_x_pos >= 450:
            self.mouse_x_change *= -1
        if self.mouse_y_pos >= 450:
            self.mouse_y_change *= -1
        if self.mouse_x_pos <= 5:
            self.mouse_x_change *= -1
        if self.mouse_y_pos <= 5:
            self.mouse_y_change *= -1
        self.after(100, self.tick)

    # the images
    def add_cat_image_label(self):
        self.cat_image_label = Label()
        self.cat_image_label.place(x=self.cat_x_pos,
                                    y=self.cat_y_pos)
        self.cat_image_label.configure(image=self.cat_image)

    def add_mouse_image_label(self):
        self.mouse_image_label = Label()
        self.mouse_image_label.place(x=self.mouse_x_pos,
                                      y=self.mouse_y_pos)
        self.mouse_image_label.configure(image=self.mouse_image)
     
# the object
if __name__ == "__main__":
    gui = AnimatedGui()    
    gui.mainloop() 