import random       #allows for the random picking of the get_shuffle function.
from playsound import playsound     #from the installed path of the playsound plugin I was able to
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
            mood_playlist[mood] = [song]        #a new list of (john) songs is created and that list contains the first (john) song.
    return mood_playlist

def get_shuffle(dlc_playlist):
    input_mood = input("What type of mood are you feelin'? ")
    random_song = ""
    if input_mood in dlc_playlist:
        random_song = random.choice(dlc_playlist[input_mood])
    else: 
        print("Please enter a valid input ")
    return random_song

def mood_shuffle(shuffle_song):
    playsound(shuffle_song)

playlist = load_playlist(input("What playlist would you like to listen to? "))
song = get_shuffle(playlist)
print(song)

mood_shuffle(song)
