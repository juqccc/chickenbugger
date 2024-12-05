import random
import cas_utils as utils


def game_robot():
    pass


def blackjack(user_cash):
    bj_player = random.randint(1, 21)
    bj_robot = random.randint(1, 21)
    bet_amount = utils.bet_annoucement(user_cash)
    print("Get as close as possible to 21 without going over!")
    print(f"\nYou have S{bet_amount} riding on this bet.")
    print(f"You: {bj_player}")
    print(f"Ai: {bj_robot}")

    # Game Logic

    if bj_robot == 21:
        print("AI has won by default!")

    if bj_player == 21:
        print("You won by Default!")

    player_score = bj_player
    robot_score = bj_robot

    # PLAYER SCORE LOGIC
    while player_score < 21 and robot_score < 21:
        hit_me = random.randint(1, 12)
        bj_user_choice = input("\nHit Me or I'll Stand (ENTER 'stand'/ hit): ")

        if bj_user_choice.lower() == "hit":
            player_score += hit_me
            print(f"You: {player_score}")
            print(f"Ai: {robot_score}")

            if player_score > 21:
                user_cash -= bet_amount
                print(f"\nBUSTED!, You lost {bet_amount}, You now have ${user_cash}.")
                break

            if player_score == 21:

                user_cash -= bet_amount  # Deduct the initial bet_amount
                user_cash += bet_amount * 2  # Add the doubled bet_amount

                print(f"You: {player_score}")
                print(f"Ai: {robot_score}")
                print(f"\nYou won {bet_amount * 2}, You now have ${user_cash}.")
                break

        # ROBOT SCORE LOGIC
        elif bj_user_choice.lower() == "stand":
            while robot_score < 21:
                hit_me = random.randint(1, 12)
                robot_score += hit_me

                if robot_score > 21:
                    user_cash -= bet_amount  # Deduct the initial bet_amount
                    user_cash += bet_amount * 2  # Add the doubled bet_amount
                    print(f"You: {player_score}")
                    print(f"Ai: {robot_score}")
                    print(f"\nYou won {bet_amount * 2}, You now have ${user_cash}.")
                    break

                if robot_score == 21:
                    user_cash -= bet_amount
                    print(
                        f"\nYou LOST!, ${bet_amount} has been taken from you Cash Balance: {user_cash}"
                    )
                    print(f"You: {player_score}")
                    print(f"Ai: {robot_score}")
                    break

    bj_play_again = input("\nWould you like to play again? Yes/No/Newgame:  ")
    if bj_play_again.lower() == "yes":
        blackjack(user_cash)
    elif bj_play_again.lower() == "no":
        pass
    else:
        pass


def dice_roll():
    pass


def high_low():
    pass
