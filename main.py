# We'll learn about how this line of code works later in the course - for now just know it loads the colored text
from colorama import Fore, Back, Style

# Function that prints out a letter with a colorful background
def printColorfulLetter(letter, isLetterInWord, isLetterInCorrectPlace = False):

  # If it's not in the word, display it with a red background
  if(not isLetterInWord):
    print(Back.RED + Fore.WHITE + f" {letter} ", end="")

  # If it's in the word...
  else:

    # ...and it's also in the right place, display it with a green background
    if(isLetterInCorrectPlace):
      print(Back.LIGHTGREEN_EX + Fore.WHITE + f" {letter} ", end="")  

    # ...but in the wrong place, display it with a yellow background
    else:
      print(Back.LIGHTYELLOW_EX + Fore.BLACK + f" {letter} ", end="")

# Display a guess, where each letter is color-coded by it's accuracy
def printGuessAccuracy(guess, actual):

  # Loop through each index/position 
  for index in range(6):

    # Grab the letter from the guess
    letter = guess[index]
    secret = actual[index]

    # Check if the letter at this index of the user's guess is in the secret word AT ALL or not
    if letter in actual:

      # If the letter is in the secret word, is it also AT THE CURRENT INDEX in the secret word?
      if(letter == secret):
        # Then print it out with a green background
        printColorfulLetter(letter, True, True)

      # If it's not at the current index, we know by this point in the code that it's still used in the secret word somewhere...
      else:
        # ...so we'll print it out with a yellow background
        printColorfulLetter(letter, True, False)
    # ...but if the letter is not in the word at all...
    else:
      # ...print it out with a red background
      printColorfulLetter(letter, False, False)
      
    # Don't worry about the line of code below, it works. It just handles the transition between colors
  print(Style.RESET_ALL + " ", end="")

# TO-DO: Write a Function that takes in a six-lettered word from the user
def getSixLetterWordFromUser():
  while True:
    guess = input("Enter a six lettered word: ")
    if len(guess) != 6:
      print("Must be exactly six letters long: ")
    else:
      return guess

# This marks the end of the function definitions, below this is where the program will actually start!
      
### Main Program ###

# TO-DO: Write the logic of the game here!
#Show the Game Title



print(r"""

▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄
██░███░█▀▄▄▀█░▄▄▀█░▄▀████░▄▄░█░██░▄▄▀█░██░
██░█░█░█░██░█░▀▀▄█░█░████░▀▀░█░██░▀▀░█░▀▀░
██▄▀▄▀▄██▄▄██▄█▄▄█▄▄█████░████▄▄█▄██▄█▀▀▀▄
▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀



""")
#Show the Game instruction 
print("Welcome to Word Play!")
print("=====================")
print("You have six tries to get the word correct")
print("The word is SIX CHARACTERS long, and you must enter a guess of this length")
print("If a letter is in the correct place, it will be green")
print("If a letter is in the word but NOT in the correct place, it will be yellow")
print("If the letter is not in the word, it will be red")


#define the word to guess
secret = 'python'

#set the maximum number of incorrect guesses allowed
maxIncorrectGuesses = 6

#initialize the incorrect guess counter
incorrectGuesses = 0

#

#loop until the word is guesses or the maximum number of incorrect guesses is read
guess = getSixLetterWordFromUser()
# While the user has not WON AND has not LOST
# WIN CONDITION: guess equal to the secret word
# LOSE CONDITION: user has as many incorrectGuesses as there are maxIncorrectGuesses
# If BOTH OF THESE are NOT TRUE, keep the loop going
while guess != secret and incorrectGuesses < maxIncorrectGuesses:
  guess = getSixLetterWordFromUser()
  
  

  # Display the user guess (first = user's guess, second = correct word - USE VARIABLES)
  printGuessAccuracy(guess, secret)

  # Did they guess incorrectly? (INCORRECTLY = THE GUESS IS NOT THE SECRET WORD)
  if guess != secret:
    # If they guessed incorrectly, increase the number of incorrect guesses by 1
    incorrectGuesses += 1

# We are UNINDENTED because the loop has ENDED...
# ... NOW we want to see if they won or not

# Check if the maximum number of incorrect guesses reached
if incorrectGuesses == maxIncorrectGuesses:
  print("Sorry you have reached your maximum attempts")

# Otherwise the user won!
if guess == secret:
  print("Congratulation! You won")
