"""
    Author: Mihai Morar
    Candidate number: 001235169-5
    Aim of the program: user class with name and friends attributes while it allows the user to input their names and
                        who their friends are
"""

from NetworkClass import SocialNetwork

# user class with two attributes, name and friends, which are inputted by the user
class User(SocialNetwork):
    def __init__(self):
        SocialNetwork.__init__(self)
        name = input("Please enter your name: ")
        name_index = self.get_people().index(name)
        self.friends = self.get_friends()[name_index].split(',')
        self.name = name
    
    def friends_amount(self):
        return len(self.friends)

obj = User()
obj.friends_amount()
print(obj.friends_amount())
