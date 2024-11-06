import json

def save_grid(grille, nom_fichier):
    with open(nom_fichier, 'w') as f: # Open file with permissions of write.
        json.dump(grille, f)

def load_grid(nom_fichier):
    with open(nom_fichier, 'r') as f: # Open file with permission of read.
        return json.load(f)

def afficher_grille(grille):
    for ligne in grille:
        print(" ".join(str(val) if val != 0 else "." for val in ligne)) # If have val print val else print a '.' for empty.

# afficher_grille(load_grid("empty_grid.json"))
