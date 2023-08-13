import os, requests, webbrowser, random, urllib.request, hashlib, base64
from dotenv import load_dotenv

class Auth():
    def __init__(self) -> None:
        self.client_id = "44f4f79135ee4d8883e443eb74bb17f6"
        self.text_hash_base64 = ""
        #load_dotenv()
        #self.client_secret = os.getenv("SECRET")
    
    def do_auth(self):
        self.get_authorize()
        #main function of this class!
        pass
    
    def code_challenge(self):
        text = ""
        length = random.randrange(43, 129)
        char_set = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789_-.'
        for _ in range(length):
            text += char_set[random.randrange(len(char_set))]
        
        text_hash = hashlib.sha256(text.encode()).digest()
        self.text_hash_base64 = base64.b64encode(text_hash)
        return self.text_hash_base64
    
    def get_authorize(self):
        url = 'https://accounts.spotify.com/authorize' 
        redirect = "&redirect_uri=http://127.0.0.1:5678/redirect" 
        response_type = "&response_type=code" 
        scope = "&scope=playlist-read-private%20user-library-read" 
        show_dialog = "&show_dialog=true"
        code_challenge_method = "&code_challenge_method=S256"
        code_challenge = "&code_challenge=" + str(self.code_challenge())
        self.url = url + "?client_id=" + self.client_id + redirect + response_type + scope + show_dialog + code_challenge_method + code_challenge
        webbrowser.open(self.url)
        #Teď somehow vymyslet jakou redirect_uri používat abych se dostal ke query
        #UŽ VÍM, UDĚLAT LOCAL FLASK APLIKACI JEN NA TOTO (Flask API na localhost)!!
        
    def get_AccessToken(self):
        pass
    
   
    #Tohle je v hajzlu 💀
