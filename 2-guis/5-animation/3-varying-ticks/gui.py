from tkinter import *
import time

# the class
class AnimatedGui(Tk):
    def __init__(self):
        super().__init__()
        
        # load resources
        self.ms_char_1 = PhotoImage(file="U:\\com404\\2-guis\\5-animation\\3-varying-ticks\\MS_char_1.gif")
        self.ms_char_2 = PhotoImage(file="U:\\com404\\2-guis\\5-animation\\3-varying-ticks\\MS_char_2.gif")
        self.ms_char_3 = PhotoImage(file="U:\\com404\\2-guis\\5-animation\\3-varying-ticks\\MS_char_3.gif")
        
        # set window attributes
        self.configure(height=500,
                       width=500)

        # set animation attributes
        self.num_ticks = 0
        
        self.person_1_x_pos = 15 
        self.person_1_y_pos = 15
        self.person_1_x_change = 10
        self.person_1_y_change = 0

        self.person_2_x_pos = 425 
        self.person_2_y_pos = 175 
        self.person_2_x_change = -10
        self.person_2_y_change = 0

        self.person_3_x_pos = 15 
        self.person_3_y_pos = 275 
        self.person_3_x_change = 10
        self.person_3_y_change = 0
        
        # add components
        self.add_ms_char_1_label()
        self.add_ms_char_2_label()
        self.add_ms_char_3_label()
        
        # start the timer
        self.tick()
        
    # the timer tick function    
    def tick(self):

        self.num_ticks += 1
    
        # person 1
        self.person_1_x_pos += self.person_1_x_change
        self.person_1_y_pos += self.person_1_y_change
        self.ms_char_1_label.place(x=self.person_1_x_pos,
                                        y=self.person_1_y_pos)
        # hit right
        if self.person_1_x_pos >= 446:
            self.person_1_x_pos = 445
            self.person_1_x_change = 0
            self.person_1_y_change = 10
        # hit bottom
        if self.person_1_y_pos >= 126:
            self.person_1_y_pos = 125
            self.person_1_y_change = 0
            self.person_1_x_change = -10
        # hit left
        if self.person_1_x_pos <= 14:
            self.person_1_x_pos = 15
            self.person_1_x_change = 0
            self.person_1_y_change = -10
        # hit top
        if self.person_1_y_pos <= 14:
            self.person_1_y_pos = 15
            self.person_1_y_change = 0
            self.person_1_x_change = 10
        
        if (self.num_ticks % 4 == 0):
            # person 2
            self.person_2_x_pos += self.person_2_x_change
            self.person_2_y_pos += self.person_2_y_change
            self.ms_char_2_label.place(x=self.person_2_x_pos,
                                            y=self.person_2_y_pos)
            
            # hit left
            if self.person_2_x_pos <= 14:
                self.person_2_x_pos = 15
                self.person_2_x_change = 0
                self.person_2_y_change = 10
            # hit bottom
            if self.person_2_y_pos >= 225:
                self.person_2_y_pos = 224
                self.person_2_y_change = 0
                self.person_2_x_change = 10
            # hit right
            if self.person_2_x_pos >= 446:
                self.person_2_x_pos = 445
                self.person_2_x_change = 0
                self.person_2_y_change = -10            
            # hit top
            if self.person_2_y_pos <= 174:
                self.person_2_y_pos = 175
                self.person_2_y_change = 0
                self.person_2_x_change = -10


        if (self.num_ticks % 2 ==0):
            # person 3
            self.person_3_x_pos += self.person_3_x_change
            self.person_3_y_pos += self.person_3_y_change
            self.ms_char_3_label.place(x=self.person_3_x_pos,
                                            y=self.person_3_y_pos)
            # hit right
            if self.person_3_x_pos >= 446:
                self.person_3_x_pos = 445
                self.person_3_x_change = 0
                self.person_3_y_change = 10
            # hit bottom
            if self.person_3_y_pos >= 476:
                self.person_3_y_pos = 475
                self.person_3_y_change = 0
                self.person_3_x_change = -10
            # hit left
            if self.person_3_x_pos <= 14:
                self.person_3_x_pos = 15
                self.person_3_x_change = 0
                self.person_3_y_change = -10
            # hit top
            if self.person_3_y_pos <= 274:
                self.person_3_y_pos = 275
                self.person_3_y_change = 0
                self.person_3_x_change = 10
            
        self.after(100, self.tick)

    # the person images
    def add_ms_char_1_label(self):
        self.ms_char_1_label = Label()
        self.ms_char_1_label.place(x=self.person_1_x_pos,
                                        y=self.person_1_y_pos)
        self.ms_char_1_label.configure(image=self.ms_char_1)

    def add_ms_char_2_label(self):
        self.ms_char_2_label = Label()
        self.ms_char_2_label.place(x=self.person_2_x_pos,
                                        y=self.person_2_y_pos)
        self.ms_char_2_label.configure(image=self.ms_char_2)

    def add_ms_char_3_label(self):
        self.ms_char_3_label = Label()
        self.ms_char_3_label.place(x=self.person_3_x_pos,
                                        y=self.person_3_y_pos)
        self.ms_char_3_label.configure(image=self.ms_char_3)
  
# the object
if __name__ == "__main__":
    gui = AnimatedGui()    
    gui.mainloop() 