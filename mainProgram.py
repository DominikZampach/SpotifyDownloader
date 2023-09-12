import sys, requests, os, subprocess, time
from spotifyAPI import SpotifyAPI
from spotifyAuth import SpotifyAuth
from ytAuth import YTAuth

class MainProgram():
    def __init__(self) -> None:
        self.dir_path = os.path.dirname(os.path.realpath(__file__)) #path to this folder
        self.info = {}
        self.SpotAuth = SpotifyAuth()
        self.YTAuth = YTAuth()
    
    def main(self):
        print("Welcome to my application for downloading Spotify playlists.\nI'm really happy you have chosen my application <3")
        #Here, I will need to add way to get the user create his own google application and use it for API calls
        
        self.info["token"] = self.SpotAuth.do_auth()
        self.info["yt_request"] = self.YTAuth.authorize()
        self.SpotAPI = SpotifyAPI(self.info["token"])
        self.info["songs"] = self.SpotAPI.get_list_of_songs()
        for song in self.info["songs"]:
            """Here, i will download every fuckin song in the list by using Track.download_track() func"""
            pass
        #Now we have song names and author, so we can go and try to download them
        
        
        
        
        
    
    
    
        
        