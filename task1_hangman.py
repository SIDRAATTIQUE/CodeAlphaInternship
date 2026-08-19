import random

def run_hangman():
    # Predefined list of 5 words
    words = ["python", "codealpha", "developer", "program", "hangman"]
    secret_word = random.choice(words)
    
    guessed_letters = set()
    incorrect_guesses = 0
    max_incorrect = 6

    print("=== Welcome to Hangman! ===")
    
    while incorrect_guesses < max_incorrect:
        # Display current word state
        display_word = "".join([letter if letter in guessed_letters else "_" for letter in secret_word])
        print(f"\nWord: {' '.join(display_word)}")
        print(f"Incorrect attempts remaining: {max_incorrect - incorrect_guesses}")
        
        # Check win condition
        if "_" not in display_word:
            print("\nCongratulations! You guessed the word correctly!")
            break

        guess = input("Guess a letter: ").lower().strip()

        # Input validation
        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single valid letter.")
            continue

        if guess in guessed_letters:
            print("You already guessed that letter!")
            continue

        guessed_letters.add(guess)

        if guess in secret_word:
            print(f"Good job! '{guess}' is in the word.")
        else:
            print(f"Sorry, '{guess}' is not in the word.")
            incorrect_guesses += 1

    if incorrect_guesses == max_incorrect:
        print(f"\nGame Over! The word was: {secret_word}")

if __name__ == "__main__":
    run_hangman()