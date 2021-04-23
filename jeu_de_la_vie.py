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
val = 0
delai = 500

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


def etape():
    """Fait une étape du jeu de la vie"""
    global tableau
    tableau_res = copy.deepcopy(tableau)
    for i in range(NB_COL):
        for j in range(NB_LIG):
            tableau_res[i][j] = etape_ij(i, j)
    tableau = tableau_res


def etape_n(event):
    """Fait une étape de l'automate en enelevant le paramètre event"""
    etape()


def sauvegarder():
    """Sauvegarde le tableau dans le fichier sauvegarde.txt"""
    fic = open("sauvegarde.txt", "w")
    for i in range(NB_COL):
        for j in range(NB_LIG):
            fic.write(str(tableau[i][j]) + "\n")
    fic.close()


def charger():
    """Chargement du fichier sauvegarde.txt pour dessiner la grille"""
    fic = open("sauvegarde.txt", "r")
    canvas.delete("all")
    quadrillage()
    cpt = 0
    for ligne in fic:
        i, j = cpt // NB_LIG, cpt % NB_LIG
        n = int(ligne)
        if n == 0:
            tableau[i][j] = 0
        else:
            x, y = i * COTE, j * COTE
            carre = canvas.create_rectangle((x, y),
                                            (x+COTE, y+COTE),
                                            fill=COUL_CARRE,
                                            outline=COUL_QUADR)
            tableau[i][j] = carre
        cpt += 1
    fic.close()


def start():
    """Démarre l'automate"""
    global id_after
    etape()
    id_after = racine.after(delai, start)


def start_stop():
    """Démarre ou arrête l'automate et change le texte du bouton"""
    global val
    if val == 0:
        bout_start_stop.config(text="arrêter")
        start()
    else:
        bout_start_stop.config(text="démarrer")
        racine.after_cancel(id_after)
    val = 1 - val


def augmente_delai(event):
    """augmente le délai entre 2 étapes de l'automate"""
    global delai
    if delai < 1000:
        delai += 10
        lbl_delai.config(text="Délai entre 2 étapes " + str(delai) + "ms")


def diminue_delai(event):
    """diminue le délai entre 2 étapes de l'automate"""
    global delai
    if delai > 10:
        delai -= 10
        lbl_delai.config(text="Délai entre 2 étapes " + str(delai) + "ms")


#############################
# programme principal

# création du tableau initialisé à 0
for i in range(NB_COL):
    tableau.append([0] * NB_LIG)

racine = tk.Tk()
racine.title("Jeu de la vie")

# création des widgets
canvas = tk.Canvas(racine, bg=COUL_FOND, width=LARGEUR, height=HAUTEUR)
bout_sauv = tk.Button(racine, text="Sauvegarder", command=sauvegarder)
bout_charger = tk.Button(racine, text="Charger", command=charger)
bout_start_stop = tk.Button(racine, text="démarrer", command=start_stop)
lbl_delai = tk.Label(racine, text="Délai entre 2 étapes " + str(delai) + "ms")

# placement des widgets
canvas.grid(rowspan=3)
bout_sauv.grid(column=1, row=0)
bout_charger.grid(column=1, row=1)
bout_start_stop.grid(column=1, row=2)
lbl_delai.grid(column=0, row=3)

# gestion des événements
canvas.bind("<1>", chg_case)
racine.bind("n", etape_n)
racine.bind("m", diminue_delai)
racine.bind("p", augmente_delai)

# autres fonctions
quadrillage()

racine.mainloop()
