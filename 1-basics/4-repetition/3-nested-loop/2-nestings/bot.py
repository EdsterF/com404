# question + user input 1
print("")
print("Please enter a sequence")
sequence = input()

# question + user input 2
print("")
print("Please enter the character for the marker")
marker = input()

#other variable
marker_begin = 0
marker_end = 0
#nested loops
for marker_position in range (0, len(sequence), 1):
    non_marker = sequence[marker_position]

    if (non_marker == marker):
        if (marker_begin == 1):
            marker_begin = marker_position

        else:
            marker_end = marker_position

print("")
print ("The distance between the markers is ", marker_end - marker_begin -1, ".")
print("")


