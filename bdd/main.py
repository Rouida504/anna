import pymongo  
from game import demarrer_jeu 
from utils import quitter_le_jeu , voir_le_classement 

# Connexion à la base de données
client = pymongo.MongoClient("mongodb://localhost:27017/")
db = client["jeu_video"]

# affiche la liste de 10 personnages 
liste_des_perssonages = []


#  on define les fonctions 

def afficher_classement():
    print("les meilleurs scores")

# on recupere tous les scores dans la bd 
tous_les_resultats = db.cores.find()


# On transforme ces résultats en une liste 
liste_des_scores = list(tous_les_resultats)
for resultats in liste_des_scores:
    print("tous les resultats")

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

# cree une fonction pour affichier le classement 
def voir_le_classement():
    print("le classement s'affiche ")



# cree une fonction pour quitter le jeu 
def quitter_le_jeu():
    print("vous aves quitter le jeu")


# on lance le  programme pour qu'on dis 

def recuperer_saisie_valide(message, min_val, max_val):
    while True:
        choix = input(message)
        
    # On vérifie que c bien un nombre 
        if choix.isdigit():
            nombre = int(choix)
            
            # on vérifie si c'est inférieur ou supérieur 
            if nombre < min_val:
                print("C'est trop petit ")
            elif nombre > max_val:
                print("C'est trop grand ")
            else:
            # Si ce n'est ni trop petit ni trop grand
                return nombre
        else:
            print("Erreur")


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







