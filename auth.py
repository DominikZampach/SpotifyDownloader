import os
from dotenv import load_dotenv
import requests
import webbrowser
import urllib.request

class Auth():
    def __init__(self) -> None:
        self.client_id = "44f4f79135ee4d8883e443eb74bb17f6"
        load_dotenv()
        self.client_secret = os.getenv("SECRET")
    
    def get_auth(self):
        url = 'https://accounts.spotify.com/authorize' 
        redirect = "&redirect_uri=https://open.spotify.com/" 
        response_type = "&response_type=code" 
        scope = "&scope=playlist-read-private%20user-library-read" 
        show_dialog = "&show_dialog=true" 
        self.url = url + "?client_id=" + self.client_id + redirect + response_type + scope + show_dialog
        webbrowser.open(self.url)
        #Teď somehow vymyslet jakou redirect_uri používat abych se dostal ke query
        #UŽ VÍM, UDĚLAT LOCAL FLASK APLIKACI JEN NA TOTO !!
        pass
   
    
   
    #Tohle je v hajzlu 💀