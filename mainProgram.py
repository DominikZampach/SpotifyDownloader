import sys
class MainProgram():
    def __init__(self) -> None:
        pass
    
    def main(self):
        print("Welcome to my application for downloading Spotify playlists.\nI'm really happy you have chosen my application <3")
        self.informations = self.get_info()
    
    def get_info(self):
        self.info = {}
        self.info["public"] = input("Do you want to download public (write 1) playlist or private (write 2): ")
        while self.info["public"] != "1" and self.info["public"] != "2":
            self.info["public"] = input("Wrong input, please write 1 if you want to download public playlist\nor 2 if you want to download private playlist: ")
        self.info["public"] = int(self.info["public"]) #Convert to int for better work
        if self.info["public"] == 2: #when chosen playlist is private
            print("Not implemented yet")
            input()
            sys.exit()
        
        