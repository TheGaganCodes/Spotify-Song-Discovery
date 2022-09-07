import os

from spotify_client import SpotifyClient

#Callinf functions from spotify_client.py
def run():
	spotify_client = SpotifyClient(token)
	random_tracks = spotify_client.get_random_tracks() 
	track_ids = [tracks['id'] for tracks in random_tracks]
	#Adding generated random spotify tracks to your library
	was_added_to_library = spotify_client.add_tracks_to_library(track_ids)
	if was_added_to_library:
		for tracks in random_tracks:
			print(f"Added {tracks['name']} to your library") #Printing the names of the tracks added

#Initializing program
if __name__ == '__main__':
	run()