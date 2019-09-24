#Working out user's Body Mass
print("what is your name human?")
user_name = input()
print("")

#Age
print("how old are you (in years)?")
age = int(input())
print("")

#Height
print("How tall are you (in meters)?")
height = float(input())
print("")

#Weight
print("How much do you weigh (in kilograms)?")
weight = float(input())
print("")

#BMI
bmi = (weight/(height*height))
print(user_name, " you are", age, " years old and your bmi is", bmi)
print("")

#((height*height)/age)),