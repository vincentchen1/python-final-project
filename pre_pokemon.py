import json


class Pokemon:
    def __init__(self):
        self.name = input("What is your Pokemon's name? ")
        self.type = input("What is your Pokemon's type? ")
        self.level = input("What is your Pokemon's level? ")
        pokemon_data = f"Name: {self.name}\n" \
                       f"Type: {self.type}\n" \
                       f"Level: {self.level}"
        print(pokemon_data)


filename = 'pokemon.json'
pokemon = Pokemon

with open(filename, 'a+') as f:
    json.dumps(f.__init__(self=Pokemon))

