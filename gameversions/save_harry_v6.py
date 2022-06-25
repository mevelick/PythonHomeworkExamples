import random

# Initialize constants - game ending variables, set to reference their tuple position:
LEAKY_CAULDRON = 0
MAX_VOLDEMORT_BEHIND = 1
MIN_SPELLS_REMAINING = 2
MIN_BROOM_MAGIC = 3

# Tuple to hold constants:
ENDING_VALUES_TUPLE = (50, 0, 0, 0)

# Reference to variable position in player_start list:
FLEW = 0
BEHIND = 1
MAGIC = 2
SPELLS = 3


def main():
    # Play again loop:
    play_again = 'Y'

    while play_again.upper() == 'Y':
        # Create list of variables:
        player_start = [0, 15, 4, 3]

        # For reference, the variables assignments are/were:
        # miles_flew = 0
        # voldemort_behind = 15
        # broom_magic = 4
        # spells_remaining = 3

        over = False

        splash()

        while not over:

            # Calling function to get user's menu selection
            option = get_user_option()

            if option == 1:
                # Fly:
                player_start = fly(player_start)
            elif option == 2:
                # Add magic:
                player_start = add_magic(player_start)
            elif option == 3:
                # Cast spell:
                player_start = cast_spell(player_start)
            elif option == 4:
                check_stats(player_start)
            elif option == 5:
                save_game(player_start)
            elif option == 6:
                player_start = load_game(player_start)

            over = win_lose(player_start)

        play_again = input("Would you like to play again? Please enter 'Y' or 'N'. ")


# Display splash screen:
def splash():
    print(" *********************************************** ")
    print(" *                                              *")
    print(" *            Welcome to Save Harry!            *")
    print(" *      Save Harry Potter from Voldemort!       *")
    print(" *         Velick Gaming - Version 3.0          *")
    print(" *                                              *")
    print(" *********************************************** ")


# _____________________________________________________________

def menu():
    print("Menu:")
    print("1. Fly")
    print("2. Replenish broom's magic")
    print("3. Cast spell")
    print("4. Check stats")
    print("5. Save game")
    print("6. Load saved game")
    print()


# _____________________________________________________________

def get_user_option():
    # Initialize boolean flag
    valid_option = False

    while not valid_option:
        menu()
        # Code that could raiser an exception
        try:
            user_option = int(input("Pick the option for your turn. "))
        # code to handle to exception if raised
        except ValueError:
            print("Error: The option selected must be an integer.")
        # Checking if the option is within the range
        else:
            valid_option = 1 <= user_option <= 6
            if not valid_option:
                # Error message
                print("Invalid menu selection. Try again. \n")
            else:
                valid_option = True
    # Return valid option
    return user_option


# _____________________________________________________________

def fly(player_start):
    player_start[FLEW] += random.randint(6, 10)
    player_start[BEHIND] -= 5
    player_start[MAGIC] -= 1
    return player_start


# _____________________________________________________________

def add_magic(player_start):
    player_start[MAGIC] += random.randint(1, 3)
    player_start[BEHIND] -= 5
    return player_start


# _____________________________________________________________

def cast_spell(player_start):
    player_start[SPELLS] -= random.randint(1, 2)
    player_start[BEHIND] += 5
    return player_start


# _____________________________________________________________


def check_stats(player_start):
    print("Miles flew:", player_start[FLEW])
    print("Miles voldemort is behind Harry Potter:", player_start[BEHIND])
    print("Magic remaining on your broom:", player_start[MAGIC])
    print("Spells left to cast:", player_start[SPELLS])


# _____________________________________________________________

def save_game(player_start):
    # User will enter a file name
    file_name = input("Enter the name of the file to save the game to: ")

    # Try opening the file
    try:
        outfile = open(file_name + '.txt', 'w')
    except Exception:
        print("Error: The file could not be opened.")
    else:
        # Convert the integer variables to string and write to the file
        outfile.write(str(player_start[FLEW]) + "\n")
        outfile.write(str(player_start[BEHIND]) + "\n")
        outfile.write(str(player_start[MAGIC]) + "\n")
        outfile.write(str(player_start[SPELLS]) + "\n")
        outfile.close()


# _____________________________________________________________

def load_game(player_start):
    # Have the user enter the name of the file to load
    file_name = input("Enter the name of the file to load the game from: ")

    # Try to open the file
    try:
        infile = open(file_name + ".txt", "r")
    except Exception:
        print("Error: The file could not be opened.")
    else:
        # Read each line, convert it back to an int and place its value into the variable
        player_start[FLEW] = int(infile.readline())
        player_start[BEHIND] = int(infile.readline())
        player_start[MAGIC] = int(infile.readline())
        player_start[SPELLS] = int(infile.readline())

        infile.close()

    return player_start


# _____________________________________________________________

# Function evaluating game-ending conditions

def win_lose(player_start):
    if player_start[BEHIND] <= ENDING_VALUES_TUPLE[MAX_VOLDEMORT_BEHIND]:
        print("Oh no! Voldemort caught Harry! You lose, game over!")
        return True
    elif player_start[MAGIC] <= ENDING_VALUES_TUPLE[MIN_BROOM_MAGIC]:
        print("Whoops! Your Nimbus 2000 ran out of magic! You lose, game over!")
        return True
    elif player_start[SPELLS] <= ENDING_VALUES_TUPLE[MIN_SPELLS_REMAINING]:
        print("You muggle! You can't cast any more spells! You lose, game over!")
        return True
    elif player_start[FLEW] >= ENDING_VALUES_TUPLE[LEAKY_CAULDRON]:
        print("You got Harry Potter to the Leaky Cauldron safely! You won the game!")
        return True
    return False


# _____________________________________________________________

main()
