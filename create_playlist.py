import json
import requests
from secrets import spotify_user_id, spotify_token

class CreatePlaylist:

	def __init__(self):
		self.user_id = spotify_user_id
		self.spotify_token = spotify_token

	def get_youtube_client(self):
		pass

	def get_liked_videos(self):
		pass

	def create_playlist(self):
		request_body = json.dumps({
			"name": "YouTube Liked Videos",
			"descriptions": "All Liked YouTube Videos",
			"public": True
		})

		query = "https://api.spotify.com/v1/users/{self.user_id}/playlists"
		response = requests.post(
			query,
			data=request_body,
			headers={
				"Content-Type":"application/json",
				"Authorization":"Bearer {}".format(self.spotify_token)
			}
		)
		response_json = response.json()

		# playlist id
		return response_json["id"]

	def get_spotify_uri(self, song_name, artist):
		query = "https://api.spotify.com/v1/search"

		response = requests.get(
			query,
			headers={
				"Content-Type":"application/json",
				"Authorization":"Bearer {}".format(self.spotify_token)
			}
		)
		response_json = response.json()
		songs = response_json["tracks"]["items"]

	def add_song_to_playlist(self):
		pass