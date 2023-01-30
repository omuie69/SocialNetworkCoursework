"""
    Author: Mihai Morar
    Candidate number: 001235169-5
    Aim of the program:
"""
import sys
from FileHandler import function


# Create a class called SocialNetwork

class SocialNetwork:

    def __init__(self):
        users = function()

        names, friends = [], []
        for user in users:
            name, friend = user.split(':')
            names.append(name)
            friends.append(friend)

        self.names = names
        self.friends = friends
    
    def get_people(self):
        return self.names
    
    def get_friends(self):
        return self.friends

    #define a method that takes in names and friends lists as parameters, asks the user if they want to pretty print the file and if they do, it prints the names and the friends in a nice format
    def pretty_print(self):
        answer = input("Would you like to pretty print the file? (y/n) ").lower()
        if answer == "y":
            for i, v in enumerate(self.names):
                print(i)
                print(v, ":", self.friends[i])
        elif answer == "n":
            print("Ok, the program will now exit.")
            sys.exit()
        else:
            print("Invalid input.")
            self.pretty_print()

    #define a method that will allow the user to search for a name in the names list and if it is found, it will print the name and the friends of that name
    def friends_list(self, name):
        if name in self.names:
            print(name, "has friends:", self.friends[self.names.index(name)])
        else:
            print("Name not found.")
    
    #define a method that will allow the user to input whether or not they'd like to see another file from the directory
    def another_file(self):
        answer = input("Would you like to read another file? (y/n) ")
        if answer.lower() == "y":
            network = SocialNetwork()
            network.pretty_print()
            network.another_file()
        elif answer.lower() == "n":
            print("Ok, the program will now exit.")
            sys.exit()
        else:
            print("Invalid input.")

