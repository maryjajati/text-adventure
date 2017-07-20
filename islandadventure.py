name = input("What's your name?")

print(name + " ,your plane has just crashed on an abandoned island along with 13 other people, try to survive until someone comes to the rescue")
print("\n")
one = "go fishing"
two = "go hunting"
food = int(input(name + " ,you and your fellow passengers havent eaten in 8 hours and you are starving, are you going to 1)" + one + " or 2)" + two + " : "))

print("\n")

if(food == 1):
    three = "make a new line with the resources around you"
    four = "forget about fishing and go hunting instead"
    choiceone = int(input(name + " ,your line just broke, do you 3)" + three + " or 4)" + four + " : "))
    print("\n")
    print("Great Job " + name + "! You have just saved you and your fellow passengers from starvation")
elif(food == 2):
    five = "kill it with your bare hands"
    six = "starve to death"
    choicetwo = int(input("The animal that you were hunting has just broken your weapon, do you choose to 1) " + five + " or 2) " + six + " : "))
    if(choicetwo == 1):
        print("\n")
        choicethree = int(input("Oh no! You are now surrounded by even more animals that are looking for something to eat, do you 1)run away or 2)fight?"))
            if(choicethree == 1):
                print("Now you and your fellow passengers have to resort to the poisonous berries that make you hallucinate.")
                choicefour = int(input("Since your fellow passengers also ate the berries, they now want to kill you and eat you for food do you 1)run away or 2)fight them off?"))
                    if(choicefour == 1):
                        print("Now you have to learn to survive on your own, atleast until someone comes to rescue you")
                    if(choicefour == 2):
                        print("Great Job! You were able to fight them off!")
            if(choicethree == 2):
                print("You werent able to successfully take them on so you ran away")
                choicefive = int(input("Your fellow passengers are furiated that you ran away, so now they all want to exterminate you and eat you as their only source of food, do you 1)run away or 2)fight them off?"))
                    if(choicefive == 1):
                        print("Now you have to learn to survive on your own, atleast until someone comes to rescue you")
                    if(choicefive == 2):
                        print("Great Job! You were able to fight them off!")
        print("Great Job " + name + "! You have just saved you and your fellow passengers from starvation")
    elif(choicetwo == 2):
        print("\n")
        print("Oh No! You and your fellow passengers have just starved to death!")

print("\n")
print("Someone has just come to rescue you! You and your fellow passangers have survived the abandoned island!")
print("\n")
