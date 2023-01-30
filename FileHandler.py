""""
    Author: Mihai Morar
    Candidate number: 001235169-5
    Aim of the program: a basic file handler that separates the names from the friends from a txt file which is picked
                        by the user
"""

import os
import sys


def function():
    # Ask the user if they want to display the list of text files
    answer = input("Would you like to display the list of text files? (y/n) ")

    if answer.lower() == "y":
        # Get the current directory
        path = 'C:/Users/serba/OneDrive/Documents/GitHub/SocialNetworkCoursework'
        # Get a list of all files in the directory
        files = [f for f in os.listdir(path) if os.path.isfile(os.path.join(path, f))]
        while True:
            # Iterate over the files and print the ones that end with '.txt'
            for i, file in enumerate(files):
                if file.endswith(".txt"):
                    print(i+1, file)
            try:
                # Ask the user to pick a file
                choice = int(input("Which file would you like to read? Please enter the number: "))
                # Get the name of the file the user picked
                chosen_file = files[choice-1]
                # Open the text file for reading
                with open(chosen_file, 'r') as f:
                    lines = f.readlines()
                    # Iterate over the lines
                    for line in lines:
                        name, friends = line.strip().split(':')
                        friends = friends.strip()
                    return lines
                # Ask the user if they want to pick another file
                pick_another = input("Would you like to pick another file? (y/n) ")
                if pick_another.lower() == "n":
                    print("Ok, the program will now exit.")
                    sys.exit()
            except FileNotFoundError:
                # Handle the exception if the file is not found
                print("file not found")
            except ValueError:
                # Handle the exception if the user enters an invalid input
                print("Invalid input.")
    # Handle the case where the user doesn't want to display the list of text files
    elif answer.lower() == "n":
        print("Ok, the program will now exit.")
        sys.exit()
    else:
        print("Invalid input.")
        icup = function()
