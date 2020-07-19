# says i can figure out this project using everything i learned in chapter 9 and 10
# however, concepts are far more advanced than what I have learned about JSON
# only the methods dump() and load() are taught in the book, and nothing more
# book does not even talk about decoding errors or "TextIOWrapper()" or serialization
# not once are classes and JSON used together, so I am completely lost
# debugging is not enough to explain anything


import json

filename = 'pokemon.json'


class Pokemon:
    def __init__(self):
        self.name = input("What is your Pokemon's name? ")
        self.type = input("What is your Pokemon's type? ")
        self.level = input("What is your Pokemon's level? ")
        pokemon_data = f"Name: {self.name}\n" \
                       f"Type: {self.type}\n" \
                       f"Level: {self.level}"
        print(pokemon_data)


try:
    with open(filename, 'r+') as f:
        json.load(f)
        print("Good")
except FileNotFoundError:
    pokemon = Pokemon
    with open(filename, 'a+') as f:
        json.dumps(f.__init__(self=Pokemon))


