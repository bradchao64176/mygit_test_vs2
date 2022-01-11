rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 
import random
you_choose=int(input("what do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors :"))
rock_paper_scissor = [0,1,2]
computer_choose = random.randint(0,len(rock_paper_scissor)-1) 
mylist = [rock,paper,scissors]

print(you_choose)
print(mylist[you_choose])
print("Computer choose")
print(mylist[computer_choose])

if you_choose == 0 and computer_choose == 1:
    print("You lose.")
elif you_choose == 0 and computer_choose == 2:
    print("You win")
elif you_choose == 1 and computer_choose == 0:
    print("You win")
elif you_choose == 1 and computer_choose == 2:
    print("You lose")    
elif you_choose == 2 and computer_choose == 0:
    print("You lose")
elif you_choose == 2 and computer_choose == 1:
    print("You win")
elif you_choose > 2 or you_choose < 0:
	print("Invalid number.")
else:
    print("the same")

