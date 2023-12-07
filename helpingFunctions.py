import os


def make_windows_friendly(string):
    chars_to_replace = ["<", ">", ":", "\"", "/", "\\", "|", "?", "*"]
    for char in chars_to_replace:
        string = string.replace(char, "#")
    return string


def create_folder(folder_name, dir_path):
    new_folder = os.path.join(dir_path +
                              "/downloaded_songs/" + folder_name)
    try:
        os.mkdir(new_folder)
    except FileExistsError:
        pass

def create_downloaded_songs_folder(dir_path):
    if not os.path.isdir("downloaded_songs"):
        downloaded_songs_folder = os.path.join(dir_path + "/downloaded_songs")
        os.mkdir(downloaded_songs_folder)
# Edulint done
# MyPy
