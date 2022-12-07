#guess the number game

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
    

numbers_range = choose_range()
print(numbers_range)



#Jeśli min_value będzie większe lub równe  max_value to błąd. Trzeba zrobić warunek, który nie pozwoli na to
#Do max_value trzeba dodać 1, żeby się zgadzało z tym co user wpisał
