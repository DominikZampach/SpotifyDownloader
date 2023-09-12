import requests, time
from track import Track

class SpotifyAPI():
    def __init__(self, token, ytAuth) -> None:
        self.token = token
        self.ytAuth = ytAuth
        self.authHeader = {"Authorization": "Bearer " + self.token}
        self.playlist_name: str
        self.number_of_tracks: int

    def get_list_of_songs(self):
        self.playlist_id: str = self.get_playlist_id()
        playlist_name_and_number_of_tracks: list = self.get_playlist_name_and_total_number_of_tracks()
        self.playlist_name, self.number_of_tracks  = playlist_name_and_number_of_tracks[0], playlist_name_and_number_of_tracks[1]
        self.tracks: list[Track] = self.get_playlist_tracks()
    
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
    
    def get_playlist_name_and_total_number_of_tracks(self):
        link: str = 'https://api.spotify.com/v1/playlists/' + self.playlist_id
        request: dict = requests.get(link, headers=self.authHeader).json()
        return [request["name"], request["tracks"]["total"]]

    def get_playlist_tracks(self):
        offset: int = 0
        list_of_tracks: list[Track] = []
        number_of_items: int = self.number_of_tracks
        
        while number_of_items >= 0:
            link: str = 'https://api.spotify.com/v1/playlists/' + self.playlist_id + '/tracks?limit=100&offset=' + str(offset)
            request: dict = requests.get(link, headers=self.authHeader).json()
            for i in range(len(request["items"])):
                single_item: dict = request["items"][i]["track"]
                list_of_tracks.append(Track(single_item, self.ytAuth))
            
            number_of_items -= 100
            offset += 100
            
        #get info and make Track objects placed in big list
        return list_of_tracks

"""
JUST FOR TESTING
testToken = "Insert token here for testing"
test = SpotifyAPI(token)
test.get_list_of_songs()
"""