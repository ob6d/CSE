"""
A general guide for Hangman
1. Make a word bank - 10 items, can be a list of movies or phrases  *
2. Pick an item from the list  *
3. Add a guess to the list of letters guessed
4. Reveal letters already guessed
5. Create the win and lose conditions
#guesses_left =
#letters_guessed = []
#output = ['']
"""
import random
word_bank = ["soccer", "Magic Mountain", "Edison High School", "Fresno Fair", "nike", "adidas", "Fashion Fair",
             "Regal Cinemas", "Dave and Busters", "New York City"]
guesses_left = 10
letters_guessed = []
randomWord = random.choice(word_bank)

# Ask for guess

while guesses_left > 0:
    # Building output
    guess = input("guess a letter")
    letters_guessed.append(guess)
    print(letters_guessed)
    print()
    output = []

    for letter in randomWord:
        if letter in letters_guessed:
            output.append(letter)

        if letters_guessed == randomWord:
            print("You win")

        else:
            output.append("*")

    # print(output)
    print("".join(output))