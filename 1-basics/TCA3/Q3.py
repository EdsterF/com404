#Intro message
print("How many heroes must we gather?")

#User response
heroes_num = int(input())

print("Gathering heroes...")

#variable
heroes_min_num=0

#loop
while heroes_num>heroes_min_num: #(heroes_min_num, heroes_num, 1):
    heroes_min_num=heroes_min_num+1
    print("...found hero", heroes_min_num)

#Final statement
print("...all the heroes have been gathered")