import sys, requests, os, subprocess, time
from playlist import Playlist
from auth import Auth

class MainProgram():
    def __init__(self) -> None:
        self.dir_path = os.path.dirname(os.path.realpath(__file__)) #path to this folder
        self.info = {}
        self.auth = Auth()
        self.pl = Playlist()
    
    def main(self):
        print("Welcome to my application for downloading Spotify playlists.\nI'm really happy you have chosen my application <3")
        #Private or public status isnt needed
        
        self.info["token"] = self.auth.do_auth()
        print(self.info["token"])
        #self.info["songs"] = self.pl.get_list_of_songs(self.info["token"])
        
        #Now we have song names and author, so we can go and try to download them
        
        
        
    
    
    
        
        