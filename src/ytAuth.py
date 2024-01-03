import sys

class YTAuth():
    def authorize_api_key(self, dir_path):
        api_key = self.get_api_key(dir_path)
        if api_key == "":
            self.how_to_setup_API_key()
            input()
            sys.exit()
        return api_key

    def how_to_setup_API_key(self):
        print("There is no key in key.txt file. Please look at README.md for more info...")

    def get_api_key(self, dir_path):
        with open(f'{dir_path[0:len(dir_path)-4]}/key.txt', 'r') as f:
            text = f.read()
            if "key=" in text:
                data = text.split("key=")[1].strip()
                return data

# Edulint Done
# mypy
