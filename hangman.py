import random

# Predefined words
words = ["python", "computer", "program", "coding", "developer"]

# Randomly select a word
word = random.choice(words)

# Game variables
guessed_letters = []
wrong_guesses = 0
max_wrong_guesses = 6

print("🎮 Welcome to Hangman!")
print("Guess the word one letter at a time.")
print("You have 6 incorrect guesses allowed.\n")

while wrong_guesses < max_wrong_guesses:

# Display current word
display_word = ""

for letter in word:
if letter in guessed_letters:
display_word += letter + " "
else:
display_word += "_ "

print("Word:", display_word)

# Check if word is completely guessed
if all(letter in guessed_letters for letter in word):
print("\n🎉 Congratulations! You guessed the word:", word)
break

# Take user input
guess = input("Enter a letter: ").lower()

# Validate input
if len(guess) != 1 or not guess.isalpha():
print("⚠️ Please enter only one letter.\n")
continue

# Check if already guessed
if guess in guessed_letters:
print("⚠️ You already guessed that letter.\n")
continue

guessed_letters.append(guess)

# Check the guess
if guess in word:
print("✅ Correct guess!\n")
else:
wrong_guesses += 1
print("❌ Wrong guess!")
print("Wrong guesses:", wrong_guesses, "/", max_wrong_guesses)
print()

else:
print("\n😢 Game Over!")
print("The word was:", word)