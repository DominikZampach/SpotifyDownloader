import requests, time
from track import Track

class SpotifyAPI():
    def __init__(self, token) -> None:
        self.token = token
        self.authHeader = {"Authorization": "Bearer " + self.token}
    
    def get_list_of_songs(self):
        self.playlist_id: str = self.get_playlist_id()
        self.playlist_name: str = self.get_playlist_name()
        self.tracks: list[Track] = self.get_playlist_tracks()
        print(self.tracks)
        print(self.playlist_name)
    
    def get_playlist_id(self): #Both for private/public playlists (pretty cool)
        self.playlistURL = input("Paste your url adress for playlist: ")
        #Before checking url, check if it's even url :D (That means try request that url and see the response code)
        notURL = True
        while notURL: 
            if not self.playlistURL.startswith("https://"): #adding https if not included
                self.playlistURL = "https://" + self.playlistURL
            try:
                testRequest = requests.get(self.playlistURL).status_code
                if testRequest == 200 and self.playlistURL.startswith("https://open.spotify.com/playlist/"):
                    notURL = False
                else:
                    self.playlistURL = input("This URL adress isn't for Spotify playlist, please try it again: ")
            except:
                self.playlistURL = input("Text isn't URL adress, please try it again: ")
        
        return self.playlistURL[34:self.playlistURL.index("?")] #returns playlist_id
    
    def get_playlist_name(self):
        link: str = 'https://api.spotify.com/v1/playlists/' + self.playlist_id
        request: dict = requests.get(link, headers=self.authHeader).json()
        return request["name"]
        
    
    def get_playlist_tracks(self):
        link: str = 'https://api.spotify.com/v1/playlists/' + self.playlist_id + '/tracks'
        request: dict = requests.get(link, headers=self.authHeader).json()
        #get info and make Track objects placed in big list
        return request

"""
JUST FOR TESTING
testToken = "Insert token here for testing"
test = SpotifyAPI(token)
test.get_list_of_songs()
"""