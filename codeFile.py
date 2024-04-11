import random

def choose_word():
    with open("words.txt", "r") as file:
        words = file.readlines()
    return random.choice(words).strip().lower()

def display_word(word, guessed_letters):
    displayed_word = ""
    for letter in word:
        if letter in guessed_letters:
            displayed_word += letter
        else:
            displayed_word += "_"
    return displayed_word

def hangman():
    print("Welcome to Hangman!")
    print("Try to guess the word.")
    
    play_again = True
    total_score = 0
    
    while play_again:
        word = choose_word()
        guessed_letters = []
        attempts = 6
        round_score = 0

        while True:
            print("\nAttempts left:", attempts)
            displayed_word = display_word(word, guessed_letters)
            print("Word:", displayed_word)

            if "_" not in displayed_word:
                print("Congratulations! You've guessed the word:", word)
                round_score += attempts * 10
                total_score += round_score
                print("Round Score:", round_score)
                print("Total Score:", total_score)
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

        play_again_input = input("Do you want to play again? (yes/no): ").lower()
        if play_again_input != "yes":
            play_again = False

    print("Thanks for playing Hangman!")

hangman()
