import random

def choose_word(difficulty):
    words = {
        "easy": ["python", "game", "code", "play", "dog", "cat"],
        "medium": ["hangman", "computer", "programming", "player", "challenge", "solution"],
        "hard": ["intelligence", "algorithm", "development", "application", "optimization", "technology"]
    }

    return random.choice(words[difficulty])

def display_word(word, guessed_letters):
    displayed_word = ""
    for letter in word:
        if letter in guessed_letters:
            displayed_word += letter
        else:
            displayed_word += "_"
    return displayed_word

def draw_hangman(attempts):
    hangman_art = [
        """
            -----
            |   |
                |
                |
                |
                |
        -----------
        """,
        """
            -----
            |   |
            O   |
                |
                |
                |
        -----------
        """,
        """
            -----
            |   |
            O   |
            |   |
                |
                |
        -----------
        """,
        """
            -----
            |   |
            O   |
           /|   |
                |
                |
        -----------
        """,
        """
            -----
            |   |
            O   |
           /|\\  |
                |
                |
        -----------
        """,
        """
            -----
            |   |
            O   |
           /|\\  |
           /    |
                |
        -----------
        """,
        """
            -----
            |   |
            O   |
           /|\\  |
           / \\  |
                |
        -----------
        """
    ]
    return hangman_art[6 - attempts]

def hangman():
    print("Welcome to Hangman!")
    print("Try to guess the word.")

    play_again = True
    total_score = 0

    word_definitions = {
        "python": "A high-level programming language known for its readability and simplicity.",
        "hangman": "A classic word guessing game.",
        "computer": "An electronic device that processes data.",
        "programming": "The process of writing instructions for a computer to execute.",
        "game": "An activity with rules and goals, typically for entertainment.",
        "player": "A participant or contestant in a game or sport.",
        "code": "A system of symbols and rules used to represent instructions to a computer.",
        "challenge": "A task or problem that tests someone's abilities.",
        "intelligence": "The ability to acquire and apply knowledge and skills.",
        "algorithm": "A step-by-step procedure or formula for solving a problem.",
        "development": "The process of growth or formation.",
        "optimization": "The action of making the best or most effective use of a situation or resource.",
        "technology": "The application of scientific knowledge for practical purposes."
    }

    while play_again:
        difficulty = input("Choose difficulty level (easy/medium/hard): ").lower()
        while difficulty not in ["easy", "medium", "hard"]:
            print("Invalid difficulty level. Please choose from 'easy', 'medium', or 'hard'.")
            difficulty = input("Choose difficulty level (easy/medium/hard): ").lower()

        word = choose_word(difficulty)
        guessed_letters = []
        attempts = 6
        round_score = 0

        while True:
            print(draw_hangman(attempts))
            print("\nAttempts left:", attempts)
            displayed_word = display_word(word, guessed_letters)
            print("Word:", displayed_word)

            if "_" not in displayed_word:
                print("Congratulations! You've guessed the word:", word)
                round_score += attempts * len(word)
                total_score += round_score
                print("Round Score:", round_score)
                print("Total Score:", total_score)
                print("Word Definition:", word_definitions.get(word, "Definition not found."))
                break

            guess = input("Guess a letter: ").lower()
            if len(guess) != 1 or not guess.isalpha():
                print("Invalid input. Please enter a single letter.")
                continue

            if guess in guessed_letters:
                print("You already guessed that letter.")
                continue

            guessed_letters.append(guess)

            if guess not in word:
                print("Incorrect guess.")
                attempts -= 1
                if attempts == 0:
                    print("Sorry, you've run out of attempts. The word was:", word)
                    break
            else:
                print("Correct guess!")

        play_again_input = input("Do you want to play again? (yes/no): ").lower()
        if play_again_input != "yes":
            play_again = False

    print("Thanks for playing Hangman!")

hangman()
