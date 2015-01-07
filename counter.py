#!/usr/bin/env python3

import math

print "Select coins to count:"
print "(a)   1p Coins"
print "(b)   2p Coins"
print "(c)   5p Coins"
print "(d)  10p Coins"
print "(e)  20p Coins"
print "(f)  50p Coins"
print "(g) 100p Coins"
print "(h) 200p Coins"

print

def chooseAnOption():
    option = raw_input("Choose an option (A-H): ")
    
    coinMass = 0.00
    
    if (option == "A"):
        coinMass = 3.56
    elif (option == "B"):
        coinMass = 7.12
    elif (option == "C"):
        coinMass = 3.25
    elif (option == "D"):
        coinMass = 6.5
    elif (option == "E"):
        coinMass = 5.0
    elif (option == "F"):
        coinMass = 8.0
    elif (option == "G"):
        coinMass = 9.5
    elif (option == "H"):
        coinMass = 12.0
    else:
        print "There was an error."
        chooseAnOption()
    return coinMass
    

coinMass = chooseAnOption()

incBag = raw_input("Is the money in a bank bag? (Y/N): ")

def isBagged():
    if (incBag == "Y"):
        adjustments = -1.20
    elif (incBag == "N"):
        adjustments = 0.00
    else:
        print "Error."
        isBagged()
    return adjustments

def calculateCoins():
    
    print "--- Preparing to Calculate Worth ---"
    print
    massOfTotalCoins = float(raw_input("Mass of Coins (inc Bag): "))
    realMass = float(massOfTotalCoins) + adjustments
    print "Mass of Coins (exc bag): " + str(realMass) + "g"
    amountOfCoins = realMass / coinMass
    
    actualCoins = round(amountOfCoins)
    percentageDifference = (actualCoins - amountOfCoins)/actualCoins
    apparatusError = 0.1/massOfTotalCoins
    
    print "Amount of Coins: " + str(actualCoins)
    
    if (percentageDifference >= apparatusError):
        print "Percentage Difference of " + str(percentageDifference * 100) + "% is not accounted for by apparatus error, consider repeating."

adjustments = isBagged()
calculateCoins()


    
