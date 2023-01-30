"""
    Author: Mihai Morar
    Candidate number: 001235169-5
    Aim of the program:
"""
import sys
from FileHandler import function
 
#create a variable that will hold the names of the users from the data file and the friends they have
users = function()

#create two lists that will split the names and the friends from the users variable
names = []
friends = []

#iterate over the users variable and split the names and the friends into the two lists
for user in users:
    name, friend = user.split(':')
    names.append(name)
    friends.append(friend)

#print(names)
#print(friends)

# Create a class called SocialNetwork

class SocialNetwork:
    #define a method that takes in names and friends lists as parameters, asks the user if they want to pretty print the file and if they do, it prints the names and the friends in a nice format
    def __init__(self, names, friends):
        self.names = names
        self.friends = friends
        answer = input("Would you like to pretty print the file? (y/n) ")
        if answer.lower() == "y":
            for i in range(len(names)):
                print(names[i], "has friends:", friends[i])
        elif answer.lower() == "n":
            print("Ok, the program will now exit.")
            sys.exit()
        else:
            print("Invalid input.")

#create an instance of the SocialNetwork class
network = SocialNetwork(names, friends)
print(network)
