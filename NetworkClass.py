"""
    Author: Mihai Morar
    Candidate number: 001235169-5
    Aim of the program:
"""

class SocialNetwork:
    def __init__(self):
        self.connections = {}
        self.common_friends = {}
        self.members = set()

    def add_connection(self, member1, member2):
        """Add a connection between two members."""
        self.members.add(member1)
        self.members.add(member2)
        if member1 in self.connections:
            self.connections[member1].add(member2)
        else:
            self.connections[member1] = {member2}
        if member2 in self.connections:
            self.connections[member2].add(member1)
        else:
            self.connections[member2] = {member1}

    def generate_common_friends(self):
        """Generate the common_friends structure."""
        for member1 in self.members:
            for member2 in self.members:
                if member1 == member2:
                    continue
                common_friends = self.connections[member1].intersection(self.connections[member2])
                self.common_friends[(member1, member2)] = len(common_friends)

    def recommend_friend(self, member):
        """Recommend a friend for a member."""
        friend = None
        max_common_friends = -1
        for other_member, common_friends in self.common_friends.items():
            if member in other_member and common_friends > max_common_friends and other_member[0] != other_member[1]:
                friend = other_member[0] if other_member[1] == member else other_member[1]
                max_common_friends = common_friends
        return f"Recommended friend for {member} is {friend}" if friend else f"Recommended friend for {member} is none"



# Create an instance of the SocialNetwork class
network = SocialNetwork()

# Add connections between members
network.add_connection("Adam", "Bob")
network.add_connection("Adam", "Mia")
network.add_connection("Adam", "Amir")
network.add_connection("Bob", "Zia")
network.add_connection("Mia", "Amir")

# Generate the common_friends structure
network.generate_common_friends()

# Recommend a friend for a member
print(network.recommend_friend("Mia"))
print(network.recommend_friend("Bob"))
