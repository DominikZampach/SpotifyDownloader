from googleapiclient.discovery import build

class Track():
    def __init__(self, item, apiKey) -> None:
        self.youtube = build("youtube", "v3", developerKey=apiKey)
        self.track_album: str = item["album"].get("name")
        self.track_name: str = item.get("name")
        
        number_of_artists: int = len(item["artists"])
        self.track_artist: list = []
        for i in range(number_of_artists):
            self.track_artist.append(item["artists"][i]["name"])
    
    #def Vše, co je možné dělat s tracky (stahovat, ...)
    def url_of_track_on_YT(self):
        searchSentence = self.track_name
        for artist in self.track_artist:
            searchSentence += " " + artist
        print(searchSentence)
        response = self.youtube.search().list(
            part = "snippet",
            maxResults = 1,
            q = searchSentence
        ).execute()
        videoId = response["items"][0]["id"]["videoId"]
        return videoId

    def download_track(self):
        pass
    