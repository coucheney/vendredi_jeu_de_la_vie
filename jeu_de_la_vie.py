####################################
# Auteurs:
# Pierre Coucheney
# Toto
# Groupe de TD:
# MPCI 5
# Adresse du dépôt GitHub:
# https://github.com/coucheney/vendredi_jeu_de_la_vie
####################################

#########################
# import des modules

import tkinter as tk


###########################
# constantes du programme

COUL_FOND = "grey30"
COUL_QUADR = "grey60"
LARGEUR = 600
HAUTEUR = 400
COTE = 10




##########################
# fonctions du programme

def quadrillage():
    """Dessine un quadrillage formé de carrés de côté COTE"""
    y = 0
    while y <= HAUTEUR:
        canvas.create_line((0, y), (LARGEUR, y), fill=COUL_QUADR)
        y += COTE
    x = 0
    while x <= LARGEUR:
        canvas.create_line((x, 0), (x, HAUTEUR), fill=COUL_QUADR)
        x += COTE



#############################
# programme principal

racine = tk.Tk()
racine.title("Jeu de la vie")

# création des widgets
canvas = tk.Canvas(racine, bg=COUL_FOND, width=LARGEUR, height=HAUTEUR)

# placement des widgets
canvas.grid()

# autres fonctions
quadrillage()

racine.mainloop()


