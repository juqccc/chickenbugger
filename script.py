import pyttsx3

def get_user_credentials():
    # Get user credentials
    login = input("Enter your login: ")
    password = input("Enter your password: ")
    return login, password

def authenticate_user(login, password):
    # For demonstration purposes, let's consider any login as valid
    return True

def main():
    # Initialize the text-to-speech engine
    engine = pyttsx3.init()

    # Get user credentials
    login, password = get_user_credentials()

    # Authenticate user
    if authenticate_user(login, password):
        # Welcome message
        welcome_message = f"Hi {login}, you have been logged in. Please have a good day!"
        print(welcome_message)

        # Convert the welcome message to speech
        engine.say(welcome_message)
        engine.runAndWait()
    else:
        # Authentication failed message
        authentication_failed_message = "Authentication failed. Please try again."
        print(authentication_failed_message)

        # Convert the authentication failed message to speech
        engine.say(authentication_failed_message)
        engine.runAndWait()

if __name__ == "__main__":
    main()
