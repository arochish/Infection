__author__ = 'Rochish'


''' User Object to display on the graph
    Constructor takes a name of the person
    and a number representing the frequency
    of KhanAcademy usage (0-3)
    Frequency will default to 1 if not specified
'''

class User:
    def __init__(self, name, frequency=1):
        self.name = name
        self.neighbors = []
        self.version = 1
        self.frequency = frequency

    def addNeighbor(self, neighbor):
        if neighbor is self or neighbor == self:
            return
        if neighbor not in self.neighbors:
            self.neighbors.append(neighbor)
        if self not in neighbor.neighbors:
            neighbor.addNeighbor(self)

    def getFrequency(self):
        return self.frequency

    def setVersion(self, version):
        self.version = version

    def hasNeighbors(self):
        return len(self.neighbors) != 0


class CoachingGraph:
    # default users list will be empty unless specified
    def __init__(self, users=[]):
        self.users = users

    def addUser(self, user):
        self.users.append(user)

    def removeUser(self, user):
        self.users.remove(user)

    def getUsersByFrequency(self, frequency) -> int:
        matched = []
        # return none for out of range frequency
        if frequency < 0 or frequency > 3:
            return None

        for user in self.users:
            if user.getFrequency() == frequency:
                matched.append(user)

        return matched

    # returns True if edge was successfully added, returns false otherwise
    def addEdge(self, user1, user2):
        if user1 not in self.users or user2 not in self.users:
            return False

        # check if users are already neighbors
        if user2 not in user1.neighbors:
            user1.addNeighbor(user2)
            return True
        # if they are, return false
        return False

    def getNeighbors(self, user) -> User:
        if user not in self.users:
            return None

        # index of element inside array
        userIndex = self.users.index(user)
        return self.users[userIndex].neighbors

    def listUsers(self):
        return self.users

    def getUserByName(self, name):
        for user in self.users:
            if user.name == name:
                return user
        return None
