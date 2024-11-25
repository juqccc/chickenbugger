import time 
import random

''' Bank Heist word game '''

#pretty typewriter text 
def typewriter(str):
	for char in str:
		print(char, end='', flush=True)
		time.sleep(0.01)
	print("\n")
		
#scene 1 

def scene_1():
    typewriter("Scene 1: The Bank Robbery")
    
    clues = ["mask", "footprint", "gloves", "fingerprint", "note", "glass", "shoes", "weapon", "hair strand", "bag"]
    random.shuffle(clues)
    found_clues = []
    
    while len(found_clues) < 3:
        typewriter("The vault is in chaos. Search for any suspicious items.")
        typewriter("Think carefully what might robbers leave behind at a crime scene?")
        
        guess = input("Type a name of a clue to investigate: ").lower()
        if guess in clues:
            if guess not in found_clues:
                found_clues.append(guess)
                typewriter(f"You found the {guess}! Keep searching for more clues.")
                typewriter(f"Clues found: {len(found_clues)}/3. Keep searching!")
            else:
                typewriter("You've already found that clue. Look for something else.")
        else:
            typewriter("That clue doesn't seem to be here! LOOK AGAIN!")
    
    typewriter(f"Good job! You found all 3 clues: {', '.join(found_clues)}.")
    typewriter("You hear whispers among the crowd. Witnesses may have seen something...")
    typewriter("Let's move on to interrogating the witnesses.")
 

def scene_2():
    typewriter("As you gather the witnesses and start asking questions, the room feels tense. Everyone has a story, but something doesn’t seem right.")
    witnesses = {
    "1": {  
        "truths": [
            "The robbers were covered in all black and had a black ski mask on.",
            "The robbers had a heavy accent."
        ],
        "lies": [
            "They were in a hurry to leave, they busted in at exactly 4:55 am.",
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
            "I seen one with a rubber duck mask on.",
            "They were wearing all white clothes."
        ]
    },
    "5": {
        "truths": [
            "I seen one with a rubber duck mask on.",
            "They were carrying a duffel bag full of cash."
        ],
        "lies": [
            "They seemed to be pretty tall from my point of view.",
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
    pick_3_liars = random.sample(witnesses.keys(), 3)
    liars = set(pick_3_liars)
    total_questioned = 0
    questioned_witnesses = []
    
    
    while total_questioned < 6:
        if total_questioned > 0:
               witness_to_question = input(
        f"\nYou've now questioned {total_questioned} out of 6 witness(es): {', '.join(questioned_witnesses)}, which one would you like to question next?: "
                )
        else:
            witness_to_question = input("You have 6 witnesses, which one would you like to question for. (1-6): ")
            
        if witness_to_question in questioned_witnesses:
            print("You've already questioned this witness.")
            continue
        else:
            questioned_witnesses.append(witness_to_question)
            
        truth_or_lie = 'lies' if witness_to_question in liars else 'truths'
        witness_statement = random.choice(witnesses.get(witness_to_question)[truth_or_lie])
        total_questioned += 1
        print (f"\nWitness {witness_to_question} says, {witness_statement}")
            
    
    typewriter ("\nAfter questioning the witnesses & reviewing the information, It is time to figure out the liars, But You will only have 3 tries")
    
    correct_guesses = set()
    incorrect_guesses = set()
    
    chances = 3
    
    
    while len(correct_guesses) < 3 and len(incorrect_guesses) < chances:
        
        guess_the_liar = input("Enter the number of the witness that you think could be lying: ")
        
        if guess_the_liar not in witnesses:
            print("Invalid input. Please choose a valid witness number (1-6).")
            continue
            
        if guess_the_liar in correct_guesses or guess_the_liar in incorrect_guesses:
            print(f"You've already guessed Witness {guess_the_liar} {'correctly' if guess_the_liar in correct_guesses else 'incorrectly'}.")
        
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
        
        

scene_1()
scene_2()
start_game()
