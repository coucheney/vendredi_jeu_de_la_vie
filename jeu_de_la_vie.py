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

COUL_FOND = "blue"
LARGEUR = 600
HAUTEUR = 400



##########################
# fonctions du programme





#############################
# programme principal

racine = tk.Tk()
racine.title("Jeu de la vie")
canvas = tk.Canvas(racine, bg=COUL_FOND, width=LARGEUR, height=HAUTEUR)
canvas.grid()

racine.mainloop()


