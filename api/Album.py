

class Album:
    def __init__(self, id, name,img, artist, release_date, genre):
        self.id = id
        self.name = name
        self.img = img
        self.artist = artist
        self.release_date = release_date
        self.genre = genre

    def serialize(self):
        return {
            'id': self.id,
            'name': self.name,
            'artist': self.artist,
            'release_date': self.release_date,
            'genre': self.genre
        }