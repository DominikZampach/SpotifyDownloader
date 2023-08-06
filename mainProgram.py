import sys, requests
from publicPlaylist import PublicPlaylist
from privatePlaylist import PrivatePlaylist
from auth import Auth
import os
import subprocess
from app import Server

class MainProgram():
    def __init__(self) -> None:
        self.dir_path = os.path.dirname(os.path.realpath(__file__))
        self.info = {}
    
    def main(self):
        print("Welcome to my application for downloading Spotify playlists.\nI'm really happy you have chosen my application <3")
        Auth().get_auth()
        self.get_state_of_PL()
        
        if self.info["public"] == True:
            public = PublicPlaylist(self.info)
            self.info["songs"] = public.get_list_of_songs()
        else:
            private = PrivatePlaylist(self.info)
            self.info["songs"] = private.get_list_of_songs()
        
        #Now we have song names and author, so we can go and try to download them
        print(self.info)
        
    
    def get_state_of_PL(self):
        self.info["public"] = input("Do you want to download public (write 1) playlist or private (write 2): ")
        
        while self.info["public"] != "1" and self.info["public"] != "2": #Checking input
            self.info["public"] = input("Wrong input, please write 1 if you want to download public playlist\nor 2 if you want to download private playlist: ")
            
        if self.info["public"] == "1":
            self.info["public"] = True
        else:
            self.info["public"] = False


        if self.info["public"] == False: #when chosen playlist is private
            print("Not implemented yet")
            input()
            sys.exit()
    
    def run_batch(self, fileName):
        subprocess.call([f'{self.dir_path}\{fileName}'])
        
        
    
    
    
        
        