class Song(object):

    def __init__(self, name, artist, ID):
        self.name = name
        self.artist = artist
        self.ID = ID

    def __str__(self):
        return f"Song: {self.name}, Artist: {self.artist}"

    def getName(self):
        return self.name

    def getArtist(self):
        return self.artist

    def getID(self):
        return self.ID

    def create_uri(self):
        return f"spotify:track:{self.ID}"



