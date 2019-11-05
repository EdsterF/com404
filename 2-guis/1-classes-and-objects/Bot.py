class Bot:

    #constructor (only add in brackets arguments that are going to be queried)
    def __init__(self, name, age=0): #(so not included energy or shield)
        self.name = name
        self.age = age
        self.energy = 100
        self.shield = 100

    #methods #get
    def get_age(self):
        return self.age

    def get_energy(self):
        return self.energy

    def get_name(self):
        return self.name

    def get_shield(self):
        return self.shield

    #methods #get
    def decrement_energy(self, energy=-1):


    def display_name(self):
        name_lenght= len(self.name)
        print("#"+"#" * name_lenght +"###")
        print("#", self.name, "#")
        print("#"+"#" * name_lenght +"###")

    def display_age(self):
        print("     ", self.age)
        print("   __##__")
        print(" __#____#__")
        print(" #        # ")
        print("############")

    def display_energy(self):
        print("shield = "+("#" * self.energy))

    def display_shield(self):
        print("____________")
        print("|          |")
        print("|  ", self.shield, "   |")
        print("\\         /")
        print(" \\       /")
        print("  \\     /")
        print("   \\   /")
        print("    \\ /")
        print("     V")

    def display_summary(self):
        print("{} is {} years old and has an energy level of {} with a shiled level of {}".format(self.name, self.age, self.energy, self.shield))

    def __str__(self):
        return ("name="+self.name+","+"age="+self.age+","+self.energy+","+self.shield)

#object of Bot
beep = Bot("Beep")
beep.display_name()
beep.display_age()
beep.display_energy()
beep.display_shield()




