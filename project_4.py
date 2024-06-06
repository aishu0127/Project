import random

#both the scores starting from zero to see who wins
user_wins = 0
computer_wins = 0

options = ["rock", "paper", "scissors" ]

while True:
    user_input = input("Type Rock/Paper/Scissors or Q to quit: ").lower()
    if user_input == "q":
        break

    if user_input not in ["rock", "paper", "scissors" ]:
        continue

    random_number = random.randint(0,2)
    #0=Rock, 1=Paper, 2=Scissors
     
    computer_pick = options[random_number].lower()
    print("Computer picked", computer_pick + ".")

    if user_input == "rock" and computer_pick == "scissors":
        print("You Won!")
        user_wins += 1

    elif user_input == "paper" and computer_pick == "rock":
        print("You Won!")
        user_wins += 1

    elif user_input == "scissors" and computer_pick == "paper":
        print("You Won!")
        user_wins += 1

    else:
        print("You lost!")
        computer_wins += 1
    
print("you won", user_wins, "times")
print("Computer wins", computer_wins, "times")
print("Goodbye!")
