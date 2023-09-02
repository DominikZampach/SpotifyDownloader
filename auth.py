import os, requests, webbrowser, random, urllib, hashlib, base64, json, time, datetime
from dotenv import load_dotenv

class Auth():
    def __init__(self) -> None:
        self.client_id = "44f4f79135ee4d8883e443eb74bb17f6"
        self.redirect_uri = "http://127.0.0.1:5678/redirect"
        self.code_hashed: str
        self.code_veri: str
        self.token: str
    
    def do_auth(self): #main function of this class!, WORKING
        self.load_json()
        if not self.logged_user():
            print("Now, I need you to grant me access to your Spotify account to download playlists.")
            time.sleep(3)
            
            self.code_veri = self.code_verifier() #generate code_verifier string (not hashed yet)
            self.code_hashed = self.code_challenge(self.code_veri) #generate code challenge, saved into self.
            self.get_authorize()
            self.load_json() #Get data from data.json
            self.token = self.get_AccessToken()
            self.save_json()
            return self.token
        else:
            #print("no API call, just pull from data.json")
            return self.data.get("token")
    
    def logged_user(self):
        """look if there is any login in the data.json newer than 1hour, if so, i can just use it and dont need authorization again
        """
        time_now = self.current_time_and_date()
        time_of_token_call = self.data.get("token_call_datetime")
        if time_of_token_call == None or time_of_token_call == "null":
            return False
        
        converted_time_now = self.time_converter(time_now)
        converted_time_of_token_call = self.time_converter(time_of_token_call)
        if converted_time_of_token_call + datetime.timedelta(minutes=55) < converted_time_now:
            return False
        
        
        header = {'Authorization': 'Bearer ' + self.data.get("token")}
        response = requests.get("https://api.spotify.com/v1/me", headers=header)
        responseStatus = response.status_code
        if responseStatus != 200:
            return False
        API_me = response.json()
        user_name = API_me.get("display_name")
        
        stay_at_this_acc = input(f"You have used this application recently, do you want to continue as {user_name} (type "'y'") or want to log into another account (type "'n'"): ").strip().lower()
        if stay_at_this_acc == "n":
            return False
        else:
            return True
            
    def current_time_and_date(self):
        now = datetime.datetime.now()
        return now.strftime("%Y/%m/%d/%H/%M")
    
    def time_converter(self, time: str):
        splitted_time = time.split("/")
        for i in range(len(splitted_time)):
            splitted_time[i] = int(splitted_time[i])
            
        datetime_object = datetime.datetime(*map(int, splitted_time))
        return datetime_object
    
    def code_verifier(self) -> str:
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
        time.sleep(3)
        print("After authorizing throught web browser, press Enter to continue...")
        input()
        
    def get_AccessToken(self):
        url = 'https://accounts.spotify.com/api/token'
        params = {'redirect_uri': self.redirect_uri,
                  'client_id': self.client_id,
                  'code_verifier': self.code_veri, #tohle se jebe
                  'grant_type': "authorization_code",
                  'code': self.data.get("code")}

        AccTokenUrl = url + "?" + urllib.parse.urlencode(params)
        print(AccTokenUrl)
        responseToken = requests.post(AccTokenUrl, headers={'Content-Type': 'application/x-www-form-urlencoded'}).json()
        print(responseToken)
        return responseToken.get("access_token")

    def load_json(self):
        with open('data.json', 'r') as f: 
            self.data = json.load(f)
    
    def save_json(self):
        with open('data.json', 'w') as f:
            self.data["token"] = self.token
            self.data["token_call_datetime"] = self.current_time_and_date()
            json_object = json.dumps(self.data, indent=4)
            f.write(json_object)
    
