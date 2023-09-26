class YTAuth():
    def authorize_api_key(self):
        api_key = self.get_api_key()
        if api_key == "delete_this_and_enter_your_key":
            self.how_to_setup_API_key()
            api_key = self.get_api_key()
        return api_key

    def how_to_setup_API_key(self):
        print("Do this and than, then press enter...")
        input()

    def get_api_key(self):
        with open('key.txt', 'r') as f:
            text = f.read()
            if "key=" in text:
                data = text.split("key=")[1].strip()
                return data

#Edulint Done
#mypy
