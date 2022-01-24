#Step1
from dis import dis
import random
from turtle import pos

word_list = ["ardvark","baboon","camel"]

#TODO1 -Randomly choose a word from the word_list and assign it to a variable called chosen_word
#For each letter in the chosen_word, add a "_" to 'display'.
#So if the chosen_word was "apple", display should be ["_", "_", "_", "_", "_"] with 5 "_" representing each letter to guess.

chosen_word = random.choice(word_list)
#create a empty list
display_word=[]

#for letter in range(0,len(chosen_word)):
#    display_word.append("_")

#TODO2 - Ask the user to guess a letter and assign their answer to a variable called guess. Make guess lowercase
#If the letter at that position matches "guess" then reveal that letter in the display at that position.
#e.g If the user guessed "p" and the chosen word was "apple", then display should be ["_","p","p","_","_"]
guess = input("Guess a letter: ").lower()
word_length=len(chosen_word)
for position in range(word_length):
    if chosen_word[position] == guess:
        display_word.append(guess)
    else:
        display_word.append("_")

#Test code
print(f"Psst, the solution is {chosen_word}")
print(f"represent display word: {display_word}")

#TODO3 - Check if the letter the user guessed (guess) is one of the leters in the chosen_word.

for letter in chosen_word:
    if letter == guess:
        print("Right")
    else:
        print("Wrong")


