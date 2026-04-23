import random

# Step 1: Word list
words = ["apple", "tiger", "chair", "robot", "plant"]

# Step 2: Random word selection
word = random.choice(words)

# Step 3: Game setup
guessed_letters = []
attempts = 6
display = ["_"] * len(word)

print("Welcome to Hangman Game!")

# Step 4: Game loop
while attempts > 0 and "_" in display:
    print("\nWord:", " ".join(display))
    
    guess = input("Enter a letter: ").lower()

    # Check if already guessed
    if guess in guessed_letters:
        print("You already guessed that letter.")
        continue

    guessed_letters.append(guess)

    # Check correct or wrong guess
    if guess in word:
        print("Correct guess!")
        for i in range(len(word)):
            if word[i] == guess:
                display[i] = guess
    else:
        attempts -= 1
        print("Wrong guess! Attempts left:", attempts)

# Step 5: Result
if "_" not in display:
    print("\nCongratulations! You won. The word was:", word)
else:
    print("\nGame Over! The word was:", word)