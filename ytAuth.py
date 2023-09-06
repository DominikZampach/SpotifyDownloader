import googleapiclient.discovery
from google.oauth2 import credentials

class YTAuth():
    def __init__(self) -> None:
        self.creds = credentials.Credentials.from_authorized_user_file('config.json') #Maybe I will need to load that file, get only the usable things and replace the other things, like redirect_uri if it will be needed 💀
