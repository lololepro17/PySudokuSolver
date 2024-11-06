import json

def save_grid(grille, nom_fichier):
    with open(nom_fichier, 'w') as f: # Open file with permissions of write.
        json.dump(grille, f)

def load_grid(nom_fichier):
    with open(nom_fichier, 'r') as f: # Open file with permission of read.
        return json.load(f)
