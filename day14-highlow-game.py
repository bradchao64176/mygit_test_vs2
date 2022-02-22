from sqlalchemy import false
from art import *
from game_data import data
import random

def gameController():
    '''
        Operation action list below
        "displayScore":displayScore,
        "displayCompareInfo":displayCompareInfo,
        "displayAgainstInfo":displayAgainstInfo,
        "compareFollower":compareFollower
    '''
    #Init score set as 0
    score=0
    #2. Print your current score
    def displayScore():
        print(f"Current score: {score}")

    #3. Print compare A’s Name, Job description, Country
    def displayCompareInfo():
        '''
        For example,
        Game data information:
        'name': 'Maluma',
        'follower_count': 50,
        'description': 'Musician',
        'country': 'Colombia'
        '''
        idx = random.randint(1,len(data))
        info = data[idx]
        print(f'Compare A: {info["name"]}, {info["description"]}, from {info["country"]}')
        return info

    #5. Print Against B’s Name, Job description, Country
    def displayAgainstInfo():
        '''
        For example,
        Game data information:
        'name': 'Maluma',
        'follower_count': 50,
        'description': 'Musician',
        'country': 'Colombia'
        '''
        idx = random.randint(1,len(data))
        info = data[idx]
        print(f'Against B: {info["name"]}, {info["description"]}, from {info["country"]}')
        return info

    #6. Print Who has more followers? Type ‘A’ or ‘B’:
    def compareFollower(compareInfo, againstInfo,score):
        '''
        param1: compareInfo, object type is disctionary
        param2: againstInfo, object type is disctionary
        param3: current score
        '''
        Answer = input("Who has more followers? Type 'A' or 'B'? ")
        print(f"I guess answer is {Answer} ")
        print(f'Compare A follower number: {compareInfo["follower_count"]}')
        print(f'Against B follower number: {againstInfo["follower_count"]}')
        countA = compareInfo["follower_count"]
        countB = againstInfo["follower_count"]
 
        
        if Answer.lower() == "a" and countA > countB:
            score += 1
        elif Answer.lower() == "b" and countA < countB:
            score += 1
        return score
 
    
        #define operation function in dictionary
    OPERATE_FUNCTION ={
        "displayScore":displayScore,
        "displayCompareInfo":displayCompareInfo,
        "displayAgainstInfo":displayAgainstInfo,
        "compareFollower":compareFollower
    }
    #print(type(OPERATE_FUNCTION["displayScore"]))

    stopGame = False
    _compareInfo = {}
    _againstInfo = {}
    displayCompareInfo = OPERATE_FUNCTION["displayCompareInfo"]
  
    while not stopGame:
        #1. Load and print art logo of high low game
        print(logo_highlow_game)
        displayScore = OPERATE_FUNCTION["displayScore"]
        displayScore()

        #print assign againstInfo to compareInfo 
        if len(_compareInfo) == 0:
            _compareInfo = displayCompareInfo()
        else:
            print(f'Compare A: {_compareInfo["name"]}, {_compareInfo["description"]}, from {_compareInfo["country"]}')

        #4. Load and print art logo of vs.
        print(logo_highlow_game_vs)
        displayAgainstInfo = OPERATE_FUNCTION["displayAgainstInfo"]
        _againstInfo = displayAgainstInfo()

        compareFollower = OPERATE_FUNCTION["compareFollower"]
        scoreOfCompare = compareFollower(_compareInfo, _againstInfo, score)
        
        #print(f"current score: {scoreOfCompare}")
        #8. Continue game, if answer is right until you answer is fault.
        if scoreOfCompare <= score:
            print(f"Sorry, that's wrong. Final score: {scoreOfCompare} ")
            stopGame = True
        else:
        #7. Player can continue game and then to replace the compare A as B if going on next round
            _compareInfo = _againstInfo
        score = scoreOfCompare

gameController()


