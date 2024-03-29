from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from yt_dlp import YoutubeDL
from yt_dlp import utils
import os
import eyed3
import contextlib
from helpingFunctions import make_windows_friendly


class Track():
    def __init__(self, item, api_key, type_of_collection, name) -> None:
        self.youtube = build("youtube", "v3", developerKey=api_key)
        if type_of_collection == "albums":
            self.track_album = make_windows_friendly(name)
        else:
            self.track_album: str = make_windows_friendly(
                item["album"].get("name"))
        self.track_name: str = make_windows_friendly(item.get("name"))
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
                f"{self.track_name} - {self.string_track_artist}")
        else:
            self.download_name = (f"{self.track_name} - " +
                                  f"{self.string_track_artist} " +
                                  f"({self.track_album})")
        self.download_name = make_windows_friendly(self.download_name)

    def download_track(self, folder_name, dir_path):
        already_downloaded = self.check_download(folder_name, dir_path)
        if not already_downloaded:
            youtube_url = self.url_of_track_on_YT()
            self.yt_dpl_call(
                folder_name, dir_path, youtube_url)
            self.add_metadata(folder_name, dir_path)
        else:
            print(f"Song '{self.track_name}' already downloaded.")

    def add_metadata(self, folder_name, dir_path):
        mp3_file = f'{dir_path[0:len(dir_path)-4]}/downloaded_songs/{(folder_name)}/{self.download_name}.mp3'
        audiofile = eyed3.load(mp3_file)
        artists = self.string_track_artist.replace(", ", ";").replace(",", ";")
        audiofile.tag.artist = artists
        audiofile.tag.album = self.track_album
        audiofile.tag.save()
        
    def url_of_track_on_YT(self):
        search_sentence = self.track_name
        for artist in self.list_track_artist:
            search_sentence += " " + artist
        try:
            response = self.youtube.search().list(
                part="snippet",
                maxResults=1,
                q=search_sentence,
                type="video"
            ).execute()
        except HttpError as e:
            if e.resp.status == 403:
                print("You have exceeded your daily limit on Google Cloud.")
                print("You can continue tomorrow 😥")
                print(e)
                input()
            else:
                print("Unexpected error, please try it again or contact me.")
                input()
            exit()

        video_id = response["items"][0]["id"]["videoId"]
        return self.url_youtube + video_id

    def check_download(self, folder_name, dir_path):
        folder = os.listdir(dir_path[0:len(dir_path)-4] + '/downloaded_songs/' + folder_name)
        return self.download_name + ".mp3" in folder

    def yt_dpl_call(self, folder_name, dir_path, url):
        ydl_opts = {
            'outtmpl': f'{dir_path[0:len(dir_path)-4]}/downloaded_songs/{(folder_name)}'
            + f'/{self.download_name}',
            'format': 'bestaudio/best',
            'ffmpeg_location': (dir_path
                                + '/ffmpeg.exe'),
            # Path to FFmpeg inside SpotifyDownloader
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
                'preferredquality': '192'
            }]
        }

        try:
            with open(os.devnull, 'w') as fnull, \
                    contextlib.redirect_stdout(fnull), \
                    contextlib.redirect_stderr(fnull):
                # Not getting any output into console from yt_dlp
                with YoutubeDL(ydl_opts) as ydl:
                    ydl.download([url])

            print(f"Song '{self.track_name}' downloaded.")
        except utils.DownloadError:
            print("While downloading song named"
                  + f"'{self.track_name}' download error occured.")
        except utils.ExtractorError:
            print("While downloading song named"
                  + f"'{self.track_name}' extraction error occured.")
        except Exception:
            print("While downloading song named"
                  + f"'{self.track_name}' unexpected error occured.")

# EduLint done
# mypy
