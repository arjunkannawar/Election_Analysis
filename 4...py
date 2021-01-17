# Initial variable to track game play

user_play = "y"

# While we are still playing...
while user_play == "y":

    # Ask the user how many numbers to loop through
    user_choice = int(input("how many numbers would you like to loop through?"))    
    # Loop through the numbers. (Be sure to cast the string into an integer.)
    for x in range(user_choice):
        # Print each number in the range
            print(x)

    # Once complete...
    user_play = input("Continue: (y)es or (n)o? ")
