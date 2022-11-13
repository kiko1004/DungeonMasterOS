import requests

class Character:
    def __init__(self, char_number):
        url = f"https://character-service.dndbeyond.com/character/v3/character/{char_number}"
        response = requests.request("GET", url).json()['data']
        self.name, self.race, self.age = response['name'], response['race']['fullName'], response['age']

class NullCharacter(Character):
    def __init__(self):
        self.name, self.race, self.age = ('Player', 'Human', 20)
