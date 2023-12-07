import requests
from track import Track
from helpingFunctions import make_windows_friendly


class SpotifyAPI():
    def __init__(self, token, yt_auth) -> None:
        self.token = token
        self.yt_auth = yt_auth
        self.auth_header = {"Authorization": "Bearer " + self.token}
        self.name: str
        self.number_of_tracks: int
        self.id_type: str

    def get_list_of_songs(self):
        self.id: str = self.get_id()
        self.request = self.request_spotify_api()
        self.name: str = make_windows_friendly(self.request["name"])
        self.number_of_tracks: int = self.request["tracks"]["total"]

        self.tracks: list[Track] = self.get_tracks()
        return self.tracks

    def get_id(self):
        self.url = input("Paste your url adress for playlist/album: ")
        # Before checking url, check if it's even url :D
        # (That means try request that url and see the response code)
        not_url = True
        while not_url:
            not_url = self.check_url()
        if self.id_type == "albums":
            return self.url[31:self.url.index("?")]
        else:
            return self.url[34:self.url.index("?")]

    def check_url(self):
        if not self.url.startswith("https://"):
            # adding https if not included
            self.url = "https://" + self.url
        try:
            test_request = requests.get(self.url).status_code
            if test_request == 200:
                if (self.url.startswith
                    ("https://open.spotify.com/playlist/")):
                    self.id_type = "playlists"
                    return False
                elif (self.url.startswith
                      ("https://open.spotify.com/album/")):
                    self.id_type = "albums"
                    return False
                else:
                    self.url = input(
                        "This URL adress isn't for Spotify playlist/album, "
                        + "please try it again: ")
                    return True
            return True

        except requests.exceptions.RequestException:
            self.url = input(
                "This URL adress isn't for Spotify playlist, "
                + "please try it again: ")

            return True

    def request_spotify_api(self):
        link: str = f'https://api.spotify.com/v1/{self.id_type}/' + self.id
        request: dict = requests.get(link, headers=self.auth_header).json()
        return request

    def get_tracks(self):
        offset: int = 0
        list_of_tracks: list[Track] = []
        number_of_items: int = self.number_of_tracks

        while number_of_items >= 0:
            link: str = (
                f'https://api.spotify.com/v1/{self.id_type}/'
                + self.id
                + '/tracks?limit=50&offset='
                + str(offset)
                )
            request: dict = requests.get(link, headers=self.auth_header).json()
            for i in range(len(request["items"])):
                if self.id_type == "playlists":
                    single_item: dict = request["items"][i]["track"]
                else:
                    single_item: dict = request["items"][i]
                list_of_tracks.append(Track(single_item, self.yt_auth, self.id_type, self.name))

            number_of_items -= 50
            offset += 50

        # get info and make Track objects placed in big list
        return list_of_tracks

# EduLint done
# mypy
