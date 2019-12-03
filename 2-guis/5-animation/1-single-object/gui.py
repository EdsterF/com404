from tkinter import *
import time

# the class
class AnimatedGui(Tk):
    def __init__(self):
        super().__init__()
        
        # load resources
        self.umbrella_image = PhotoImage(file="U:\\com404\\2-guis\\5-animation\\1-single-object\\umbrella.gif")
        
        # set window attributes
        self.configure(height=500,
                       width=500)

        # set animation attributes
        self.umbrella_x_pos = 250
        self.umbrella_y_pos = 30
        self.umbrella_x_change = 15
        self.umbrella_y_change = 15
        
        # add components
        self.add_umbrella_image_label() 
        
        # start the timer
        self.tick()
        
    # the timer tick function    
    def tick(self):
        self.umbrella_x_pos = self.umbrella_x_pos + self.umbrella_x_change
        self.umbrella_y_pos = self.umbrella_y_pos + self.umbrella_y_change
        self.umbrella_image_label.place(x=self.umbrella_x_pos,
                                    y=self.umbrella_y_pos)
        if self.umbrella_x_pos >= 440:
            self.umbrella_x_change *= -1
        if self.umbrella_y_pos >= 440:
            self.umbrella_y_change *= -1
        if self.umbrella_x_pos <= 5:
            self.umbrella_x_change *= -1
        if self.umbrella_y_pos <= 5:
            self.umbrella_y_change *= -1
        self.after(100, self.tick)

    # the ball image
    def add_umbrella_image_label(self):
        self.umbrella_image_label = Label()
        self.umbrella_image_label.place(x=self.umbrella_x_pos,
                                    y=self.umbrella_y_pos)
        self.umbrella_image_label.configure(image=self.umbrella_image)
     
# the object
if __name__ == "__main__":
    gui = AnimatedGui()    
    gui.mainloop() 