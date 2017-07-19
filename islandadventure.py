print("Your plane has just crashed on an abandoned island along with 13 other people, try to survive until someone comes to the rescue")

one = "go fishing"
two = "go hunting"
food = int(input("You and your fellow passengers havent eaten in 8 hours and you are starving, are you going to 1)" + one + " or 2)" + two + " : "))

if(food == 1):
    three = "make a new line with the resources around you"
    four = "forget about fishing and go hunting instead"
    choiceone = int(input("Your line just broke, do you 3)" + three + " or 4)" + four + " : "))
    print("Great Job! You have just saved you and your fellow passengers from starvation")
elif(food == 2):
    five = "kill it with your bare hands"
    six = "starve to death"
    choicetwo = int(input("The animal that you were hunting has just broken your weapon, do you choose to 5) " + five + " or 6) " + six + " : "))
    if(choicetwo == 5):
        print("Great Job! You have just saved you and your fellow passengers from starvation")
    elif(choicetwo == 6):
        print("Oh No! You and your fellow passengers have just starved to death!")
print("Someone has just come to rescue you! You and your fellow passangers have survived the abandoned island!")

