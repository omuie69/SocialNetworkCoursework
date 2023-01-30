"""
    Author: Mihai Morar
    Candidate number: 001235169-5
    Aim of the program: user class with name and friends attributes while it allows the user to input their names and
                        who their friends are
"""

# Importing the SocialNetwork class
from SocialNetwork import SocialNetwork

# User class that inherits from the SocialNetwork class
class User(SocialNetwork):
    def __init__(self):
        # Call the init method of the parent class
        SocialNetwork.__init__(self)
        
        # Ask the user for their name
        name = input("Please enter your name: ")
        
        # Get the index of the user's name in the get_people list of the SocialNetwork class
        name_index = self.get_people().index(name)
        
        # Set the friends attribute of the User object to a list of the user's friends
        self.friends = self.get_friends()[name_index].split(',')
        
        # Set the name attribute of the User object to the user's name
        self.name = name
    
    # Method to return the number of friends the User object has
    def friends_amount(self):
        return len(self.friends)

# Create an object of the User class
obj = User()

# Call the friends_amount method of the User object
print(obj.friends_amount(),"friends.")
