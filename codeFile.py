import random

def choose_word():
    words = ["python", "hangman", "computer", "programming", "game", "player"]
    return random.choice(words)

def display_word(word, guessed_letters):
    displayed_word = ""
    for letter in word:
        if letter in guessed_letters:
            displayed_word += letter
        else:
            displayed_word += "_"
    return displayed_word

def hangman():
    word = choose_word()
    guessed_letters = []
    attempts = 6

    print("Welcome to Hangman!")
    print("Try to guess the word.")

    while True:
        print("\nAttempts left:", attempts)
        displayed_word = display_word(word, guessed_letters)
        print("Word:", displayed_word)

        if "_" not in displayed_word:
            print("Congratulations! You've guessed the word:", word)
            break

        guess = input("Guess a letter: ").lower()

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

hangman()
