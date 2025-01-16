# Asking the user to type their name and storing the input in the variable 'name'
name = input("Hey! Type your name: ") 

# Displaying a greeting message using the name the user entered. 
# The + symbol is used to concatenate (join) the strings.
print("Hello " + name + " welcome to my game!") 

# Asking the user if they want to play the game. 
# The input is then converted to lowercase using .lower().
# This ensures that whether the user types 'YES', 'Yes', or 'yes', the answer will always be 'yes'.
should_we_play = input("Do you want to play? ").lower() 

# Checking if the user answered 'yes' or 'y', either of which means the user wants to play
# The condition checks if 'should_we_play' is equal to 'yes' OR 'y'. The 'or' keyword is used to check multiple options.
if should_we_play == "yes" or should_we_play == "y":
    # If the user wants to play, print this message
    print("We are gonna play!")  

    # Asking the user whether they want to go 'left' or 'right'.
    # Again, we use .lower() to ensure that the user's answer is in lowercase, so it matches the options we check for.
    direction = input("Do you want to go left or right? (left/right) ").lower()
    
    # If the user chooses 'left', we print the message that the game is over because they fell off a cliff
    if direction == "left":
        print("You went left and fell off a cliff, game over")
    
    # If the user chooses 'right', we ask them to make another choice: to swim under a bridge or to cross it
    elif direction == "right":
        # Asking the user for their choice under the bridge. This time we do not use .lower() as we expect specific answers.
        choice = input("Okay! You went right. Do you want to swim under the bridge or cross it? (swim/cross) ")
        
        # If the user chooses 'swim', they encounter a river monster and lose the game.
        if choice == "swim":
            print("You got eaten by a river monster! The end")
        else:
            # If the user chooses 'cross', they win the game.
            print("You found the game and won!!!")
    
    # If the user enters anything other than 'left' or 'right', this message appears.
    else:
        print("Sorry! Not a valid response :(")

# If the user does NOT want to play (anything other than 'yes' or 'y'), the game ends right away from the first if-else chain and this message is shown
else:
    print("We are NOT playing...")
