from pokedex import Database
from save_json import writeAJson

db = Database(database="dex", collection="pokemons")
db.resetDatabase()
pokemons = db.collection.find()


# for pokemon in pokemons:
# print(pokemon)

def getPokemonByDefense(number: int):
    return db.collection.find({"base.Defense": {"$lte": number}})


weak = getPokemonByDefense(50)
writeAJson(weak, "Weakers")


def getPokemonByType(word: str):
    return db.collection.find({"type": word})


typePokemons = getPokemonByType("Bug")
writeAJson(typePokemons, "Bugs")


def fastAndpoisonous():
    return db.collection.find({"type": "Poison", "base.Speed": {"$gte": 60}})


writeAJson(fastAndpoisonous(), "Dangerous")


def newandStrong():
    return db.collection.find({"id": {"$gte": 500}, "base.Attack": {"$gte": 70}})


writeAJson(newandStrong(), "NewerAndStronger")


def get_5_letters_or_less_french(collection):
    names = collection.find({}, {"name": 4})
    five_letters_or_less = []
    for name in names:
        if len(name["name"].keys()) <= 5:
            if all(len(word) <= 5 for word in name["name"].values()):
                five_letters_or_less.append(name["name"].values())
    return five_letters_or_less


writeAJson(get_5_letters_or_less_french(db.collection), "pokemon_5_words_or_less_french")
