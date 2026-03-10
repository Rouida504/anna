import random


# Le choix de l'équipe 3 personnages  
# Le combat (avec une boucle qui tourne tant qu'on a des héros en vie)
# enregistrer le score final

# on lance le jeu 
def demarrer_jeu(db):
    print("debut de jeu ")
    nom_joueur = input("entrer le nom de jouer ")

# On recupere les listes depuis MongoDB 
    liste_persos = list(db.personnages.find())
    liste_monstres = list(db.monstres.find())

# on fait le choix d'equipe
equipe_choisis = 
print("les 3 personnages de l'equipe ")

# le commancement de combat 
def lancer_combat(persona,monstre,heros)

# on doit choisit un monstre det un heros 
    print("")
    
    
# faie une condition 
heros_vivant = True
monstre_vivant = False 

# si le héros est mort
if not heros_vivant and monstre_vivant:
    print("Le héros est mort")

# si le monstre est mort
elif heros_vivant and not monstre_vivant:
    print("Le monstre est mort")

# si les deux sont morts
elif not heros_vivant and not monstre_vivant:
    print("Les deux sont morts")

# si aucun n'est mort
else:
    print("Les deux sont encore vivants")

    
           
# a la fin on sauvegarde le score 
donnees_du_score = {"joueur":nom , "score": score_final}
db.scores.insert_one(donnees_du_score)
print("Ton score a été enregistré dans le classement")