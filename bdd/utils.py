#contenant les fonctions pour l'affichage et la gestion des données

# faut deja connecter a la bd 
client = MongoClient("mongodb://localhost:27017/")
db = client["jeu_video"]

# recuperer les personnages 
def recuperer_les_personnages():
    return list(db.personnages.find())
print("recuperation des personnages ")


# recuperer les monstres 
def recuperer_les_monstres():
    return list(db.monstres.find())
print("recuperation des monstres")


# afficher le classement 
def voir_le_classement():
    return
print("classement afficher")


# enregistrer le score 
def enregistrer_le_score(nom_utilisateur,score_final): 
    "username" = nom_utilisateur,
    "score" = score_final 
    db.scores.insert_one(donnes_du_score)
print("score enregister ")