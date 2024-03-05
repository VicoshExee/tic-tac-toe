import tkinter as tk
from morpion_tkinter import create_board
from morpion_ia_ez import create_board_ia_easy
from morpion_ia_middle import create_board_ia_middle
from morpion_ia_hard import create_board_ia_hard

win_jeu = tk.Tk()
win_jeu.title("Jeu Rétro")
win_jeu.maxsize(900, 600)
win_jeu.config(bg="skyblue")


def start_game_multi():
    suppr_right_frame()
    create_board(right_frame)

def start_game_ia_easy():
    suppr_right_frame()
    create_board_ia_easy(right_frame)

def start_game_ia_middle():
    suppr_right_frame()
    create_board_ia_middle(right_frame)

def start_game_ia_hard():
    suppr_right_frame()
    create_board_ia_hard(right_frame)

def suppr_right_frame():
    for i in right_frame.winfo_children():
        i.destroy()

def button_morpion():
    suppr_right_frame()
    boutton_morpion_multi = tk.Button(right_frame, text="1 VS 1", command= start_game_multi)
    boutton_morpion_multi.grid(row=0, column=0, padx=5, pady=5)

    boutton_morpion_ez = tk.Button(right_frame, text="IA easy", command= start_game_ia_easy)
    boutton_morpion_ez.grid(row=1, column=0, padx=5, pady=5)

    boutton_morpion_middle = tk.Button(right_frame, text="IA intermediate", command=start_game_ia_middle)
    boutton_morpion_middle.grid(row=2, column=0, padx=5, pady=5)

    boutton_morpion_hard = tk.Button(right_frame, text="IA HARD!!!!!!!!!!!!!!!!!", command=start_game_ia_hard)
    boutton_morpion_hard.grid(row=3, column=0, padx=5, pady=5)



#frame gauche
left_frame = tk.Frame(win_jeu, width=200, height=400, bg='grey')
left_frame.grid(row=0, column=0, padx=10, pady=5)

tk.Label(left_frame, text="Choisissez un jeu", bg="grey").grid(row=0, column=0, padx=5, pady=5)
tool_bar = tk.Frame(left_frame, width=180, height=185, bg="grey")
tool_bar.grid(row=2, column=0, padx=5, pady=5)

boutton_morpion = tk.Button(tool_bar, text="Morpion", bg="grey", command= button_morpion)
boutton_morpion.grid(row=1, column=0, padx=5, pady=5)

boutton_puissance4 = tk.Button(tool_bar, text="Puissance 4", bg='grey')
boutton_puissance4.grid(row=2, column=0, padx=5, pady=5)

#frame droite
right_frame = tk.Frame(win_jeu, width=650, height=400, bg='grey')
right_frame.grid(row=0, column=1, padx=10, pady=5)


win_jeu.mainloop()

