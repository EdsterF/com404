## This will continue BEEP's story, by finding out its remaining battery power.

print("")
print("""Please confirm my current lives, energy and shield levels.
I'll then work out my average power left with your help, and total time to full charge""")

#Questions

print("")
print("Please enter the number of lives (From 1 to 10).")
lives = int(input())
print("")

print("Please enter the energy level (From 1 to 10).")
energy = int(input())
print("")

print("Please enter the shield level (From 1 to 10).")
shield = int(input())
print("")

#Symbols

lives_symbol = "♥"
energy_symbol = "☺"
shield_symbol = "♦"
average_power_symbol = "☼"

#Calculations

lives_level = lives * lives_symbol
energy_level = energy * energy_symbol
shield_level = shield * shield_symbol
average_power = int((lives + energy + shield)/3) * average_power_symbol


#Results

print("Lives:  ", lives_level)
print("")
print("Energy: ", energy_level)
print("")
print("Shield: ", shield_level)
print("")

print("Press ENTER now for me to work out my average power based on above levels (The results will be displayed on my Power Monitor)")
enter = input()
print(" $     $   $    $")
print("    $     $    $")
print("    ###########")
print("    #  @   @  #")
print("    #    |    #")
print("    #  \\__/   #")
print("    ###########")
print("         ##    ")
print("")
print("POWER MONITOR: ", average_power)
print("")

#Questions

print("Now can you check my power monitor and tell me how many power lights \"☼\" are on?")

power_monitor = int(input())

#Calculations

power_percentage = int((100/10) * power_monitor)

#Results
print("Based on this, the percentage of power left is: ", power_percentage, "%")
print("My charging capabilities are 1% every 5 minutes")

#Calculations
charging_time_minutes = int(100-power_percentage) * 5
charging_time_hours = charging_time_minutes // 60
minutes = charging_time_minutes % 60

#Results
print("Total remaining time to full charge is: ", charging_time_minutes, "minutes")
print("or ", charging_time_hours, "hour(s)", minutes, "minute(s)")