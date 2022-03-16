import requests
import json

from requests.structures import CaseInsensitiveDict

headers = CaseInsensitiveDict()
headers["Accept"] = "application/json"

class Pokedex:
    """This is the interpriter for the pokemon api"""
    def __init__(self) -> None:
        self.url = "https://pokeapi.co/api/v2/"

    def _get_pokemon(self, pokemon):
        url_request=self.url+"pokemon/"+pokemon
        response = requests.get (
            url_request,
            headers
        )
        print(response.headers)
        json.dump()
        data = response.json()
        return data