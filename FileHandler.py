""""
    Author: Mihai Morar
    Candidate number: 001235169-5
    Aim of the program: a basic file handler that separates the names from the friends from a txt file which is picked
                        by the user
"""

import os

path = 'C:/Users/serba/coursework'

# Get a list of all files in the directory
files = os.listdir(path)

# Iterate over the list of files
for file in files:
    # Get the full file path
    full_path = os.path.join(path, file)

    # Check if the file is a text file
    if os.path.isfile(full_path) and file.endswith('.txt'):
        # Print the name of the text file
        print(os.path.basename(full_path))


# function read_text_file with filepath as a parameter
def read_text_file(filepath):
    names = []
    friends = []
    # the function then tries to open a text file, if successful it will separate the names and their friends into two
    # different lists, the way it does this is by separating everything after ':' and classify it as friends
    try:
        with open(filepath, 'r') as file:
            for line in file:
                data = line.strip().split(':')
                names.append(data[0])
                friends.append(data[1:])
    # if the file is not found it prints an error message and then the program quits
    except FileNotFoundError:
        print(f"Error: the file {filepath} does not exist.")
        names = None
        friends = None
    return names, friends


# the function is being called with the filepath parameter with an input from the user

filepath = input('Please specify which text file you want to open')
names, friends = read_text_file(filepath)


# if there are names it will print out names and if there are friends it will print friends
if names is not None and friends is not None:
    print('These are the names of the people in the file', names)
    print('These are the friends of those people in order', friends)
