python_dictionary = {
    "Bug": "An error in a program that prevents the program from running as expected.",
    "Function": "A piece of code that you can easily call over and over again.",
    "Loop": "The action of doing something over and over again.",
    "Tuple": "A collection which is ordered and unchangeable. Allows duplicate members."
}
#retrieving items from dictionary
(python_dictionary["Bug"])

#Adding new items to dictionary
python_dictionary["Man"] = "A human being."

#create empty dictionary
empty_dictionary = {}

#wipe an existing dictionary
# python_dictionary = {} # here we are assigning an empty dictionary to the variable python_dictionary which will wipe the existing dictionary

#Edit an item in a dictionary
python_dictionary["Bug"] = "A moth in your computer."

#loop through a dictionary
for key in python_dictionary:
    print(key)
    print(python_dictionary[key]) # here we are printing the value of the key in the dictionary
    