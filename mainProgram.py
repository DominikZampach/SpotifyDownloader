import sys, requests, os, subprocess, time
from spotifyAPI import SpotifyAPI
from auth import Auth

class MainProgram():
    def __init__(self) -> None:
        self.dir_path = os.path.dirname(os.path.realpath(__file__)) #path to this folder
        self.info = {}
        self.auth = Auth()
    
    def main(self):
        print("Welcome to my application for downloading Spotify playlists.\nI'm really happy you have chosen my application <3")
        
        self.info["token"] = self.auth.do_auth()
        self.SpotAPI = SpotifyAPI(self.info["token"])
        self.info["songs"] = self.SpotAPI.get_list_of_songs()
        
        #Now we have song names and author, so we can go and try to download them
        
        
        
        
        
    
    
    
        
        