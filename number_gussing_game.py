import random
import math

# giving greattings
print("Hi. Welcome to the game.")

# getting inputs
upper_num=int(input("Enter upper limit: "))
lower_num=int(input("Enter lower limit: "))
# generating random number
number=random.randint(lower_num,upper_num)

# give a limited chance to guess the number
def new_func(upper_num, lower_num):
    chance=math.ceil(math.log(upper_num-lower_num+1,2))
    return chance

chance = new_func(upper_num, lower_num)
print("You have got ",chance," chances to guess the game.")

while chance >0 :
    chance-=1
    guess_number=int(input("Enter your number: "))

    if guess_number == number :
        print("Congratulations.you won.")
        break
    elif guess_number < number :
        print("Your number is lower than the guessed number.You have left ",chance ,"Try again")
        continue 
    elif guess_number > number :
        print("Your number is higher than the guessed number.You have left ",chance , "Try again")
        continue

if  chance ==0 :
    print("You have lost the game. Better luck next time.")
    


