def load_playlist(filename):
    playlist = open(filename, "r")
    for line in playlist:
        line.split(",")
        return playlist
print(load_playlist("resources/beatles.txt"))