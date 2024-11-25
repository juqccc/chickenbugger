import time


def typewriter(message, delay=0.1, end=""):
    for char in message:
        print(char, end="", flush=True)
        time.sleep(delay)
    print(end, end="")


#-- GAME INTRO
typewriter("Welcome.....", delay=0.06)
time.sleep(1)
print("TO YOUR WORST NIGHTMARE!")
time.sleep(2)
typewriter("Press Enter To Continue", delay=0.05)
input()

while True:
    UserPlayingChoice = input(
        "Play The  Dream House (Press Y For Yes and N for No): "
    ).lower()
    if UserPlayingChoice == "y":
        print("Good Luck... Tip: Listen to the rules carefully")
        break

    elif UserPlayingChoice == "n":
        print("Exiting Game....")
        exit()

    else:
        print("Please enter a valid input")

typewriter("\n Press Enter To Continue", delay=0.05)
input()


#-- STORY INTRO
typewriter(
    "\n You were taken to a house with no memory of how you got there or who you are. There's 2 people with you; \n A man and a woman who seem like your parents. Their eyes are glowing and they won't stop smiling... "
)
print()
typewriter("\n Press Enter To Continue", delay=0.05)
input()

rules = [
    "Rule 1: Don't ever let motther and father know if you're scared"
    "Rule 2: Dont leave the house without permission"
    "Rule 3: When mother is working in the attic, dont talk to her"
    "Rule 4: If you hear crying coming from the attic, ignore it. Mother and father wll get angry"
    "Rule 5: Dont eat anything mother cooks after 8pm. The food isnt what it looks like"
    "Rule 6: If you remember who yoouu are, pretend you dont" 
    "Rule 7: Find a way to wake up...."  
    ]


typewriter("\n Press Enter To Continue", delay=0.05)
input()

#-- Game Starting Point
def story():
    typewriter ("You go downstairs and see father but he turned into a tall crreatre with black eyes and sharp teeth.\n The noises in the attic stopped; Mother heard you. YOU NEED TO HIDE")
choices 
print ("""1. Go back to your room and lock the door. 
       2. Go to the attic 
       3. Run Outside
""")
UserChoiceScene1 = int(input("Choose wisely...: "))

if 
