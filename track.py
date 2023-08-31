
class Track():
    def __init__(self, item) -> None:
        self.track_album: str = item["album"].get("name")
        self.track_name: str = item.get("name")
        
        number_of_artists: int = len(item["artists"])
        self.track_artist: list
        for _ in range(number_of_artists):
            self.track_artist.append(item["artists"].get("name"))
    
    #def Vše, co je možné dělat s tracky (stahovat, ...)