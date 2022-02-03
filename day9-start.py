programming_dictionary = {
    "Bug": "An error in a program that prevents the program from running as expected.", 
    "Function": "A piece of code that you can easily call over and over again."}

#1. obtain dictionary value by key
print(programming_dictionary["Bug"])

#if key is not match in dictionary, python will report a KeyError 

#2. Add new item to dictionary
programming_dictionary["Lopp"] = "The action of doing something over and over again."

#3. Create an empty dictionary
empty_dictionary = {}

#4. Wipe an existing dictionary
#programming_dictionary = {}

#5.Loop through a dictionary
for key in programming_dictionary:
	print(key)
	print(programming_dictionary[key])