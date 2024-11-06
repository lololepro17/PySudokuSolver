### Load from other fetch ###


def is_valide(grille, row, col, valeur):
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


###   ###

def solve_sudoku(grille):
    # search an empty hut
    for i in range(9):
        for j in range(9):
            if grille[i][j] == 0:  # find empty hut
                # Try to inser a value in the empty hut (1 to 9)
                for valeur in range(1, 10):
                    if is_valide(grille, i, j, valeur):
                        # Place place the values if is valide
                        grille[i][j] = valeur
                        # Recursive call to try to complete the grid
                        if solve_sudoku(grille):
                            return True
                        # Backtracing of the values block the solve
                        grille[i][j] = 0
                # If don't have values go back 
                return False
    # If don't have empty hut finish
    return True