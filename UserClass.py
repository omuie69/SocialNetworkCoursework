"""
    Author: Mihai Morar
    Candidate number: 001235169-5
    Aim of the program: user class with name and friends attributes while it allows the user to input their names and
                        who their friends are
"""


# user class with two attributes, name and friends, which are inputted by the user


class User:
    def __init__(self):
        self.name = input("What is your name? ")
        self.friends = input("Who are your friends? (comma-separated) ").split(",")

    # used decorators `property` and `setter` to define getter and setter methods for the attributes

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value

    @property
    def friends(self):
        return self._friends

    @friends.setter
    def friends(self, value):
        self._friends = value
