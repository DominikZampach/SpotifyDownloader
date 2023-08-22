import requests, time

class Playlist():
    def __init__(self) -> None:
        self.songs = {}
    
    def get_list_of_songs(self, token):
        self.get_playlist_id()
        #self.songs = self.get_playlist_items(self.token)
        #xxx, then return list of song names, maybe with author names
        #return self.songs
    
    def get_playlist_id(self): #Both for private/public playlists (pretty cool)
        self.info["urlPlaylist"] = input("Paste your url adress for playlist: ")
        #Before checking url, check if it's even url :D (That means try request that url and see the response code)
        notURL = True
        while notURL: 
            if not self.info["urlPlaylist"].startswith("https://"): #adding https if not included
                self.info["urlPlaylist"] = "https://" + self.info["urlPlaylist"]
            try:
                testRequest = requests.get(self.info["urlPlaylist"]).status_code
                if testRequest == 200 and self.info["urlPlaylist"].startswith("https://open.spotify.com/playlist/"):
                    notURL = False
                else:
                    self.info["urlPlaylist"] = input("This URL adress isn't for Spotify playlist, please try it again: ")
            except:
                self.info["urlPlaylist"] = input("Text isn't URL adress, please try it again: ")
        
        #here, the right Spotify playlist URL adress comes
        self.info["playlist_id"] = self.info["urlPlaylist"][34:self.info["urlPlaylist"].index("?")]
    
    def get_playlist_items(self, token):
        link = 'https://api.spotify.com/v1/playlists/' + self.info["playlist_id"]
        header = {"Authorization": "Bearer " + token}
        request = requests.get(link).content 
        return request