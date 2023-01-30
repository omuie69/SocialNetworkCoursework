"""
    Author: Mihai Morar
    Candidate number: 001235169-5
    Aim of the program:
"""

class SocialNetwork:
    def __init__(self):
        self.users = {}
    
    def add_user(self, name):
        self.users[name] = set()
    
    def add_friend(self, name, friend):
        if name not in self.users or friend not in self.users:
            print("Error: user not found.")
        else:
            self.users[name].add(friend)
    
    def recommend_friends(self, name):
        if name not in self.users:
            print("Error: user not found.")
        else:
            friends = self.users[name]
            recommendations = set()
            for friend in friends:
                for friend_of_friend in self.users[friend]:
                    if friend_of_friend != name and friend_of_friend not in friends:
                        recommendations.add(friend_of_friend)
            return recommendations

network = SocialNetwork()
name = input("Enter a name: ")
# Get the recommended friends for that user
print("Recommended friends for {}: {}".format(name, network.recommend_friends(name)))
