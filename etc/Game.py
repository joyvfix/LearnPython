# import random


# def guessing_game():
#     number = random.randint(1, 100)
#     attempts = 0

#     print("Welcome to the Guessing Game!")
#     print("I'm thinking of a number between 1 and 100.")

#     while True:
#         guess = int(input("Take a guess: "))
#         attempts += 1

#         if guess < number:
#             print("Too low!")
#         elif guess > number:
#             print("Too high!")
#         else:
#             print(
#                 f"Congratulations! You guessed the number in {attempts} attempts!")
#             break


# guessing_game()
# (;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;)
import random


def hangman():
    words = ["python", "hangman", "game", "openai", "coding"]
    word = random.choice(words).lower()
    guessed_letters = []
    tries = 6

    print("Welcome to Hangman!")
    print("Try to guess the word. You have 6 attempts.")

    while True:
        hidden_word = ""
        for letter in word:
            if letter in guessed_letters:
                hidden_word += letter
            else:
                hidden_word += "_"

        print(f"\nWord: {hidden_word}")
        print(f"Guessed letters: {', '.join(guessed_letters)}")
        print(f"Attempts left: {tries}")

        if hidden_word == word:
            print("Congratulations! You guessed the word correctly!")
            break

        if tries == 0:
            print("Game over! You ran out of attempts.")
            print(f"The word was: {word}")
            break

        guess = input("Guess a letter: ").lower()

        if len(guess) != 1 or not guess.isalpha():
            print("Invalid guess. Please enter a single letter.")
            continue

        if guess in guessed_letters:
            print("You already guessed that letter. Try again.")
            continue

        guessed_letters.append(guess)

        if guess in word:
            print("Correct guess!")
        else:
            print("Wrong guess!")
            tries -= 1


hangman()
