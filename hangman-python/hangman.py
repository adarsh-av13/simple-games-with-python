import random
import pyfiglet
import string
from words import words
def get_valid_word(words):
    word = random.choice(words)
    while '-' in word or '-' in word:
        word = random.choice(words)
    return word


curWord = get_valid_word(words)
wordDisplay = "_ "*len(curWord)
heart = "\u2764\ufe0f"
usedLetters = set()
alphabet = set(string.ascii_lowercase)
mistakes = 0
header=pyfiglet.figlet_format("HANGMAN")

print(f"{header}")
print("lives left:", end=" ")
# for i in range(7):
print(f"{heart} "*7)
print(f"your word is {wordDisplay}")
while wordDisplay.replace(" ","") != curWord and mistakes!=7:
    letter = input("\nguess a letter(lowercase): ")
    if letter not in alphabet:
        print("You have entered an invalid character. Please enter only lowercase alphabets.")
        continue
    elif letter in usedLetters:
        print("You have guessed this letter already.")
    elif letter in curWord:
        start = 0
        usedLetters.add(letter)
        i = curWord.find(letter, start, len(curWord))
        listWord = list(wordDisplay)
        while(start<len(curWord) and i != -1):
            listWord[i*2] = letter
            start = start + 1
            i = curWord.find(letter, start, len(curWord))
        wordDisplay = "".join(listWord)
    else:
        usedLetters.add(letter)
        print("Incorrect Choice!")
        mistakes += 1
    print("\nlives left:", end=" ")
    print(f"{heart} " * (7-mistakes))
    print(f"letters used: {usedLetters}")
    print(wordDisplay)

if mistakes == 7:
    print(f"\nYou lost. The word was {curWord}")
else:
    print(f"\nYou won! You guessed the word {curWord}")