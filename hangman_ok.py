import random

HANGMANPICS = ['''

  +---+
  |   |
      |
      |
      |
      |
=========''', '''

  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''

  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''

  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''

  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', '''

  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''

  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']

# ======כאן יש להוסיף אוסף של מילים=====
wordList = ["home"]


# ============כאן יכתבו הפונקציות=============

def displayBoard (HANGMANPICS, missedLetters, correctLetters,secretWord):
    str1 = ""
    print(HANGMANPICS[len(missedLetters)])
    if len(missedLetters) > 0:
        print("the missed letters are:")
        for k in missedLetters:
            print(k, end=" ")
    for j in secretWord:
        if j in correctLetters:
            str1 += j
        else:
           str1 += "_"

    print("\n",str1)


def getGuess(alreadyGussesed):
    ad = "you have guessed it, try another letter"
    letter = input("insert a letter:   ")
    if letter in alreadyGussesed:
        print(ad)
    if letter.isalpha() is False:
        print(ad)
    if len(letter) != 1:
        print(ad)
    return letter


def playAgain():
     x=input("would you like to play again?\n insert True or False")
     if x == 'true' or x == 'TRUE':
       return True

# ========כאן תחילת המשחק================

missedLetters = ''
correctLetters = ''
gameIsDone = False
secretWord = wordList[random.randint(0, len(wordList) - 1)]
while True:
    displayBoard(HANGMANPICS, missedLetters, correctLetters, secretWord)

    # המשתמש מקיש אות ובודקים אם זה תקין

    guess = getGuess(missedLetters + correctLetters)

    if guess in secretWord:
        correctLetters = correctLetters + guess

        # בדיקה אם השחקן ניצח
        foundAllLetters = True
        for i in range(len(secretWord)):
            if secretWord[i] not in correctLetters:
                foundAllLetters = False
                break
        if foundAllLetters:
            displayBoard(HANGMANPICS, missedLetters, correctLetters, secretWord)
            print('Yes! The secret word is "' + secretWord + '"! You have won!')
            gameIsDone = True
    else:
        missedLetters = missedLetters + guess

        # בדיקה האם השחקן הפסיד
        if len(missedLetters) == len(HANGMANPICS) - 1:
            displayBoard(HANGMANPICS, missedLetters, correctLetters, secretWord)
            print('You have run out of guesses!\nAfter ' + str(len(missedLetters)) + ' missed guesses and ' + str(
                len(correctLetters)) + ' correct guesses, the word was "' + secretWord + '"')
            gameIsDone = True

    # האם השחקן רוצה לשחק שוב?? 
    # אתחול המשתנים והמשחק מתחדש...
    if gameIsDone:
        if playAgain():
            missedLetters = ''
            correctLetters = ''
            gameIsDone = False
            secretWord = wordList[random.randint(0, len(wordList) - 1)]
        else:
            break
