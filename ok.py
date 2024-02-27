import time


def timew (message, delay = 0.1):
    for char in message:
        print (char, end='', flush = True)
        time.sleep(delay)
    print ()

timew ('wassup')