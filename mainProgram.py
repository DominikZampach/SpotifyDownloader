import sys, requests
class MainProgram():
    def __init__(self) -> None:
        pass
    
    def main(self):
        print("Welcome to my application for downloading Spotify playlists.\nI'm really happy you have chosen my application <3")
        self.get_state_of_PL()
        self.get_playlist_id()
        print(self.info)
        
    
    def get_state_of_PL(self):
        self.info = {}
        self.info["public"] = input("Do you want to download public (write 1) playlist or private (write 2): ")
        
        while self.info["public"] != "1" and self.info["public"] != "2": #Checking input
            self.info["public"] = input("Wrong input, please write 1 if you want to download public playlist\nor 2 if you want to download private playlist: ")
            
        if self.info["public"] == "1":
            self.info["public"] = True
        else:
            self.info["public"] = False


        if self.info["public"] == False: #when chosen playlist is private
            print("Not implemented yet")
            input()
            sys.exit()
    
    def get_playlist_id(self):
        self.info["urlPlaylist"] = input("Paste your url adress for playlist: ")
        #Before checking url, check if it's even url :D (That means try request that url and see the response code)
        notURL = True
        while notURL: 
            if not self.info["urlPlaylist"].startswith("https://"): #adding https if not included
                self.info["urlPlaylist"] = "https://" + self.info["urlPlaylist"]
            try:
                testRequest = requests.get(self.info["urlPlaylist"]).status_code
                if testRequest == 200 and self.info["urlPlaylist"].startswith("https://open.spotify.com/playlist/"):
                    notURL = False
                else:
                    self.info["urlPlaylist"] = input("This URL adress isn't for Spotify playlist, please try it again: ")
            except:
                self.info["urlPlaylist"] = input("Text isn't URL adress, please try it again: ")
        
        #here, the right Spotify playlist URL adress comes
        self.info["playlist_id"] = self.info["urlPlaylist"][34:self.info["urlPlaylist"].index("?")]
    
    
        
        