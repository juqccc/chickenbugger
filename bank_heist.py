import time
import random


# Pretty typewriter text
def typewriter(text):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(0.05)
    print("\n")


# Scene 1
def scene_1():
    # Encrypted note to find the manager
    find_manager_note = (
        "Very few Answers are Useless, Look Thoroughly. "
        "Realizing Only Ordinary Methods are sufficient, "
        "Only the Mightiest Reach their Objective Mission."
    )

    typewriter("Scene 1: The Bank Robbery")
    typewriter("The bank is in total chaos, everyone is terrified!")
    typewriter("The employees can't believe what just happened!")
    typewriter("You decided it would be best to go in each room to look for clues.")
    typewriter("Clues the robbers might've left behind.")
    typewriter("You tell everyone to remain calm.")
    typewriter("You begin to scout the room, hoping to find the manager.")
    typewriter("There is no sign of the manager anywhere.")
    typewriter('You ask everyone, "Where is the manager?"')
    typewriter(
        "You got no answer, but long behold, someone hiding behind the front desk\n"
        "hands you a piece of paper."
    )
    typewriter(f"The note says:\n{find_manager_note}")

    rooms = {
        'vault room': {
            'clue1': 'footprint',
            'clue2': 'fingerprint',
            'clue3': 'gloves',
            'manager': True
        },
        'break room': {
            'clue1': 'note',
            'clue2': 'mask',
            'clue3': 'hair strand',
            'manager': False
        },
        'manager office': {
            'clue1': 'voice recorder',
            'clue2': 'ski mask',
            'clue3': 'bag',
            'manager': False
        }
    }

    # Timer logic
    start_time = time.time()
    time_limit = 120  # 2 minutes to find manager

    while True:
        passed_time = time.time() - start_time
        remaining_time = int(time_limit - passed_time)
        if passed_time > time_limit:
            typewriter("Time's up!!! The manager has met his fate... Game Over.")
            break

        # Display options
        typewriter(f"Where do you want to search? Options: {', '.join(rooms.keys())}")
        chosen_room = input("Enter the name of the room: ").strip().lower()

        if chosen_room not in rooms:
            typewriter("Invalid room. Please choose a valid option.")
            continue

        room_data = rooms[chosen_room]
        typewriter(f"You enter the {chosen_room} and start searching.....")

        # Check if manager is in the room
        if room_data.get('manager'):
            typewriter("Hooray!! You found the manager. He is alive but shaken. Good job!")
            break
        else:
            typewriter("No sign of the manager here. Keep searching.")

        # Show clues in the room
        for clue in ['clue1', 'clue2', 'clue3']:
            typewriter(f"You found a clue: {room_data[clue]}")

        # Time left
        typewriter(f"Time remaining: {remaining_time} seconds.")


# Scene 2
def scene_2():
    typewriter(
        "As you gather the witnesses and start asking questions, the room feels tense. Everyone has a story, but something doesn’t seem right."
    )

    witnesses = {
        "1": {
            "truths": [
                "The robbers were covered in all black and had a black ski mask on.",
                "The robbers had a heavy accent."
            ],
            "lies": [
                "They busted in at exactly 4:55 am.",
                "I didn’t see anything; I was too busy with customers."
            ]
        },
        "2": {
            "truths": [
                "They seemed to be pretty tall from my point of view.",
                "One of them had a scar on their cheek."
            ],
            "lies": [
                "I saw them drive off in a red Camry.",
                "They looked young, like teenagers."
            ]
        },
        "3": {
            "truths": [
                "I remember they busted in approximately 4:55 am.",
                "The robbers seemed nervous and kept looking around."
            ],
            "lies": [
                "One of the robbers had SpongeBob pajamas on.",
                "They escaped by running down the street."
            ]
        },
        "4": {
            "truths": [
                "I saw them drive off in a red Camry.",
                "There were two robbers, not three."
            ],
            "lies": [
                "I saw one with a rubber duck mask on.",
                "They were wearing all white clothes."
            ]
        },
        "5": {
            "truths": [
                "One had a rubber duck mask on.",
                "They were carrying a duffel bag full of cash."
            ],
            "lies": [
                "They seemed to be tall from my point of view.",
                "They were shouting at each other while inside."
            ]
        },
        "6": {
            "truths": [
                "I could hear the robbers talking, but couldn’t understand them.",
                "One of the robbers had a tattoo on their arm."
            ],
            "lies": [
                "They used a crowbar to break into the vault.",
                "I didn’t see anyone inside the bank when they entered."
            ]
        }
    }

    # Convert dict_keys to list for random sampling
    pick_3_liars = random.sample(list(witnesses.keys()), 3)
    liars = set(pick_3_liars)
    total_questioned = 0
    questioned_witnesses = []

    while total_questioned < 6:
        if total_questioned > 0:
            witness_to_question = input(
                f"\nYou've questioned {total_questioned} out of 6 witnesses: {', '.join(questioned_witnesses)}. "
                "Which one would you like to question next? (1-6): "
            )
        else:
            witness_to_question = input("You have 6 witnesses. Which one would you like to question first? (1-6): ")

        if witness_to_question in questioned_witnesses:
            print("You've already questioned this witness.")
            continue
        elif witness_to_question not in witnesses:
            print("Invalid witness number. Please choose between 1 and 6.")
            continue

        questioned_witnesses.append(witness_to_question)

        truth_or_lie = 'lies' if witness_to_question in liars else 'truths'
        witness_statement = random.choice(witnesses.get(witness_to_question)[truth_or_lie])
        total_questioned += 1
        print(f"\nWitness {witness_to_question} says: \"{witness_statement}\"")

    typewriter(
        "\nAfter questioning the witnesses and reviewing the information, it's time to figure out the liars. "
        "But you only have 3 tries!"
    )

    correct_guesses = set()
    incorrect_guesses = set()
    chances = 3

    while len(correct_guesses) < 3 and len(incorrect_guesses) < chances:
        guess_the_liar = input("Enter the number of the witness you think is lying: ")

        if guess_the_liar not in witnesses:
            print("Invalid input. Please choose a valid witness number (1-6).")
            continue

        if guess_the_liar in correct_guesses or guess_the_liar in incorrect_guesses:
            print(
                f"You've already guessed Witness {guess_the_liar} "
                f"{'correctly' if guess_the_liar in correct_guesses else 'incorrectly'}."
            )
        else:
            if guess_the_liar in liars:
                correct_guesses.add(guess_the_liar)
                print(f"CORRECT! Witness {guess_the_liar} is lying.")
            else:
                incorrect_guesses.add(guess_the_liar)
                print(f"WRONG! Witness {guess_the_liar} is not lying.")

    if len(correct_guesses) == 3:
        print("You've identified all the liars! Great work!")
    else:
        print("You ran out of guesses! Better luck next time.")
    truthful_witnesses = [witness for witness in witnesses.keys() if witness not in liars]
    return truthful_witnesses


def scene_3(truthful_witnesses):
    typewriter("Scene 3: Pursuing the Robbers")

        # Clues based on truthful witnesses
    final_clues = {
            "1": "The robbers spoke with a heavy accent and were wearing ski masks.",
            "2": "The robbers seemed tall, and one had a scar on their cheek.",
            "3": "The robbers entered the bank at 4:55 am and were very nervous.",
            "4": "The robbers drove off in a red Camry, and there were two of them.",
            "5": "The robbers carried a duffel bag full of cash, and one wore a rubber duck mask.",
            "6": "One of the robbers had a tattoo on their arm, and they were whispering to each other."
        }

    typewriter("Based on the witnesses who told the truth, you piece together the story.")
    for witness in truthful_witnesses:
        typewriter(f"Witness {witness} revealed: {final_clues[witness]}")

        # Building the final decision making
        typewriter(
            "\nWith this information, you must decide where to go next. "
            "Each location has a risk, and time is running out!"
        )

        locations = {
            "downtown warehouse": "A place where suspicious activity has been reported recently.",
            "abandoned docks": "A witness reported seeing a red Camry heading toward the docks.",
            "riverside motel": "The robbers might be hiding in a motel near the city outskirts."
        }

        typewriter("Here are your options:")
        for location, description in locations.items():
            typewriter(f"- {location}: {description}")

        chosen_location = input("Enter the name of the location you want to investigate: ").strip().lower()

        # Outcome based on the chosen location
        if chosen_location == "abandoned docks":
            typewriter(
                "You arrive at the docks just in time to see the robbers boarding a speedboat! "
                "With quick thinking, you radio for backup, and the robbers are apprehended. Great job!"
            )
        elif chosen_location in locations:
            typewriter(
                f"You search the {chosen_location}, but it turns out to be a dead end. "
                "The robbers have escaped... Better luck next time!"
            )
        else:
            typewriter("Invalid choice. The robbers have escaped because of the delay!")

def scene_3(truthful_witnesses):
    typewriter("Scene 3: Pursuing the Robbers")

    # Clues based on truthful witnesses
    final_clues = {
        "1": "The robbers spoke with a heavy accent and were wearing ski masks.",
        "2": "The robbers seemed tall, and one had a scar on their cheek.",
        "3": "The robbers entered the bank at 4:55 am and were very nervous.",
        "4": "The robbers drove off in a red Camry, and there were two of them.",
        "5": "The robbers carried a duffel bag full of cash, and one wore a rubber duck mask.",
        "6": "One of the robbers had a tattoo on their arm, and they were whispering to each other."
    }

    typewriter("Based on the witnesses who told the truth, you piece together the story.")
    for witness in truthful_witnesses:
        typewriter(f"Witness {witness} revealed: {final_clues[witness]}")

    # Building the final decision point
    typewriter(
        "\nWith this information, you must decide where to go next. "
        "Each location has a risk, and time is running out!"
    )

    locations = {
        "downtown warehouse": "A place where suspicious activity has been reported recently.",
        "abandoned docks": "A witness reported seeing a red Camry heading toward the docks.",
        "riverside motel": "The robbers might be hiding in a motel near the city outskirts."
    }

    typewriter("Here are your options:")
    for location, description in locations.items():
        typewriter(f"- {location}: {description}")

    chosen_location = input("Enter the name of the location you want to investigate: ").strip().lower()

    # Outcome based on the chosen location
    if chosen_location == "abandoned docks":
        typewriter(
            "You arrive at the docks just in time to see the robbers boarding a speedboat! "
            "With quick thinking, you radio for backup, and the robbers are apprehended. Great job!"
        )
    elif chosen_location in locations:
        typewriter(
            f"You search the {chosen_location}, but it turns out to be a dead end. "
            "The robbers have escaped... Better luck next time!"
        )
    else:
        typewriter("Invalid choice. The robbers have escaped because of the delay!")


# Start Game
def start_game():
    scene_1()
    truthful_witnesses = scene_2()
    scene_3(truthful_witnesses)


# Run the game
start_game()
