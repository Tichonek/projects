#guess the number game

import random

def choose_range():
    """Selecting the range of numbers from which the number to be guessed will be drawn"""

    #Take from user a minimum number
    active = True
    while active:
        try:
            min_value = int(input("\nEnter a minimum value: "))
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

    #print(f"I wll pick a number from between {min_value} and {max_value}")
    
    #adding 1 to max_value because of function range(start, stop)
    max_value += 1
    
    #returning tuple of minimum value and maximum value
    numbers_range = min_value, max_value
    return numbers_range
    
def standard_game():
    """Function with standard game mechanic"""

    #asking player if he wants his own numbers range or standard range
    if ask_range():
        user_range = choose_range()

        secret_number = random.randint(user_range[0], user_range[1]-1)
        print(f"\nI am thinking about one number from between {user_range[0]} and {user_range[1]-1}...")
        #print(f"---{secret_number}---")
        #print(f"---{user_range}---")
    #variable with a secret number which player has to guess
    else:
        secret_number = random.randint(1,100)
        print("\nI am thinking about one number from between 1 and 100...")

    #player guess counter
    count = 1

    active = True
    while active:
        
        #ask player for a number
        try:
            #player guess counter
            print(f"This is your {count} try!")
            count += 1

            guess = int(input("\nMy choice is: "))
        except ValueError:
            print("\nThis is not a number!")
            continue
        else:
            #check if player's guess is correct
            if guess == secret_number:
                print(f"\nGreat! I was thinking about this number! ({secret_number})")
                active = False
        
            if guess > secret_number:
                print("\nToo big...")
                continue

            if guess < secret_number:
                print("\nToo small...")
                continue
        
def welcome_and_menu():
    """Function to display welcome message and instrucion about game"""

    print("\nHello in 'Guess the Number' game! You have to guess the number the computer is thinking of.")
    print("\nDefault range is from between 1 and 100, but you can change it to your own range.")

    #menu for player to choose option
    choice = None
    while choice != "0":
        print("""
            0 - Exit
            1 - Play!
            """
        )
        choice = input("Option: ")

        #exit game
        if choice == "0":
            print("\nGoodbye!")
            break
        #play game
        elif choice == "1":
            standard_game()
        
        #bad option
        else:
            print("\nBad option")
        

def ask_range():
    """Function to ask player if he wants to make his own number range in game.  If yes, he can enter his own range, otherwise he plays with default range"""

    active = True
    while active:
        ask = input("\nWould you like your own range? (y/n): ")
        question_status = None
        if ask.lower() == "y":
            question_status = True
            active = False
        elif ask.lower() == "n":
            question_status = False
            active = False
        else:
            print("\nBad option xd")
            continue
    return question_status


def main():
    welcome_and_menu()

main()









#numbers_range = choose_range()
#print(numbers_range)

#standard_game()
#Je??li min_value b??dzie wi??ksze lub r??wne  max_value to b????d. Trzeba zrobi?? warunek, kt??ry nie pozwoli na to
#Do max_value trzeba doda?? 1, ??eby si?? zgadza??o z tym co user wpisa??
#standard_game()