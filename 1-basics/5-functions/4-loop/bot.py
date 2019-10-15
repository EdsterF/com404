#Function
def cross_bridge(distance):

    for step in range(distance):
        print("Crossed Step.")
    

    if distance < 5:
        print ("we must keep going!")
    else:
        print ("The bridge is collapsing!")
        
    
    


#Call to function
cross_bridge(3)
cross_bridge(6)
