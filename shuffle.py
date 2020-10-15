def load_playlist(filename):
    playlist = open(filename, "r")
    mood_song = []
    mood_playlist = {}
    for line in playlist:
        line = line.strip("\n")
        mood_song = (line.split(","))
        mood = mood_song[0]
        song = mood_song[1]
        if mood in mood_playlist:       #checking if mood(john) is already in a playlist, if it is
            mood_playlist[mood].append(song)        #get the rest of lists with (john) as mood, and append it with other (john) songs.
        else:       #else means that if john is not in the play list yet-
            mood_playlist[mood] = [song]        #a new list of john songs is created and that list contains the first (john) song.
    return mood_playlist
print(load_playlist("beatles.txt"))