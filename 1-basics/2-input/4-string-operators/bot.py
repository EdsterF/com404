## String Operators ##

#Questions

print("")
print("Please enter the number of lives.")
lives = int(input())
print("")

print("Please enter the energy level.")
energy = int(input())
print("")

print("Please enter the shield level.")
shield = int(input())
print("")

#Symbols

lives_symbol = "♥"
energy_symbol = "☺"
shield_symbol = "♦"

#Calculations

lives_level = lives * lives_symbol
energy_level = energy * energy_symbol
shield_level = shield * shield_symbol

#Results

print("Lives:  ", lives_level)
print("")
print("Energy: ", energy_level)
print("")
print("Shield: ", shield_level)
print("")