#contenant les fonctions pour l'affichage et la gestion des données

# faut deja connecter a la bd 
def get_db(): 
client = MongoClient("mongodb://localhost:27017/")
db = client["jeu_video"]

# recuperer les personnages 
def recuperer_les_personnages():
    db = get_db()
    return
print("recuperation des personnages ")

# recuperer les monstres 
def recuperer_les_monstres():
    db = get_db()
    return
print("recuperation des monstres")

# afficher le classement 
def voir_le_classement():
    db = get_db()
    return
print("classement afficher")

# enregistrer le score 
def enregistrer_le_score(nom_utilisateur,score_final): 
    db = get_db()
    "username" = nom_utilisateur
    "score" = score_final 


db.scores.insert.one(score_data)
print("score enregister ")