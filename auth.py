import os, requests, webbrowser, random, urllib, hashlib, base64, json, time
from dotenv import load_dotenv

class Auth():
    def __init__(self) -> None:
        self.client_id = "44f4f79135ee4d8883e443eb74bb17f6"
        self.redirect_uri = "http://127.0.0.1:5678/redirect"
        self.code_hashed = ""
        self.code_veri = ""
    
    def do_auth(self): #main function of this class!
        print("Now, I need you to grant me access to your Spotify account to download playlists.")
        time.sleep(3)
        
        self.code_veri = self.code_verifier() #generate code_verifier string (not hashed yet)
        self.code_hashed = self.code_challenge(self.code_veri) #generate code challenge, saved into self.
        self.get_authorize()
        time.sleep(5) #user need some time to grant access, make it another way
        self.load_json() #Get data from json file
        self.get_AccessToken()
        print("self.code_veri: " + self.code_veri + "\nself.code_hashed: " + self.code_hashed)
        return 
    
    def code_verifier(self):
        length = 128
        text = ""
        char_set = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789'
        for _ in range(length):
            text += char_set[random.randrange(len(char_set))]
        
        return text

    def code_challenge(self, code_verifier): #ONO TO FUNGUJEEEEE
        text_hashed = hashlib.sha256(code_verifier.encode()).digest()
        base64_bytes = base64.b64encode(text_hashed)
        base64_string = base64_bytes.decode('utf-8')
        urlsafe_base64_string = base64_string.replace('+', '-').replace('/', '_').rstrip('=')
        return urlsafe_base64_string
    
    def get_authorize(self): #last 1 hour, implement it!!
        url = 'https://accounts.spotify.com/authorize'
        params = {'redirect_uri': self.redirect_uri,
                   'response_type': "code",
                   'scope': "playlist-read-private user-library-read", 
                   'client_id': self.client_id,
                   #'show_dialog': "true", nejsem si jistý co tohle znamená xD
                   'code_challenge_method': "S256",
                   'code_challenge': self.code_hashed
                   }
        authUrl = url + "?" + urllib.parse.urlencode(params)
        print(authUrl) #test
        webbrowser.open(authUrl)
        
    def get_AccessToken(self):
        url = 'https://accounts.spotify.com/api/token'
        params = {'redirect_uri': self.redirect_uri,
                  'client_id': self.client_id,
                  'code_verifier': self.code_veri, #tohle se jebe
                  'grant_type': "authorization_code",
                  'code': self.args.get("args").get("code")}

        AccTokenUrl = url + "?" + urllib.parse.urlencode(params)
        print(AccTokenUrl)
        responseToken = requests.post(AccTokenUrl, headers={'Content-Type': 'application/x-www-form-urlencoded'}).json()
        print("Token: " + str(responseToken))
        #return responseToken.get("access_token")

    def load_json(self):
        with open('args.json', 'r') as f: 
            self.args = json.load(f)
        print(self.args)
   
