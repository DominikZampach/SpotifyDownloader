import requests
import webbrowser
import random
from urllib import parse
import hashlib
import base64
import json
import time
import datetime


class SpotifyAuth():
    def __init__(self) -> None:
        self.client_id: str = "44f4f79135ee4d8883e443eb74bb17f6"
        self.redirect_uri: str = "http://127.0.0.1:5678/redirect"
        self.code_hashed: str
        self.code_veri: str
        self.token: str

    def do_auth(self):  # main function of this class!
        self.load_json()
        if not self.logged_user():
            print(
                "Now, I need you to grant me access to your Spotify "
                + "account to download playlists.")
            time.sleep(3)

            self.code_veri = self.code_verifier()
            self.code_hashed = self.code_challenge(self.code_veri)
            self.get_authorize()
            self.load_json()
            self.token = self.get_access_token()
            self.save_json()
            return self.token
        return self.data.get("token")

    def logged_user(self):
        """
        look if there is any login in the data.json newer than 1hour,
        if so, i can just use it and dont need authorization again
        """

        time_now = self.current_time_and_date()
        time_of_token_call = self.data.get("token_call_datetime")
        if time_of_token_call is None or time_of_token_call == "null":
            return False

        converted_time_now = self.time_converter(time_now)
        converted_time_of_token_call = self.time_converter(time_of_token_call)
        if (
            converted_time_of_token_call
            + datetime.timedelta(minutes=55) < converted_time_now
                ):
            return False

        header = {'Authorization': 'Bearer ' + self.data.get("token")}
        response = requests.get(
            "https://api.spotify.com/v1/me",
            headers=header
            )
        response_status = response.status_code
        if response_status != 200:
            return False
        api_me = response.json()
        user_name = api_me.get("display_name")

        stay_at_this_acc = input(
            "You have used this application recently, do you want to "
            + f"continue as {user_name} (type "'y'") or want to log into "
            + "another account (type "'n'"): "
            ).strip(
            ).lower()
        return not stay_at_this_acc == "n"

    def current_time_and_date(self):
        datetime_now = datetime.datetime.now()
        return datetime_now.strftime("%Y/%m/%d/%H/%M")

    def time_converter(self, time: str):
        splitted_time = time.split("/")
        for i in range(len(splitted_time)):
            splitted_time[i] = int(splitted_time[i]) # type: ignore

        datetime_object = datetime.datetime(*map(int, splitted_time)) # type: ignore
        return datetime_object

    def code_verifier(self) -> str:
        length = 128
        text = ""
        char_set = ("ABCDEFGHIJKLMNOPQRSTUVWXYZ"
                    + "abcdefghijklmnopqrstuvwxyz0123456789")
        for _ in range(length):
            text += char_set[random.randrange(len(char_set))]

        return text

    def code_challenge(self, code_verifier):
        text_hashed = hashlib.sha256(code_verifier.encode()).digest()
        base64_bytes = base64.b64encode(text_hashed)
        base64_string = base64_bytes.decode('utf-8')
        urlsafe_base64_string = base64_string.replace(
            '+', '-').replace('/', '_').rstrip('=')
        return urlsafe_base64_string

    def get_authorize(self):
        url = 'https://accounts.spotify.com/authorize'
        params = {
                    'redirect_uri': self.redirect_uri,
                    'response_type': "code",
                    'scope': "playlist-read-private user-library-read",
                    'client_id': self.client_id,
                    'code_challenge_method': "S256",
                    'code_challenge': self.code_hashed
                }
        auth_url = url + "?" + parse.urlencode(params)
        webbrowser.open(auth_url)
        time.sleep(3)
        print(
            "After authorizing throught web browser, "
            + "press Enter to continue..."
            )
        input()

    def get_access_token(self):
        url = 'https://accounts.spotify.com/api/token'
        params = {'redirect_uri': self.redirect_uri,
                  'client_id': self.client_id,
                  'code_verifier': self.code_veri,
                  'grant_type': "authorization_code",
                  'code': self.data.get("code")}

        acc_token_url = url + "?" + parse.urlencode(params)
        response_token = requests.post(
            url=acc_token_url,
            headers={'Content-Type': 'application/x-www-form-urlencoded'}
            ).json()
        return response_token.get("access_token")

    def load_json(self):
        # Get data from JSON
        with open('data.json', 'r') as f:
            self.data = json.load(f)

    def save_json(self):
        # Save data into JSON
        with open('data.json', 'w') as f:
            self.data["token"] = self.token
            self.data["token_call_datetime"] = self.current_time_and_date()
            json_object = json.dumps(self.data, indent=4)
            f.write(json_object)

# EduLint done
# mypy
