import numpy as np


def showBoard(board):
    """
        affiche le plateau de jeu
    """
    print(board)

def draw(round):
    """
        regarde si il y a egalité au bout de 9 tour car au 9ème tour il n'y a plus de case libre.
        renvoie si oui ou non il y a une égalité
    """
    if round == 9:
        print("égalité")
        return True
    return False

def victory(board, player_symbols):
    """
        regarde si qqln a gagné avec des fonctions de numpy en verifiant d'abord les lignes et colunnes , ensuite les deux diagonales.
        renvoie un booléen pour dire si oui ou non il a gagné
    """
    if np.any(np.all(board == player_symbols, axis=0)):
        print("ca gagne")
        return True
    elif np.any(np.all(board == player_symbols, axis=1)):
        print("ca gagne")
        return True
    elif np.all(np.diag(board) == player_symbols):
        print("ca gagne")
        return True
    elif np.all(np.diag(np.fliplr(board)) == player_symbols):
        print("ca gagne")
        return True
    return False

def morpion():
    """
        fonction principale du code. elle demande a l'utilisateur d'entrées des coordonnées pour pouvoir placer son symbole,
        puis vérifie si la case est libre et ensuite le place. pour a la fin vérifier si il y a égalité ou si il a gagné.
    """
    round = 0
    symbols = ("X","O")
    board = np.full((3,3)," ")

    while True:
        showBoard(board)
        player_symbols = symbols[round % 2]
        print("joueur", player_symbols, "a vous de jouer")
        line = int(input("choisissez une ligne entre 1 et 3: "))
        line -=1
        colum = int(input("choisissez une collone entre 1 et 3: "))
        colum -=1

        if line <0 or line >2 or colum <0 or colum >2:
            print("donnez coordonnées valides")
            continue

        if board[line, colum] != " ":
            print("case occupée")
            continue

        board[line, colum] = player_symbols
        round +=1

        if victory(board, player_symbols):
            break

        if draw(round):
            break

if __name__ == "__main__":
    morpion()
