def list_songs(**songs):
    print(songs)
    print("Type is ", type(songs))

list_songs()
list_songs(adele_songs=["Hello", "Someone like you"], backstreet_boys_song=["Larger than life"], ed_sheeran_songs=["Beautiful", "Perfect", "Dance"])
