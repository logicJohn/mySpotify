import json
from pokemon import Pokedex

pokedex = Pokedex()
pokemon = pokedex._get_pokemon("ditto")



with open('pokemon.json', 'w') as outfile:
    json.dump(pokemon, outfile)


with open('pokemon-type.json', 'w') as outfile:
    json.dump(pokemon["types"], outfile)

print(pokemon["types"])
#print(pokemon["types"][0])   