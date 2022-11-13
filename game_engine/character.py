import requests

class Character:
    def __int__(self, char_number):
        url = f"https://character-service.dndbeyond.com/character/v3/character/{char_number}"
        response = requests.request("GET", url)['data']
        self.name, self.race, self.age = response.json()['name'], response.json()['race']['fullName'], response.json()['age']

class NullCharacter(Character):
    def __int__(self):
        self.name, self.race, self.age = ('Player', 'Human', 20)
