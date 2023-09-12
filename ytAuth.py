from google.oauth2 import credentials
from google.oauth2 import auth

class YTAuth():
    #Vytvořit zde i ten guide jak to udělat (vlastní aplikace v google console, stáhnutí config.json, atd...)
    def __init__(self) -> None:
        pass

    def authorize(self):
        self.how_to_setup()
        self.creds = credentials.Credentials.from_authorized_user_file('config.json') 
        #Maybe I will need to load that file, get only the usable things and replace the other things, like redirect_uri if it will be needed 💀

        request = auth.authorize(self.creds)
        return request
    
    def how_to_setup(self):
        print("Do this and than, then press enter...")
        input()
        #like this