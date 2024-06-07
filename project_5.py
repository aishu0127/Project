#choose your adventure game - ask user to get make choices 

name = input("Type your name: ")
print("Welcome", name, "to this adventue!" )

answer = input("You are on a dirt road, it has come to and end and you can go left or right. Which way would you like to go? ").lower()

if answer == "left":
    answer =input("you came to a river, you can walk around or swim.Type walk to walk around and swim to swim across ").lower()

    if answer == "swim":
        print("You swim across and were eaten by alligator")
    
    elif answer == "walk":
        print("You walk for many miles, ran out of water and you lost the game")

    else:
        print("Not a valid option.You loose")


elif answer == "right":
    answer = input("you came to a brigde, it looks woblly.Do you want to cross it or head back (cross/back)?:  ").lower()
    if answer == "back":
        print("you can go back")

    elif answer == "cross":
        answer = input("you cross the bridge and met a stranger. Do you want to talk to them?: ").lower()
        if answer == "yes":
            print("you a got gold after talking to stranger. You win!!!")

        elif answer == "no":
            print("You ignored the stranger and they are offended")

        else:
            print("Not a valid option.you loose!!")

else:
    print("Not a valid option.You loose")