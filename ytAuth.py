from google.oauth2 import credentials
from google_auth_oauthlib.flow import InstalledAppFlow

class YTAuth():
    def __init__(self) -> None:
        pass

    def authorize(self):
        self.how_to_setup()
        flow = InstalledAppFlow.from_client_secrets_file('config.json', ['https://www.googleapis.com/auth/youtube.readonly'])
        creds = flow.run_local_server()
        #Maybe I will need to load that file, get only the usable things and replace the other things, like redirect_uri if it will be needed 💀

        return creds
    
    def how_to_setup(self):
        print("Do this and than, then press enter...")
        input()
        #like this