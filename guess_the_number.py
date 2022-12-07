#guess the number game

import random

def choose_range():
    """Selecting the range of numbers from which the number to be guessed will be drawn"""

    #Take from user a minimum number
    active = True
    while active:
        try:
            min_value = int(input("Enter a minimum value: "))
        except ValueError:
            print("Please enter a number!")
        else:
            active = False
    
    #Take from user a maximum number
    active = True
    while active:
        try:
            max_value = int(input("Enter a maximum value: "))
            #Check if min_value is grather than or equal to max_value
            if min_value >= max_value:
                print("Minimum value can't be greater than or equal to maximum value!")
                continue
        except ValueError:
            print("Please enter a number!")
        else:
            active = False

    print(f"I wll pick a number from between {min_value} and {max_value}")
    
    #adding 1 to max_value because of function range(start, stop)
    max_value += 1
    
    #returning tuple of minimum value and maximum value
    numbers_range = min_value, max_value
    return numbers_range
    
def standard_game():
    """Function with standard game mechanic"""

    #variable with a secret number which player has to guess
    secret_number = random.randint(1,100)
    print("I am thinking about one number from between 1 and 100...")

    #player guess counter
    count = 1

    active = True
    while active:
        
        #ask player for a number
        try:
            guess = int(input("My choice is: "))
        except ValueError:
            print("This is not a number!")
            continue
        else:
            #player guess counter
            print(f"This is your {count} try!")
            count += 1
            
            #check if player's guess is correct
            if guess == secret_number:
                print(f"Great! I was thinking about this number! ({secret_number})")
                active = False
        
            if guess > secret_number:
                print("Too big...")
                continue

            if guess < secret_number:
                print("Too small...")
                continue
        

#numbers_range = choose_range()
#print(numbers_range)

standard_game()
#Jeśli min_value będzie większe lub równe  max_value to błąd. Trzeba zrobić warunek, który nie pozwoli na to
#Do max_value trzeba dodać 1, żeby się zgadzało z tym co user wpisał
