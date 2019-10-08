#User input
print("How many live cables must I avoid?")
max_live_cables = int(input())

#control variable
cables_avoided = 0

#Condition
while (cables_avoided < max_live_cables):
    print("Avoiding...", end="")
    cables_avoided = cables_avoided + 1
    print("Done!", cables_avoided, "cables avoided.")