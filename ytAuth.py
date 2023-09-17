'''from google.oauth2 import service_account
from google_auth_oauthlib.flow import InstalledAppFlow
import time, json'''

class YTAuth():
    def authorize_apiKey(self):
        self.how_to_setup_API_key()
        apiKey = self.get_api_key()
        return apiKey
    
    def how_to_setup_API_key(self):
        print("Do this and than, then press enter...")
        input()
    
    def get_api_key(self):
        with open('key.txt', 'r') as f: 
            text = f.read()
            if "key=" in text:
                data = text.split("key=")[1].strip()
                return data
    
    
    #Authorization via oauth 2.0, but it is useless, im not using any private data
    '''
    def authorize_oauth(self):
        self.how_to_setup_oauth()
        flow = InstalledAppFlow.from_client_secrets_file('config.json', ['https://www.googleapis.com/auth/youtube.readonly'])
        #time.sleep(3)
        creds = flow.run_local_server(authorization_prompt_message="After authorizing throught web browser, press Enter to continue...", success_message="You can leave this site and head back to the application.")
        input()
        
        return creds
        
    #self.youtube = build("youtube", "v3", credentials=creds) #creating api client via creds
    
    def how_to_setup_oauth(self):
        print("Do this and than, then press enter...")
        input()
        #like this
    
    
    '''