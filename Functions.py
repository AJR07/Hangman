import random
import os
import subprocess
import sys


def error(input, requirements):
    print(f"Ur input: {input} is Invalid. This is because: {requirements} ")


def generateWord(previousord, chosen):
    chosen = chosen.replace("\n", "")
    cwd = os.getcwd()
    os.chdir(f"{cwd}/Database")

    with open(chosen) as word:
        wordchosen = random.choice(list(word))

    wordchosen = wordchosen.replace("\n", "")
    return wordchosen


def separationLine():
    print(
        "---------------------------------------------------------------------------------"
    )


def enumChecker(lives):
    print("Current live counts:")
    print(Pictures[5 - lives])


def printWord(word):
    printtext = ""
    for i in word:
        printtext += i
        printtext += " "
    print(f"This is the current word {printtext}")


def move(word, guessedletters, lives, guessedword):
    printWord(guessedword)
    details = (
        []
    )  # 1. amount of letters guessed(non-unique), 2. letter guessed, 3, lives
    while True:
        if (random.randint(1, 10) < 5 and " " in word) and " " not in guessedletters:
            print(
                "BONUS HINT: This word has a ' '(space) in it, try guessing space to avoid losing lives :D"
            )
        chaguessed = input("Guess a letter:")
        if len(chaguessed) != 1:
            error(chaguessed, "only a single character is allowed")
        elif chaguessed in guessedletters:
            error(
                chaguessed,
                f"letter has been guessed before, here is your current list of guessed letters: {guessedletters}",
            )
        elif chaguessed.isalpha == False:
            error(chaguessed, "Hmm, it seems like ur input isn't an alphabet")
        else:
            if chaguessed in word:
                occurrences = str(word.count(chaguessed))
                details.append(occurrences)
                details.append(chaguessed)
                details.append(str(lives))
                print(
                    f"{chaguessed} is in the word! There were {occurrences} '{chaguessed}'s in the word!"
                )
                enumChecker(lives)

            else:
                details.append("0")
                details.append(chaguessed)
                details.append(str(lives - 1))
                print(
                    f"{chaguessed} is not in the word :(. 1 life has been lost, u currently have {lives-1} lives!"
                )
                enumChecker(lives - 1)

            break
    separationLine()
    return details


Pictures = [
    r"""
    +---+
    |   |
        |
        |
        |
        |
  =========""",
    r"""
    +---+
    |   |
    O   |
        |
        |
        |
  =========""",
    r"""
    +---+
    |   |
    O   |
    |   |
        |
        |
  =========""",
    r"""
    +---+
    |   |
    O   |
   /|   |
        |
        |
  =========""",
    r"""
    +---+
    |   |
    O   |
   /|\  |
        |
        |
  =========""",
    r"""
    +---+
    |   |
    O   |
   /|\  |
   /    |
        |
  =========""",
    r"""
    +---+
    |   |
    O   |
   /|\  |
   / \  |
        |
  =========""",
]
