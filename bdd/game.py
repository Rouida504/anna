import random

client = MongoClient("mongodb://localhost:27017/")
db = client["jeu_video"]

# Le choix de l'équipe 3 personnages  
# Le combat (avec une boucle qui tourne tant qu'on a des héros en vie)
# enregistrer le score final

# on lance le jeu 
def demarrer_jeu(db):
    print("debut de jeu ")
    nom_joueur = input("entrer le nom de jouer ")

# On recupere les listes depuis MongoDB 
    liste_personnages = list(db.personnages.find())
    liste_monstres = list(db.monstres.find())

# on fait le choix d'equipe
equipe_choisis = []
print("les 3 personnages de l'equipe ")

# le commancement de combat 
def lancer_combat(persona,monstre,heros):
    print("combat lancer")

# on voit qui gagne / qui pert
# faire une condition 
heros_mort = []
monstre_mort =[]

# si le héros est mort
if heros_mort :
    print("Le héros est mort")

# si le monstre est mort
if monstre_mort:
    print("Le monstre est mort")

# si les deux sont morts
if heros_mort and  monstre_mort:
    print("Les deux sont morts")

# si aucun n'est mort
if not heros_mort and not monstre_mort:
    print("Les deux sont encore vivants")

# affichier le score final 
def score_final(): 
    print("score final ")

#affichier le nom 
def nom():


# a la fin on sauvegarde le score 
donnes_du_score = {"jouer":nom , "score":score_final}
db.scores.insert_one(donnes_du_score)
print("score enregistré dans le classement")



