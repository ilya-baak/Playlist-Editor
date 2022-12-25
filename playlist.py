class Playlist(object):

    def __init__(self, name, ID):
        self.name = name
        self.ID = ID

    def __str__(self):
        return f"Playlist: {self.name}"

    def getName(self):
        return self.name

    def getID(self):
        return self.ID