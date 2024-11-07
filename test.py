# ==============================
# Import des modules nécessaires
# ==============================
import tkinter as tk
from tkinter import messagebox

# ==============================
# Définition des constantes
# ==============================
GRID_SIZE = 9  # Taille de la grille (9x9)
SUBGRID_SIZE = 3  # Taille des sous-grilles (3x3)

# ==============================
# Définition des fonctions
# ==============================

def is_valid(grid, row, col, num):
    """
    Vérifie si un nombre peut être placé dans une case de la grille.
    Arguments:
        grid : liste de listes (grille 9x9)
        row : int (ligne de la case)
        col : int (colonne de la case)
        num : int (nombre à placer)
    Retourne:
        bool : True si valide, False sinon
    """
    for i in range(GRID_SIZE):
        if grid[row][i] == num or grid[i][col] == num:
            return False

    start_row, start_col = row - row % SUBGRID_SIZE, col - col % SUBGRID_SIZE
    for i in range(SUBGRID_SIZE):
        for j in range(SUBGRID_SIZE):
            if grid[i + start_row][j + start_col] == num:
                return False

    return True

def solve_sudoku(grid):
    """
    Résout une grille de Sudoku en utilisant l'algorithme de backtracking.
    Arguments:
        grid : liste de listes (grille 9x9)
    Retourne:
        bool : True si la grille est résolue, False sinon
    """
    for row in range(GRID_SIZE):
        for col in range(GRID_SIZE):
            if grid[row][col] == 0:
                for num in range(1, 10):
                    if is_valid(grid, row, col, num):
                        grid[row][col] = num
                        if solve_sudoku(grid):
                            return True
                        grid[row][col] = 0
                return False
    return True

def check_grid_complete(grid):
    """
    Vérifie si la grille est entièrement remplie.
    Arguments:
        grid : liste de listes (grille 9x9)
    Retourne:
        bool : True si complète, False sinon
    """
    for row in grid:
        if 0 in row:
            return False
    return True

# ==============================
# Interface graphique
# ==============================

class SudokuApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Résolution de Sudoku")
        self.entries = [[None for _ in range(GRID_SIZE)] for _ in range(GRID_SIZE)]
        self.create_grid()
        self.create_buttons()

    def create_grid(self):
        """
        Crée la grille de Sudoku avec des champs d'entrée pour les chiffres.
        """
        for row in range(GRID_SIZE):
            for col in range(GRID_SIZE):
                entry = tk.Entry(self.root, width=2, font=('Arial', 18), justify='center')
                entry.grid(row=row, column=col, padx=2, pady=2)
                self.entries[row][col] = entry

    def create_buttons(self):
        """
        Crée les boutons pour résoudre la grille et réinitialiser.
        """
        solve_button = tk.Button(self.root, text="Résoudre", command=self.solve)
        solve_button.grid(row=GRID_SIZE, column=0, columnspan=5, pady=10)
        
        reset_button = tk.Button(self.root, text="Réinitialiser", command=self.reset_grid)
        reset_button.grid(row=GRID_SIZE, column=5, columnspan=4, pady=10)

    def get_grid(self):
        """
        Récupère les valeurs entrées par l'utilisateur et les transforme en grille.
        Retourne:
            list : grille de Sudoku (liste de listes 9x9)
        """
        grid = []
        for row in range(GRID_SIZE):
            row_vals = []
            for col in range(GRID_SIZE):
                val = self.entries[row][col].get()
                row_vals.append(int(val) if val.isdigit() else 0)
            grid.append(row_vals)
        return grid

    def set_grid(self, grid):
        """
        Remplit les champs d'entrée avec les valeurs de la grille.
        Arguments:
            grid : liste de listes (grille 9x9)
        """
        for row in range(GRID_SIZE):
            for col in range(GRID_SIZE):
                self.entries[row][col].delete(0, tk.END)
                if grid[row][col] != 0:
                    self.entries[row][col].insert(0, grid[row][col])

    def solve(self):
        """
        Récupère la grille, la résout et affiche la solution.
        """
        grid = self.get_grid()
        if not solve_sudoku(grid):
            messagebox.showinfo("Erreur", "Impossible de résoudre la grille.")
        else:
            self.set_grid(grid)

    def reset_grid(self):
        """
        Réinitialise la grille en vidant tous les champs d'entrée.
        """
        for row in range(GRID_SIZE):
            for col in range(GRID_SIZE):
                self.entries[row][col].delete(0, tk.END)

# ==============================
# Programme principal
# ==============================

if __name__ == "__main__":
    root = tk.Tk()
    app = SudokuApp(root)
    root.mainloop()
