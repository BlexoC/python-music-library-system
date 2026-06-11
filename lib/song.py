class Song:

    # --- Class Attributes ---
    count = 0
    genres = []
    artists = []
    genre_count = {}
    artists_count = {}

    def __init__(self, name, artist, genre):
        self.name = name
        self.artist = artist
        self.genre = genre

        Song.add_song_to_count()
        Song.add_to_genres(genre)
        Song.add_to_artists(artist)
        Song.add_to_genre_count(genre)
        Song.add_to_artists_count(artist)


    @classmethod
    def add_song_to_count(cls):
        cls.count += 1

    @classmethod
    def add_to_genres(cls, genre):
        if genre not in cls.genres:
            cls.genres.append(genre)

    @classmethod
    def add_to_artists(cls, artist):
        if artist not in cls.artists:
            cls.artists.append(artist)

    @classmethod
    def add_to_genre_count(cls, genre):
        if genre in cls.genre_count:
            cls.genre_count[genre] += 1
        else:
            cls.genre_count[genre] = 1

    @classmethod
    def add_to_artists_count(cls, artist):
        if artist in cls.artists_count:
            cls.artists_count[artist] += 1
        else:
            cls.artists_count[artist] = 1

s1 = Song("Halo", "Beyonce", "R&B")
s2 = Song("Crazy in Love", "Beyonce", "R&B")
s3 = Song("HUMBLE.", "Kendrick Lamar", "Rap")
s4 = Song("Alright", "Kendrick Lamar", "Rap")
s5 = Song("Bohemian Rhapsody", "Queen", "Rock")

print(Song.count)          # 5
print(Song.genres)         # ['R&B', 'Rap', 'Rock']
print(Song.artists)        # ['Beyonce', 'Kendrick Lamar', 'Queen']
print(Song.genre_count)    # {'R&B': 2, 'Rap': 2, 'Rock': 1}
print(Song.artists_count)  # {'Beyonce': 2, 'Kendrick Lamar': 2, 'Queen': 1}