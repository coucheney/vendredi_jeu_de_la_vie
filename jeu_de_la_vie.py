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
import copy


###########################
# constantes du programme

COUL_FOND = "grey30"
COUL_QUADR = "grey60"
COUL_CARRE = "yellow"
LARGEUR = 600
HAUTEUR = 400
COTE = 20
NB_COL = LARGEUR // COTE
NB_LIG = HAUTEUR // COTE


########################
# variables globales

tableau = []

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


def xy_to_ij(x, y):
    """Retourne les coordonnées de la case du tableau
    correspondant au pixel de coordonnées (x, y)"""
    return x // COTE, y // COTE


def chg_case(event):
    """Change l'état de la case sur laquelle on a cliqué"""
    i, j = xy_to_ij(event.x, event.y)
    if tableau[i][j] == 0:
        # si la case est morte
        x, y = i * COTE, j * COTE
        carre = canvas.create_rectangle((x, y),
                                        (x+COTE, y+COTE),
                                        fill=COUL_CARRE, outline=COUL_QUADR)
        tableau[i][j] = carre
    else:
        canvas.delete(tableau[i][j])
        tableau[i][j] = 0


def nb_vivant(i, j):
    """Retourne le nombre de cases vivantes
       autour de la case de coordonnées (i, j)"""
    cpt = 0
    for k in range(max(0, i-1), min(NB_COL, i+2)):
        for el in range(max(0, j-1), min(NB_LIG, j+2)):
            if tableau[k][el] != 0 and [k, el] != [i, j]:
                cpt += 1
    return cpt


def etape_ij(i, j):
    """Fait une étape du jeu de la vie sur la case de coordonnées (i, j)
       et retourne la valeur à modifier dans le tableau"""
    n = nb_vivant(i, j)
    if tableau[i][j] == 0:
        # si la case est morte
        if n == 3:
            x, y = i * COTE, j * COTE
            carre = canvas.create_rectangle((x, y), (x+COTE, y+COTE),
                                            fill=COUL_CARRE,
                                            outline=COUL_QUADR)
            return carre
        else:
            return 0
    else:
        # si la case est vivante
        if n in [2, 3]:
            return tableau[i][j]
        else:
            canvas.delete(tableau[i][j])
            return 0


def etape(event):
    """Fait une étape du jeu de la vie"""
    global tableau
    tableau_res = copy.deepcopy(tableau)
    for i in range(NB_COL):
        for j in range(NB_LIG):
            tableau_res[i][j] = etape_ij(i, j)
    tableau = tableau_res


#############################
# programme principal

# création du tableau initialisé à 0
for i in range(NB_COL):
    tableau.append([0] * NB_LIG)

racine = tk.Tk()
racine.title("Jeu de la vie")

# création des widgets
canvas = tk.Canvas(racine, bg=COUL_FOND, width=LARGEUR, height=HAUTEUR)

# placement des widgets
canvas.grid()

# gestion des événements
canvas.bind("<1>", chg_case)
racine.bind("n", etape)

# autres fonctions
quadrillage()

racine.mainloop()
