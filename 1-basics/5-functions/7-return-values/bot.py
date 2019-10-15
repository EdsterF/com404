#Functions
def sum_weights(beep_weight, bop_weight):
    tot_weight= (beep_weight+bop_weight)
    return tot_weight

def calc_avg_weight(beep_weight, bop_weight):
    avg_weight= sum_weights(beep_weight, bop_weight)/2
    return avg_weight


def run():
    print("What is the weight of Beep?")
    beep_weight= float(input())

    print("")
    print("What is the weight of Bop?")
    bop_weight= float(input())
    print("")

    print("What would you like to calculate (sum or average)?")
    reply=input()

    print("")
    if(reply == "sum"):
        print("The sum of Beep and Bop's weight is ", sum_weights(beep_weight, bop_weight), ".")
    elif(reply == "average"):
        print("Beep and Bop's average weight is", calc_avg_weight(beep_weight, bop_weight), ".")

#Call to Function
run()