import os, requests, webbrowser, random, urllib.request, hashlib, base64, json, time
from dotenv import load_dotenv

class Auth():
    def __init__(self) -> None:
        self.client_id = "44f4f79135ee4d8883e443eb74bb17f6"
        self.code_hashed = "" #there will be stored hashed code from code_challenge
        self.code = ""
    
    def do_auth(self): #main function of this class!
        self.code = self.code_verifier() #generate code_verifier string (not hashed yet)
        self.code_hashed = self.code_challenge(self.code) #generate code challenge, saved into self.
        self.get_authorize()
        time.sleep(5) #user need some time to grant access, make it another way
        self.load_json() #Get data from json file
        self.get_AccessToken()
        print("self.code: " + self.code + "\nself.code_hashed: " + self.code_hashed)
        return 
    
    def code_verifier(self):
        text = ""
        length = random.randrange(43, 129)
        char_set = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789'
        for _ in range(length):
            text += char_set[random.randrange(len(char_set))]
        
        return text

    def code_challenge(self, code_verifier): #not working 💀
        code_verifier_bytes = code_verifier.encode()
        text_hash = hashlib.sha256(code_verifier_bytes).digest()
        text_hash = base64.b64encode(text_hash)
        return text_hash.decode()   
    
    def get_authorize(self):
        url = 'https://accounts.spotify.com/authorize' 
        redirect = "&redirect_uri=http://127.0.0.1:5678/redirect" 
        response_type = "&response_type=code" 
        scope = "&scope=playlist-read-private%20user-library-read" 
        show_dialog = "&show_dialog=true"
        code_challenge_method = "&code_challenge_method=S256"
        code_challenge = "&code_challenge=" + self.code_hashed
        authUrl = url + "?client_id=" + self.client_id + redirect + response_type + scope + show_dialog + code_challenge_method + code_challenge
        print(authUrl)
        webbrowser.open(authUrl)
        
    def get_AccessToken(self):
        url = 'https://accounts.spotify.com/api/token'
        client_id = "?client_id=" + self.client_id
        code_verifier = "&code_verifier=" + self.code
        grand_type = "&grant_type=authorization_code"
        code = "&code=" + self.args.get("args").get("code")
        redirect = "&redirect_uri=http://127.0.0.1:5678/redirect"
        AccTokenUrl = url + client_id + code_verifier + grand_type + code + redirect
        print(AccTokenUrl)
        responseJSON = requests.post(AccTokenUrl, headers={'Content-Type': 'application/x-www-form-urlencoded'}).json()
        print("Auth Token: " + str(responseJSON))
        #return responseJSON.get("AccessToken")

    def load_json(self):
        with open('args.json', 'r') as f: 
            self.args = json.load(f)
        print(self.args)
   
    #Tohle je v hajzlu 💀
