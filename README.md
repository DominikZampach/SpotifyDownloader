
# SpotifyDownloader

> Program for downloading Spotify playlists or albums locally into your PC

## Table of contents
- [Description](#description)
- [Requirements](#requirements)
- [How to setup SpotifyDownloader](#how-to-setup-spotifydownloader)
  - [Download](#download)
  - [Google key](#google-key)
  - [Downloading packages](#downloading-packages)
 - [How to actually use SpotifyDownloader](#how-to-actually-use-spotifydownloader)
 - [Limitations](#limitations)
 - [Legality statement](#legality-statement)

## Description
This program is simple CLI Python script, that takes URL of Spotify playlist/album and download it locally into your PC. It's using Spotify API to get informations about songs, then it's searching for these songs on YouTube via Google YouTube API and then downloading best match with yt_dlp.

## Requirements

 - Python 3.10 or newer (https://www.python.org/downloads/)
 - Spotify Account (Program will need to login to your Spotify account)
 - Google Account for YouTube API key

## How to setup SpotifyDownloader
### Download
If you've never used GitHub or Git, click on the "Code" button and select Download ZIP. After downloading, just extract it and you are ready for next step.

If you know how to use Git, you can just simply clone this repository into your computer.

### Google key
First of all, you will need to get API key for YouTube search. Go to this website: (https://console.cloud.google.com/), login here and choose New project.

After choosing name, click Create and go to "APIs and services" and then to "Credentials". Or you can go here by clicking this URL (https://console.cloud.google.com/apis/credentials).

Here, click "Create credentials", choose API key and create it. Now, you will see API key 1. Click on "SHOW KEY" and copy the key.

Take this key and open file named key.txt in folder with program. Paste this key after `key=` and you are ready to go to the next part.

*(Congratulations, you managed to do the hardest part of all 😄.)*

### Downloading packages
If you are using this program for the first time, you will need to download Python packages for this script to work. Simply open "Packages.bat" file and let the script download everything for you.

After downloading will end, you can close this script and ready to go using program ♥.

## How to actually use SpotifyDownloader
To run the main script, you need to open "SpotifyDownloader.bat".

After opening it, it will ask you to login into your Spotify account. It will also open URL for login in your default web browser. After logging in, you have to press Enter in script and go to the next step.

Now, it's time for Spotify URL. This program can take any album or playlist URL (also private playlists, because you gave the program permissions to do so). After you paste URL here, click enter. Now, you have to wait for couple of seconds.

After some time, you will see first message. `Song named "name of your song" downloader`. From now, it will download all songs in the playlist. The script will automatically end after downloading all songs.

You can find songs in folder named `downloaded_songs`. There will be folder with name of your album/playlist and inside, there will be all songs downloaded.

## Limitations
Because I'm using Google's YouTube API, it has daily limit of 100 searches per day. That means, you can download only 100 songs a day.

## Help
If you encounter an error in any stage of setup or using of application, please write me and I will help you.

Also, If you have any questions about program, you can write me as well.
## Legality statement

This program/application is created and provided for educational purposes only. The intent of this program/application is to showcase and teach various programming concepts and techniques. It is not intended to be used for any illegal, unethical, or malicious activities.

By using this program/application, you acknowledge that:

1. You will only use this program/application for lawful and ethical purposes.

2. You will not engage in any activities that violate any local, state, national, or international laws or regulations or any company term of use!

3. You understand that the creator(s) of this program/application do not endorse, encourage, or take any responsibility for any misuse or illegal use of this program/application.

  

The creator(s) of this program/application are not liable for any actions taken by individuals who use this program/application. Any consequences of using this program/application for illegal or unethical purposes rest solely upon the user.

It is your responsibility to use this program/application in a responsible and ethical manner. If you do not agree with these terms, you are advised not to use this program/application.

For legal advice or questions, please consult with a qualified legal professional.


Dominik Žampach

30.8.2023
