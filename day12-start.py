#Local Scope
'''
def drink_potion():
    potion_strength = 2
    print(potion_strength)


drink_potion()
print(potion_strength)
'''

'''
#Global scope
player_health = 10
def drink_potion():
    potion_strength = 2
    print(player_health)

drink_potion()


'''
'''

player_health = 10
def game():
    def drink_potion():
        potion_strength = 2
        print(player_health)

    drink_potion()

print(player_health)
'''

#There is no Block Scope, this code is valid
#No closing function, it has Global scope
'''
if 3 > 1:
    a_variable = 10
    print(f"this is a_variable = {a_variable}")
print(f"this is a_variable = {a_variable}")

'''

game_level = 3
def create_enemy():
    enemies = ["Skeleton", "Zombie", "Alien"]
    #game_level = 10
    if game_level < 5:
        new_enemy = enemies[0]
    print(new_enemy)
    print(game_level)


create_enemy()


