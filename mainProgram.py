import os
from spotifyAPI import SpotifyAPI
from spotifyAuth import SpotifyAuth
from ytAuth import YTAuth
from helpingFunctions import create_folder


class MainProgram():
    def __init__(self) -> None:
        self.dir_path = os.path.dirname(
            os.path.realpath(__file__))  # path to this folder
        self.info = {}
        self.spot_auth = SpotifyAuth()
        self.yt_auth = YTAuth()

    def main(self):
        print("Welcome to my application for downloading Spotify playlists.")
        print("I'm really happy you have chosen my application <3")

        self.info["token"] = self.spot_auth.do_auth()
        self.api_key = self.yt_auth.authorize_api_key()
        self.spot_api = SpotifyAPI(self.info["token"], self.api_key)
        self.info["songs"] = self.spot_api.get_list_of_songs()

        create_folder(self.spot_api.playlist_name, self.dir_path)
        for song in self.info["songs"]:
            song.download_track(self.spot_api.playlist_name, self.dir_path)

    

# EduLint done
# mypy
