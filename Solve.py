def resoudre_sudoku(grille):
    # Parcourt toutes les cases de la grille pour trouver une case vide
    for i in range(9):
        for j in range(9):
            if grille[i][j] == 0:  # Case vide trouvée
                # Tente d'insérer une valeur de 1 à 9 dans la case vide
                for valeur in range(1, 10):
                    if est_valide(grille, i, j, valeur):
                        # Place la valeur si elle est valide
                        grille[i][j] = valeur
                        # Appel récursif pour essayer de compléter la grille
                        if resoudre_sudoku(grille):
                            return True
                        # Si la valeur choisie mène à une impasse, annule le choix (backtracking)
                        grille[i][j] = 0
                # Si aucune valeur n'a fonctionné, retourne False pour revenir en arrière
                return False
    # Si aucune case vide n'est trouvée, le sudoku est résolu
    return True