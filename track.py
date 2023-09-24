from googleapiclient.discovery import build
import yt_dlp
import os
import contextlib


class Track():
    def __init__(self, item, apiKey) -> None:
        self.youtube = build("youtube", "v3", developerKey=apiKey)
        self.track_album: str = item["album"].get("name")
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
        
        
        self.urlYouTube = "https://www.youtube.com/watch?v="
        if self.track_name == self.track_album:
            self.download_name = f"{self.string_track_artist} - {self.track_name}.mp3"
        else:
            self.download_name = f"{self.string_track_artist} - {self.track_name} ({self.track_album})"
        
        if "/" in self.download_name:
            self.download_name = self.download_name.replace("/", "-") #Securing not creating another folder 
    
    #def Vše, co je možné dělat s tracky (stahovat, ...)
    def url_of_track_on_YT(self):
        searchSentence = self.track_name
        for artist in self.list_track_artist:
            searchSentence += " " + artist
        print(searchSentence)
        response = self.youtube.search().list(
            part = "snippet",
            maxResults = 1,
            q = searchSentence
        ).execute()
        videoId = response["items"][0]["id"]["videoId"]
        return videoId

    def download_track(self, folder_name, dir_path):
        videoId = self.url_of_track_on_YT()
        url = self.urlYouTube + videoId
        print(url)
        ydl_opts = {
            'outtmpl': f'downloaded_songs/{folder_name}/{self.download_name}',
            'format': 'bestaudio/best',
            'ffmpeg_location': dir_path + '/ffmpeg-6.0-essentials_build/bin/ffmpeg.exe',
            #Path to FFmpeg inside SpotifyPlaylistDownloader
            'postprocessors': [{
                'key': 'FFmpegExtractAudio', 
                'preferredcodec': 'mp3',  
                'preferredquality': '192'
            }]
        }
        
        with open(os.devnull, 'w') as fnull, contextlib.redirect_stdout(fnull), contextlib.redirect_stderr(fnull): #This is for not getting any output into console from yt_dlp library
            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                ydl.download([url])
        
        '''
        Fix This
        
        folder = os.listdir(dir_path + '/downloaded_songs/' + folder_name)
        if self.download_name in folder:
            print("Song named " + self.track_name + " downloaded.")
        if self.download_name not in folder:
            print("Song named " + self.track_name + " cannot be downloaded.")'''

    