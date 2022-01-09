import random
random_integer = random.randint(1,10)
print(random_integer)

#Generate a floating random number between 0 to 1
random_float = random.random()
print(random_float)

#How to generate 0 to 5? random_float times 5 (0 to 4.99999)
random_float = random.random() * 5
print(random_float)