import sys, requests
from playlist import Playlist
from auth import Auth
import os, subprocess, time

class MainProgram():
    def __init__(self) -> None:
        self.dir_path = os.path.dirname(os.path.realpath(__file__))
        self.info = {}
    
    def main(self):
        print("Welcome to my application for downloading Spotify playlists.\nI'm really happy you have chosen my application <3")
        #Private or public status isnt needed
        
        self.pl = Playlist(self.info)
        self.info["songs"] = self.pl.get_list_of_songs()
        
        #Now we have song names and author, so we can go and try to download them
        print(self.info)
        
        
        
    
    
    
        
        