from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017/")
db = client["jeu_video"]

personnages = [
    {"nom": "Guerrier", "atk": 50, "def": 19, "pv": 500},
    {"nom": "Mage", "atk": 20, "def": 5, "pv": 100},
    {"nom": "Archer", "atk": 28, "def": 10, "pv": 140},
    {"nom": "Voleur", "atk": 22, "def": 8, "pv": 95},
    {"nom": "Paladin", "atk": 20, "def": 15, "pv": 180},
    {"nom": "Sorcier", "atk": 25, "def": 8, "pv": 99},
    {"nom": "Chevalier", "atk": 17, "def": 15, "pv": 120},
    {"nom": "Moine", "atk": 19, "def": 9, "pv": 110},
    {"nom": "Berserker", "atk": 23, "def": 6, "pv": 105},
    {"nom": "Chasseur", "atk": 18, "def": 11, "pv": 100}
]

monstres = [
    {"nom": "Gobelin", "atk": 10, "def": 5, "pv": 200},
    {"nom": "Orc", "atk": 20, "def": 8, "pv": 120},
    {"nom": "Dragon", "atk": 35, "def": 20, "pv": 300},
    {"nom": "Zombie", "atk": 12, "def": 6, "pv": 70},
    {"nom": "Troll", "atk": 25, "def": 15, "pv": 200},
    {"nom": "Spectre", "atk": 18, "def": 10, "pv": 100},
    {"nom": "Golem", "atk": 30, "def": 25, "pv": 250},
    {"nom": "Vampire", "atk": 22, "def": 12, "pv": 150},
    {"nom": "Loup-garou", "atk": 28, "def": 18, "pv": 180},
    {"nom": "Squelette", "atk": 15, "def": 7, "pv": 90}
]

db.personnages.delete_many({})
db.monstres.delete_many({})
db.scores.delete_many({})

db.personnages.insert_many(personnages)
db.monstres.insert_many(monstres)

print("Base de données initialisée avec succés.")

   
