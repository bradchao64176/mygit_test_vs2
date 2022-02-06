############### Blackjack Project #####################

#Difficulty Normal 😎: Use all Hints below to complete the project.
#Difficulty Hard 🤔: Use only Hints 1, 2, 3 to complete the project.
#Difficulty Extra Hard 😭: Only use Hints 1 & 2 to complete the project.
#Difficulty Expert 🤯: Only use Hint 1 to complete the project.

############### Our Blackjack House Rules #####################

## The deck is unlimited in size. 
## There are no jokers. 
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.
## Use the following list as the deck of cards:
## cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.
## The computer is the dealer.

##################### Hints #####################

#Hint 1: Go to this website and try out the Blackjack game: 
#   https://games.washingtonpost.com/games/blackjack/
#Then try out the completed Blackjack project here: 
#   http://blackjack-final.appbrewery.repl.run

#Hint 2: Read this breakdown of program requirements: 
#   http://listmoz.com/view/6h34DJpvJBFVRlZfJvxF
#Then try to create your own flowchart for the program.

#Hint 3: Download and read this flow chart I've created: 
#   https://drive.google.com/uc?export=download&id=1rDkiHCrhaf9eX7u7yjM1qwSuyEk-rPnt

#Hint 4: Create a deal_card() function that uses the List below to *return* a random card.
#11 is the Ace.
import random
from tabnanny import check
def deal_card():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card_num = random.randint(0,len(cards)-1)    
    return cards[card_num]

#print(deal_card())

#Hint 5: Deal the user and computer 2 cards each using deal_card() and append().
user_cards = []
computer_cards = []

for card in range(2):
    mycard = deal_card()
    user_cards.append(mycard)
    mycard = deal_card()
    computer_cards.append(mycard)    

print(f"Your cards {user_cards}")
#print(computer_cards)

#Hint 6: Create a function called calculate_score() that takes a List of cards as input 
#and returns the score. 
#Look up the sum() function to help you do this.


def calculate_score(listOfCards):
#Hint 7: Inside calculate_score() check for a blackjack (a hand with only 2 cards: ace + 10) and return 0 instead of the actual score. 0 will represent a blackjack in our game.
    if len(listOfCards)==2 and sum(listOfCards) ==21:
        return 0
    else:
#Hint 8: Inside calculate_score() check for an 11 (ace). If the score is already over 21, remove the 11 and replace it with a 1. You might need to look up append() and remove().
        if sum(listOfCards) > 21 and 11 in listOfCards:
            #check if has ace
            listOfCards.remove(11)
            listOfCards.append(1)
        return sum(listOfCards)

#user_cards = [11,9,2]
#score = calculate_score(user_cards)
#print(user_cards)
#print(score)

#Hint 9: Call calculate_score(). If the computer or the user has a blackjack (0) or if the user's score is over 21, then the game ends.
user_score = calculate_score(user_cards)
computer_score = calculate_score(computer_cards)
if computer_score == 0 or user_score > 21:
    print(f"You lose, Game over. Your score is {user_score}, Computer's score is {computer_score}")

def check_score():
    user_score = calculate_score(user_cards)
    computer_score = calculate_score(computer_cards)
    if computer_score == 0 or user_score > 21:
        print(f"You lose, Game over. Your score is {user_score}, Computer's score is {computer_score}")
    else:
        print(user_cards)
        print(computer_cards)

#Hint 10: If the game has not ended, ask the user if they want to draw another card. If yes, then use the deal_card() function to add another card to the user_cards List. If no, then the game has ended.
def user_play():
    game_end = False
    while not game_end:
        wanted_card = input("Do you want another card? Y(es) or N(o)")
        if wanted_card.lower() == "yes" or wanted_card.lower() == "y":
            card = deal_card()
            user_cards.append(card)
#Hint 11: The score will need to be rechecked with every new card drawn and the checks in Hint 9 need to be repeated until the game ends.
        if sum(user_cards) < 17:
            card = deal_card()
            user_cards.append(card)
        else:
            game_end = True
        print(f"Your cards {user_cards}")
    return sum(user_cards)

def computer_play():
    game_end = False
    while not game_end:
        compute_score = sum(computer_cards)
        if  compute_score < 17:
            card = deal_card()
            computer_cards.append(card)
        elif computer_score > 17 and compute_score < 21:
            computer_wanted_card = ["Yes","No"][random.randint(0,1)]
            if compute_score < 21 and computer_wanted_card.lower() == "yes" or computer_wanted_card.lower() == "y":
                card = deal_card()
                computer_cards.append(card)
        else:
            game_end = True
        print(f"Computer's cards {computer_cards}")
    return sum(computer_cards)

user_score = user_play()
#Hint 12: Once the user is done, it's time to let the computer play. The computer should keep drawing cards as long as it has a score less than 17.
computer_score = computer_play()    
check_score()

#Hint 13: Create a function called compare() and pass in the user_score and computer_score. If the computer and user both have the same score, then it's a draw. If the computer has a blackjack (0), then the user loses. If the user has a blackjack (0), then the user wins. If the user_score is over 21, then the user loses. If the computer_score is over 21, then the computer loses. If none of the above, then the player with the highest score wins.
def compare(t_user_score,t_computer_score):
    if t_user_score > 21:
        print(f"Your score is {t_user_score}, this game is You lose.")
    elif t_computer_score > 21:
        print(f"Your score is {t_user_score}, Computer's score is {t_computer_score}, this game is You win.")
    elif t_user_score == t_computer_score:
        print(f"Your score is {t_user_score}, Computer's score is {t_computer_score}, this game is Draw.")
    elif t_computer_score == 0 or t_computer_score == 21:
        print(f"Your score is {t_user_score}, Computer's score is {t_computer_score}, this game is Computer win.")
    elif t_user_score == 0 or t_user_score == 21:
        print(f"Your score is {t_user_score}, Computer's score is {t_computer_score}, this game is You win.")
    elif t_user_score > 21:
        print(f"Your score is {t_user_score}, Computer's score is {t_computer_score}, this game is Computer win.")
    elif t_computer_score > 21:
        print(f"Your score is {t_user_score}, Computer's score is {t_computer_score}, this game is You win.")
    elif t_computer_score > t_user_score:
        print(f"Your score is {t_user_score}, Computer's score is {t_computer_score}, this game is Computer win.")
    else:
        print(f"Your score is {t_user_score}, Computer's score is {t_computer_score}, this game is You win.")


compare(user_score,computer_score)
#Hint 14: Ask the user if they want to restart the game. If they answer yes, clear the console and start a new game of blackjack and show the logo from art.py.
