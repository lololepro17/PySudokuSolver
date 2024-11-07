import json

def save_grid(grille, nom_fichier):
    """Save grid with the name 'nom_fichier'."""
    with open(nom_fichier, 'w') as f: # Open file with permissions of write.
        json.dump(grille, f)


def load_grid(nom_fichier):
    """Load the grid."""
    with open(nom_fichier, 'r') as f: # Open file with permission of read.
        return json.load(f)
    
grid = load_grid("empty_grid.json")


def afficher_grille(grille):
    """Post a grid."""
    for ligne in grille:
        print(" ".join(str(val) if val != 0 else "." for val in ligne)) # If have val print val else print a '.' for empty.

# afficher_grille(load_grid("empty_grid.json"))

def est_valide(grille, row, col, valeur):
    """Check to find if the grid load is good. Return a bool of the result"""
    if valeur in grille[row]: # Check the row
        return False
    
    if valeur in (grille[i][col] for i in range(9)): # Check the column
        return False
    
    start_row, start_col = 3 * (row // 3), 3 * (col // 3) #Check a bloc of 3*3
    for i in range(3):
        for j in range(3):
            if grille[start_row + i][start_col + j] == valeur:
                return False
    return True


def afficher_ligne(grille,n):
    """Affiche une ligne demander (n)."""
    i = 0
    for ligne in grille:
        i += 1
        if i == n:
            return ligne

# print(afficher_ligne(grid,3))

def afficher_column(grid,n):
    col = []
    for i in range(9):
        col.append(grid[i][n])
    return col

print(afficher_column(grid,4))

def afficher_bloc(grid,row,col):
    start_row, start_col = 3 * (row // 3), 3 * (col // 3) #Check a bloc of 3*3
    for i in range(3):
        for j in range(3):
            if grid[start_row + i][start_col + j] == valeur:
                return False
    return True


def bloc(S, i, j):
    # Start
    row_start = (i // 3) * 3
    col_start = (j // 3) * 3
    
    chiffres_bloc = [] # Init por stocker les valeur du bloc 
    
    # Parcourir les 3x3 cases du bloc
    for r in range(row_start, row_start + 3):
        for c in range(col_start, col_start + 3):
            if S[r][c] != 0:  # Ignorer les zéros
                chiffres_bloc.append(S[r][c])
    return chiffres_bloc

print(bloc(grid,3,4))