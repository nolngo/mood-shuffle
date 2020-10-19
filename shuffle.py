import random       #allows for the random picking of the get_shuffle function.
from playsound import playsound     #from the installed path of the playsound plugin I was able to
def load_playlist(filename):        #this function opens the txt file for the purpose of reading it
    playlist = open(filename, "r")      
    mood_song = []
    mood_playlist = {}
    for line in playlist:       #This for loop reads line by line and splits the files by the comma.
        line = line.strip("\n")
        mood_song = (line.split(","))       #this list we brought in becomes a dictionary with the mood as the key and the song as the value.
        mood = mood_song[0]
        song = mood_song[1]
        if mood in mood_playlist:       #checking if mood(john) is already in a playlist, if it is
            mood_playlist[mood].append(song)        #get the rest of lists with (john) as mood, and append it with other (john) songs.
        else:       #else means that if john is not in the play list yet-
            mood_playlist[mood] = [song]        #a new list of (john) songs is created and that list contains the first (john) song.
    return mood_playlist

def get_shuffle(dlc_playlist):      #this random function randomly selects one song within a key that we use.
    input_mood = input("What catagory would you like to listen to? ")
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
