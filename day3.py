trophies={
    "england":{
        "league cup": "Liverpool", 
        "fa cup": "Liverpool", 
        "premier league": "Manchester City",
    },
    "germany": {
        "bundesliga": "Bayern Munich",
        "dfb-pokal": "RB Leipzig",
    },
    "italy": {
        "serie a": "AC MIlan",
        "coppa italia": "Internazionale"
    },
    "spain": {
        "la liga": "Real Madrid",
        "copa del rey": "Real Betis"
    }
}

for i in trophies.values():
    print(i)

#dict.setdefault("key", "value") will update the dictionary, but can not overwrite an existing key:value pair.

#dict["key"].pop("key") will pop from a dictionary inside a dictionary.

capitals = {
    "United Kingdom": "London",
    "Spain": "Madrid",
    "Italy": "Rome",
    "France": "Paris",
    "Germany": "Munich"
}

for i in capitals:
    print(i)

for i in capitals.values():
    print(i)

capitals.setdefault("Portugal", "Lisbon")
capitals.setdefault("Austria", "Vienna")

capitals["United Kingdom"] = "English"
capitals["Spain"] = "Spanish"
capitals["Italy"] = "Italian"
capitals["Germany"] = "Germany"
capitals["France"] = "Paris"

for i in capitals.values():
    print(i)

fav_movies = [
    {
        "title": "chicken run",
        "genre": "family",
        "actor": "mel gibson"
    },
    {
        "title": "the waterboy",
        "genre": "comedy",
        "actor": "adam sandler"
    },
    {
        "title": "die hard",
        "genre": "action",
        "actor": "bruce willis"
    }
]

for i in fav_movies:
    print(i)

fav_movies.pop()

for i in fav_movies:
    print(i)