import time

def typewriter(message, delay=0.1, end=''):
    for char in message:
        print(char, end='', flush=True)
        time.sleep(delay)
    print(end, end='')  # Print the newline character only if end is provided

# INTRO
typewriter("Welcome", end=' ')
time.sleep(1)  # Add a pause of 1 second
typewriter("TO YOUR WORST NIGHTMARE!", end='\n')  # Newline only for this call
