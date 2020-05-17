import json
import os

import google_auth_oauthlib.flow
import googleapiclient.discovery
import googleapiclient.errors
import requests
import youtube_dl

from secrets import spotify_user_id, spotify_token

class CreatePlaylist:

	def __init__(self):
		self.user_id = spotify_user_id
		self.spotify_token = spotify_token
		self.youtube_client = get_youtube_client()

	def get_youtube_client(self):
        # Disable OAuthlib's HTTPS verification when running locally.
        # *DO NOT* leave this option enabled in production.
		os.environ["OAUTHLIB_INSECURE_TRANSPORT"] = "1"

        api_service_name = "youtube"
        api_version = "v3"
        client_secrets_file = "client_secret.json"

        # Get credentials and create an API client
        scopes = ["https://www.googleapis.com/auth/youtube.readonly"]
        flow = google_auth_oauthlib.flow.InstalledAppFlow.from_client_secrets_file(
            client_secrets_file, scopes)
        credentials = flow.run_console()

        # from the Youtube DATA API
        youtube_client = googleapiclient.discovery.build(
            api_service_name, api_version, credentials=credentials)

        return youtube_client

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
		uri = response_json["tracks"]["items"]

	def add_song_to_playlist(self):
		pass