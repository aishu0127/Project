#importing random numbers for calculations
import random

#imporing time to set timer
import time

#use of operators 
OPERATOR = ["+" , "-" , "*"]
MIN_OPERAND = 3
MAX_OPERAND = 12
TOTAL_PROBLEMS = 10 #SETTING THE NUMBER OF PROBLEMS

#FUNCTION TO GENERATE RANDOM PROBLEMS
def generate_problem():
    left = random.randint(MIN_OPERAND,MAX_OPERAND)
    right = random.randint(MIN_OPERAND,MAX_OPERAND)
    operator = random.choice(OPERATOR)

    #CREATING THE EXPRESSIONS
    expr = str(left) + "" + operator + "" + str(right)
    answer = eval(expr)  #to check whether the answer is right or wrong
    return expr, answer

wrong = 0 #to check how many are wrong

input("Press enter to Start")  #hit the button start the timer
print("----------------------")

start_time = time.time()  #start timer

#creating a loop to generate problem
for i in range(TOTAL_PROBLEMS):
    expr, answer = generate_problem()
    while True:
        guess =  input("Problem #" + str(i + 1) + ":" + expr + "=")
        if guess == str(answer):
            break
        wrong == 1
end_time = time.time()
total_time = round(end_time - start_time)


print("----------------------")
print("Nice Work! You finished in", total_time, "seconds")      



    