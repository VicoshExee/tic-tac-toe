import tkinter as tk
from tkinter import messagebox
import numpy as np
import random


def create_board_ia_easy(win_morpion):
    """
            Cette fonction crée le plateau de jeu en prenant en paramètre la fenêtre tkinter et le retourne.
    """

    global symbols, player, np_board, round, board
    symbols = ["X", "O"]
    player = 0
    np_board = np.full((3, 3), " ")
    round = 0
    board = []

    board = [[tk.Button(win_morpion, text=" ", width=21, height=10, command=lambda line=i, colum=j: ca_click(line, colum))
              for j in range(3)] for i in range(3)]
    for i in range(3):
        for j in range(3):
            board[i][j].grid(row=i, column=j)
    return board


def ca_click(line, colum):
    """
           Cette fonction effectue une action lorsqu'un bouton du plateau est cliqué.
           Elle prend en paramètre la ligne et la colonne du bouton cliqué.
    """
    global player, round
    if np_board[line, colum] == " ":
        button = board[line][colum]
        button.config(text=symbols[player])
        np_board[line, colum] = symbols[player]
        round += 1

        if draw():
            messagebox.showinfo("Draw", "egalite")
            reset()

        elif victory(board, symbols[player]):
            messagebox.showinfo("Winner", "ca gagne")
            reset()

        else:
            player = (player + 1) % 2
            if player == 1:
                ai_play = ai_easy()
                if ai_play:
                    ca_click(ai_play[0], ai_play[1])


def ai_easy():
    empty_cellule = np.argwhere(np_board == " ")
    if len(empty_cellule) > 0:
        return (list(empty_cellule[np.random.choice(len(empty_cellule))]))
    else:
        draw()
        messagebox.showinfo("Draw", "egalite")
        reset()


def draw():
    """
          Cette fonction vérifie s'il y a un match nul.
          Elle retourne True si le match est nul, sinon False.
    """
    if round ==9:
        return True
    return False

def victory(board, symbol):
    """
           Cette fonction vérifie s'il y a une victoire pour un joueur.
           Elle prend en paramètres le plateau de jeu et le symbole du joueur.
           Elle retourne True si le joueur a gagné, sinon False.
    """
    if np.any(np.all(np_board == symbol, axis=0)):
        return True
    elif np.any(np.all(np_board == symbol, axis=1)):
        return True
    elif np.all(np.diag(np_board) == symbol):
        return True
    elif np.all(np.diag(np.fliplr(np_board)) == symbol):
        return True
    return False

def reset():
    """
          Cette fonction réinitialise le jeu.
          Elle réinitialise les variables globales et réinitialise les boutons du plateau.
    """
    global board, player, round, np_board
    np_board = np.full((3, 3), " ")
    player = 0
    round = 0
    for i in range(3):
        for j in range(3):
            board[i][j].config(text=" ", state=tk.NORMAL)



