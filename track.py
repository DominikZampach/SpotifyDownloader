from googleapiclient.discovery import build
import yt_dlp
import os
import contextlib
from mainProgram import slugify_string


class Track():
    def __init__(self, item, api_key) -> None:
        self.youtube = build("youtube", "v3", developerKey=api_key)
        self.track_album: str = slugify_string(item["album"].get("name"))
        self.track_name: str = item.get("name")
        self.string_track_artist: str = ""
        number_of_artists: int = len(item["artists"])
        self.list_track_artist: list = []
        for i in range(number_of_artists):
            self.list_track_artist.append(item["artists"][i]["name"])

            if i == number_of_artists-1:
                self.string_track_artist += item["artists"][i]["name"]
            else:
                self.string_track_artist += item["artists"][i]["name"] + ", "

        self.url_youtube = "https://www.youtube.com/watch?v="
        if self.track_name == self.track_album:
            self.download_name = (
                f"{self.string_track_artist} - {self.track_name}")
        else:
            self.download_name = (f"{self.string_track_artist} - "
                                  + f"{self.track_name} ({self.track_album})")

        self.download_name = slugify_string(self.download_name)

    def url_of_track_on_YT(self):
        search_sentence = self.track_name
        for artist in self.list_track_artist:
            search_sentence += " " + artist
        response = self.youtube.search().list(
            part="snippet",
            maxResults=1,
            q=search_sentence
        ).execute()
        video_id = response["items"][0]["id"]["videoId"]
        return video_id

    def download_track(self, folder_name, dir_path):
        video_id = self.url_of_track_on_YT()
        url = self.url_youtube + video_id
        ydl_opts = {
            'outtmpl': f'downloaded_songs/{(folder_name)}'
            + f'/{self.download_name}',
            'format': 'bestaudio/best',
            'ffmpeg_location': (dir_path
                                + '/ffmpeg-6.0-essentials_build/bin'
                                + '/ffmpeg.exe'),
            # Path to FFmpeg inside SpotifyPlaylistDownloader
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
                'preferredquality': '192'
            }]
        }

        with open(os.devnull, 'w') as fnull, \
                contextlib.redirect_stdout(fnull), \
                contextlib.redirect_stderr(fnull):
            # This is for not getting any output into console from yt_dlp
            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                ydl.download([url])
        self.check_download(folder_name, dir_path)

    def check_download(self, folder_name, dir_path):
        folder = os.listdir(dir_path + '/downloaded_songs/' + folder_name)
        if self.download_name + ".mp3" in folder:
            print("Song named " + self.track_name + " downloaded.")
        else:
            print("Song named " + self.track_name + " cannot be downloaded.")

# EduLint done
# mypy
