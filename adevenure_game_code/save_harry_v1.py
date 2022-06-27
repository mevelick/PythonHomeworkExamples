
# Splash screen
game_title = "Save Harry"
developer = "Marni V."
version = 1

print('Game title: ', game_title, '\n''Developer: ', developer,'\n''Version: ',version)

# New line for separation
print('\n')

# Initialization of variables - starting values
miles_traveled = 0
miles_voldemort_behind = 15
broom_magic = 10
spells_remaining = 3

# Game menu:
print("To fly, press F")
print("To replenish your broom's magic, press M")
print("To cast spell, press C")
print("To check stats, press S")
print("To exit, press X")

# New line for separation
print("\n")

play = input("If you'd like to begin, press Y.")

# With the current code, the game doesn't end when it is supposed to. It only ends when the user prompts it to stop.
while play == "Y":
    selection = input("Make your selection.")
    if selection == "F":
        miles_traveled += 7
        broom_magic -= 2
        print("You selected fly.")
    elif selection == "M":
        broom_magic += 5
        print("You replenished your broom's magic.")
    elif selection == "C":
        spells_remaining -= 1
        miles_voldemort_behind -= 5
        print("Confundo! You cast a confusion spell. Voldemort has fallen behind!")
    elif selection == "S":
        print("The number of miles Harry Potter has traveled is", miles_traveled)
        print("The number of miles Voldemort is behind Harry is", miles_voldemort_behind)
        print("The amount of magic remaining on your broom is", broom_magic)
        print("The number of spells you have remaining is", spells_remaining)
    else:
        print("You have entered an invalid key, please try again.")
        input("Make your selection.")
    play = input("If you'd like to continue, press Y")

# New line for separation
print("\n")

# If/Elif to determine if the player won or lost the game (game-ending conditions)

if broom_magic <= 0:
    print("Whoops! Your Nimbus 2000 ran out of magic! You lose!")
elif miles_voldemort_behind >= miles_traveled:
    print("Oh no, Voldemort caught Harry! You have lost the game!")
elif miles_traveled >= 50 & broom_magic > 0 & miles_voldemort_behind < miles_traveled:
    print("You got Harry to the Leaky Cauldron! You saved him and won the game!")

