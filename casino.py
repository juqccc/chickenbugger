import random
import games as cg

user_cash = 0
from cas_utils import bet_annoucement


def age_verfication():
    print("Welcome...Please enter your age(18+ ONLY)")
    user_age = int(input())
    if user_age >= 18:
        print("\nAge verification successful, Make sure to follow the rules below.\n")
    else:
        print("Age verification failed. You will be escorted")
        exit()


def casino_games():

    game_choice = int(
        input(
            "Which game would you like to play (Enter the number): \n1. Blackjack\n2. Dice Roll\n3. High Low\n"
        )
    )

    if game_choice == 1:
        #  bet_amount = bet_annoucement(user_cash)
        cg.blackjack(user_cash)
    if game_choice == 2:
        # bet_amount = bet_annoucement(user_cash)
        cg.diceroll()
    if game_choice == 3:
        # bet_amount = bet_annoucement(user_cash)
        cg.highlow()


def main():
    global user_cash
    user_cash = 0

    age_verfication()
    print(
        """\
No Fighting
No Smoking Inside
No Sexual Activities
No Cheating
Lastly, Have fun."""
    )

    # ANSI escape codes for styling
    bold = "\033[1m"
    reset = "\033[0m"

    # Print a fancy message with bold text and a colored background
    print(bold + "Press Enter to continue..." + reset)

    # Pause until the user presses Enter
    input()

    while True:
        user_deposit = input(
            "Enter an amount to deposit to be able to play a game. ($500+): "
        )
        if user_deposit.isdigit():
            user_deposit = int(user_deposit)
            if user_deposit >= 500:
                # global user_cash
                user_cash += user_deposit
                break
            else:
                print("Please enter an amount above $500")
        else:
            print("Invalid Number")

    # ANSI escape codes for styling
    bold = "\033[1m"
    reset = "\033[0m"

    # Print a fancy message with bold text and a colored background
    print(bold + "\nPress Enter to continue..." + reset)

    # Pause until the user presses Enter
    input()

    casino_games()


main()
