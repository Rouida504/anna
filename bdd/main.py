import pymongo  
from game import demarrer_jeu 

# Connexion à la base de données
client = pymongo.MongoClient("mongodb://localhost:27017/")
db = client["jeu_video"]


#  on define les fonctions 

def afficher_classement():
    print("les meilleurs scores")

# on recupere tous les scores dans la bd 
tous_les_resultats = db.cores.find()

# On transforme ces résultats en une liste 
liste_des_scores = list(tous_les_resultats)

# On crée une petite fonction toute simple
def recuperer_le_score(un_resultat):
    return un_resultat["pv"]

# faire une fonction pour trier 
liste_triee = sorted(liste_des_scores, key=recuperer_le_score, reverse=True)

# 
def menu_principal():
        print("1. Jouer")
        print("2. Voir le classement")
        print("3. Quitter")



# on lance le  programme pour qu'on dis 
def recuperer_saisie_valide():
    while true: 
      try:
        choix = int(input(choisissez entre 1,2 et 3)) 
        if choix = [1,2 ou 3]:
          return choix 
    else:
      print("entrer 1,2 ou 3 ") 
    

def main():
    menu_principal()
    #recuperer choix utilisteur doit etre valide 
    choix_utilisateur = recuperer_saisie_valide()

    # si choix 1 tu lance le jeu 
    if choix_utilisateur == 1:
        demarrer_jeu()
    # si choix 2 voir le classement
    if choix_utilisateur == 2:
        voir_le_classement()
    # si chois 3 quitter le jeu 
    if choix_utilisateur == 3:
        quitter_le_jeu()

main()







