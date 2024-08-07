
import random 
i = 10
cond = True
user_input = int(input("Guess Number between 1 and 20 = "))
guess = random.randint(1,20)
while cond or i == 0:
    user_input = int(input("Guess Number between 1 and 20 = "))
    if user_input > guess :
        print("To High")
        i = i-1

    elif user_input < guess :
        print("Too Low")
        i = i - 1

    elif user_input == guess:
        print("You Won ")
        print(f"You did on {i} attempt ")
        break