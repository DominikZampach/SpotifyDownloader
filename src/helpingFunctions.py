import os
import flask
import requests
import urllib
import googleapiclient
import yt_dlp
import contextlib

def make_windows_friendly(string):
    chars_to_replace = ["<", ">", ":", "\"", "/", "\\", "|", "?", "*"]
    for char in chars_to_replace:
        string = string.replace(char, "#")
    return string


def create_folder(folder_name, dir_path):
    new_folder = os.path.join(dir_path[0:len(dir_path)-4] +
                              "/downloaded_songs/" + folder_name)
    try:
        os.mkdir(new_folder)
    except FileExistsError:
        pass

def create_downloaded_songs_folder(dir_path):
    if not os.path.isdir("downloaded_songs"):
        downloaded_songs_folder = os.path.join(dir_path[0:len(dir_path)-4] + "/downloaded_songs")
        os.mkdir(downloaded_songs_folder)
        
def check_all_packages():
    try:
        print(flask.__version__)
        print(requests.__version__)
        print(urllib.__version__)
        print(googleapiclient.__version__)
        print(yt_dlp.__version__)
        print(contextlib.__version__)
    except:
        print("You don't have all packages, please download them with Package-download.bat\n" +
              "with administration privileges.")
        input()
        # Exit

# Edulint done
# MyPy
