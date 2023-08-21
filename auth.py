import os, requests, webbrowser, random, urllib, hashlib, base64, json, time, datetime
from dotenv import load_dotenv

class Auth():
    def __init__(self) -> None:
        self.client_id = "44f4f79135ee4d8883e443eb74bb17f6"
        self.redirect_uri = "http://127.0.0.1:5678/redirect"
        self.code_hashed: str
        self.code_veri: str
        self.token: str
    
    def do_auth(self): #main function of this class!
        print("Now, I need you to grant me access to your Spotify account to download playlists.")
        time.sleep(3)
        
        self.code_veri = self.code_verifier() #generate code_verifier string (not hashed yet)
        self.code_hashed = self.code_challenge(self.code_veri) #generate code challenge, saved into self.
        self.get_authorize()
        time.sleep(5) #user need some time to grant access, make it another way
        self.load_json() #Get data from json file
        self.token = self.get_AccessToken()
        self.save_json()
        return 
    
    def check_user(self):
        """look if there is any login in the data.json newer than 1hour, if so, i can just use it and dont need authorization again
        """
        pass
    
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
                   'code_challenge_method': "S256",
                   'code_challenge': self.code_hashed
                   }
        authUrl = url + "?" + urllib.parse.urlencode(params)
        webbrowser.open(authUrl)
        
    def get_AccessToken(self):
        url = 'https://accounts.spotify.com/api/token'
        params = {'redirect_uri': self.redirect_uri,
                  'client_id': self.client_id,
                  'code_verifier': self.code_veri, #tohle se jebe
                  'grant_type': "authorization_code",
                  'code': self.data.get("args").get("code")}

        AccTokenUrl = url + "?" + urllib.parse.urlencode(params)
        print(AccTokenUrl)
        responseToken = requests.post(AccTokenUrl, headers={'Content-Type': 'application/x-www-form-urlencoded'}).json()
        return responseToken.get("access_token")

    def load_json(self):
        with open('data.json', 'r') as f: 
            self.data = json.load(f)
    
    def save_json(self):
        with open('data.json', 'w') as f:
            now = datetime.datetime.now()
            self.data["args"]["token"] = self.token
            self.data["args"]["token_expire_time"] = now.strftime("%H:%M")
            json_object = json.dumps(self.data, indent=4)
            f.write(json_object)
    
