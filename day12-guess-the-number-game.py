#Guessing Number Game
#無任何提示或提醒程式碼, 全靠目前為止所學完成

#Number Guessing Game Objectives:

# Include an ASCII art logo.
# Allow the player to submit a guess for a number between 1 and 100.
import random 
from art import logo_guess_number

# Include two different difficulty levels (e.g., 10 guesses in easy mode, only 5 guesses in hard mode).
EASY_MODE = 10
HARD_MODE = 5

def generateRandomNumber():
    guess_number = random.randint(1,100)
    print(guess_number)
    return guess_number

# Check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answer. 
def checkGuessNumber(userNumber,randomNumber):
    #0: too high
    #1: too low
    #2: Bingo
    # If they got the answer correct, show the actual answer to the player.
    if userNumber == randomNumber:
        return 2
    elif userNumber < randomNumber:
        return 1
    elif userNumber > randomNumber:
        return 0

# Track the number of turns remaining.
# If they run out of turns, provide feedback to the player. 
playAgain = True
def playGame():
    print(logo_guess_number)
    isGameFinish = False
    randomNumber = generateRandomNumber()
    gameLevel = int(input("Please input game level, easy model is 1, hard mode is 2: "))
    #define game level for easy or hard mode
    round = 1
    if gameLevel == 1:
        round = EASY_MODE
    elif gameLevel == 2:
        round = HARD_MODE
    else:
        round = HARD_MODE

    while not isGameFinish:    
        for count in range(1,round+1):
            userGuessNumber = int(input("Please enter a number from 1 to 100 to play guess number game: "))  
            guessResult = checkGuessNumber(userGuessNumber,randomNumber)

            if guessResult == 0:
                print(f"Round {count}, Guess number {userGuessNumber} is too high")
            elif guessResult == 1:
                print(f"Round {count}, Guess number {userGuessNumber} is too low")
            elif guessResult == 2:
                print(f"Round {count}, Guess number {userGuessNumber} Bingo. You Win")
                isGameFinish = True
                break
            #Guess chance out of use, lose the game
            if count == round:           
                print("You lose, finish Game~")
                isGameFinish = True
            count += 1

    continueGame = input("Do you want to play again? play again enter [Yes], otherwise enter [No]")
    if continueGame.lower() == "y" or continueGame.lower() == "yes":
        playGame()
    else:
        print("Game Over")

playGame()


