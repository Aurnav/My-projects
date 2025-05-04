import random

secret_number = random.randint(1, 10)
attempts = 0

while True:
    user_input = int(input("Guess a number between 1 and 10: "))
    attempts += 1
    
    if user_input < secret_number:
        print("Go higher!")
    elif user_input > secret_number:
        print("Go lower!")
    else:
        print(f"You got it in {attempts} tries!")
        break
