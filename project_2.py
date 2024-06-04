print("Welcome to my computer quiz")

#asking player if you they want to play
playing = input("Do you want to play? ")
 
#if it is not equal to yes it will quit
if playing.lower() != "yes":
    quit()  #it will quit from the quiz

print("Okay! Let's Play........")
score = 0

#quiz questions begins
answer = input("What is the capital of India? ").lower()
if answer == "new delhi":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

answer = input("What is the currency of India? ").lower()
if answer == "inr":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

answer = input("When was India’s Independence Day? ").lower()
if answer == "august":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

answer = input("Where is India’s Silicon Valley located? ").lower()
if answer == "bangalore":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

answer = input("What is the richest state in India? ").lower()
if answer == "maharashtra":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

print("You got " + str(score) + " questions correct!")
print("You got" + str((score/5)*100) + " % ")


