import requests
from track import Track
from helpingFunctions import make_windows_friendly


class SpotifyAPI():
    def __init__(self, token, yt_auth) -> None:
        self.token = token
        self.yt_auth = yt_auth
        self.auth_header = {"Authorization": "Bearer " + self.token}
        self.playlist_name: str
        self.number_of_tracks: int

    def get_list_of_songs(self):
        self.playlist_id: str = self.get_playlist_id()
        self.request = self.request_spotify_api()
        self.playlist_name: str = make_windows_friendly(self.request["name"])
        self.number_of_tracks: int = self.request["tracks"]["total"]

        self.tracks: list[Track] = self.get_playlist_tracks()
        return self.tracks

    def get_playlist_id(self):
        self.playlist_url = input("Paste your url adress for playlist: ")
        # Before checking url, check if it's even url :D
        # (That means try request that url and see the response code)
        not_url = True
        while not_url:
            not_url = self.check_url()
        return self.playlist_url[34:self.playlist_url.index("?")]

    def check_url(self):
        if not self.playlist_url.startswith("https://"):
            # adding https if not included
            self.playlist_url = "https://" + self.playlist_url
        try:
            test_request = requests.get(self.playlist_url).status_code
            if test_request != 200 or not \
                (self.playlist_url.startswith
                    ("https://open.spotify.com/playlist/")):
                self.playlist_url = input(
                    "This URL adress isn't for Spotify playlist, "
                    + "please try it again: ")

                return True
            return False

        except requests.exceptions.RequestException:
            self.playlist_url = input(
                "This URL adress isn't for Spotify playlist, "
                + "please try it again: ")

            return True

    def request_spotify_api(self):
        link: str = 'https://api.spotify.com/v1/playlists/' + self.playlist_id
        request: dict = requests.get(link, headers=self.auth_header).json()
        return request

    def get_playlist_tracks(self):
        offset: int = 0
        list_of_tracks: list[Track] = []
        number_of_items: int = self.number_of_tracks

        while number_of_items >= 0:
            link: str = (
                'https://api.spotify.com/v1/playlists/'
                + self.playlist_id
                + '/tracks?limit=100&offset='
                + str(offset)
                )
            request: dict = requests.get(link, headers=self.auth_header).json()
            for i in range(len(request["items"])):
                single_item: dict = request["items"][i]["track"]
                list_of_tracks.append(Track(single_item, self.yt_auth))

            number_of_items -= 100
            offset += 100

        # get info and make Track objects placed in big list
        return list_of_tracks

# EduLint done
# mypy
