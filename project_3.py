#Numer Guessing Game - in this user will guess the no ie randomly generated
import random

#ask a user to get the how the large no they want to generate
top_of_range = input("Type a number : " )

#to check enter number is digit or a string
if top_of_range.isdigit():
    top_of_range = int(top_of_range)

    #to check if the number is greater than zero
    if top_of_range <= 0:
        print("Please type a number greater than a 0 next time")
        quit()
#if it is a string ask user to enter a digit
else:
     print("Please type a number  0 next time")
     quit()

random_number = random.randint(0,top_of_range)
guesses = 0
 # above code generates the random guess
 #now we have to guess the randomly generated number

while True:
   guesses +=1
   user_guess = input("Make a guess: ")
   #checking if the user guess is a number or string
   if user_guess.isdigit():
    user_guess = int(user_guess)

#if it is a string ask user to enter a digit
   else:
      print("Please type a number  0 next time")
      continue
   
   if user_guess == random_number:
      print("You got it ")
      break
   elif user_guess > random_number:
         print("You were above the number")
   else:
         print("You are below the number")

print("You got it in", guesses,"guesses")
    


