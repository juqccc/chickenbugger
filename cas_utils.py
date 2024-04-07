# cas_utils.py


def bet_annoucement(user_cash):
    print(f"Your current cash balance is ${user_cash}")
    while True:
        try:
            bet_amount = int(input("Enter your bet amount: "))
            if bet_amount > 0 and bet_amount <= user_cash:
                user_cash -= bet_amount  # Deduct the bet amount from the user's cash
                print(f"Your remaining cash balance is ${user_cash}")
                return bet_amount
            else:
                print(
                    "Invalid bet amount. Please enter a valid amount within your cash balance."
                )
        except ValueError:
            print("Invalid input. Please enter a valid integer amount.")
