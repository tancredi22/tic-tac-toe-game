import tkinter as tk
from tkinter import messagebox
from random import randrange

tablero = [[1, 2, 3], [4, "X", 6], [7, 8, 9]]
botones = []


def VictoryFor(board, sign):
    if board[0][0] == sign and board[0][1] == sign and board[0][2] == sign:
        return True

    elif board[1][0] == sign and board[1][1] == sign and board[1][2] == sign:
        return True

    elif board[2][0] == sign and board[2][1] == sign and board[2][2] == sign:
        return True

    elif board[0][0] == sign and board[1][0] == sign and board[2][0] == sign:
        return True

    elif board[0][1] == sign and board[1][1] == sign and board[2][1] == sign:
        return True

    elif board[0][2] == sign and board[1][2] == sign and board[2][2] == sign:
        return True

    elif board[0][0] == sign and board[1][1] == sign and board[2][2] == sign:
        return True

    elif board[0][2] == sign and board[1][1] == sign and board[2][0] == sign:
        return True

    else:
        return False


def EnterMove_O(board, user):
    if user == "1":

        if board[0][0] == 'X' or board[0][0] == 'O':
            return False
        else:
            board[0][0] = 'O'
            botones[0]["image"] = photo_O

    elif user == "2":

        if board[0][1] == 'X' or board[0][1] == 'O':
            return False
        else:
            board[0][1] = 'O'
            botones[1]["image"] = photo_O

    elif user == "3":

        if board[0][2] == 'X' or board[0][2] == 'O':
            return False
        else:
            board[0][2] = 'O'
            botones[2]["image"] = photo_O

    elif user == "4":

        if board[1][0] == "X" or board[1][0] == "O":
            return False

        else:
            board[1][0] = 'O'
            botones[3]["image"] = photo_O

    elif user == "5":

        if board[1][1] == "X" or board[1][1] == "O":
            return False

        else:
            board[1][1] = 'O'
            botones[4]["image"] = photo_O

    elif user == "6":

        if board[1][2] == "X" or board[1][2] == "O":
            return False

        else:
            board[1][2] = 'O'
            botones[5]["image"] = photo_O

    elif user == "7":

        if board[2][0] == "X" or board[2][0] == "O":
            return False
        else:
            board[2][0] = 'O'
            botones[6]["image"] = photo_O

    elif user == "8":

        if board[2][1] == "X" or board[2][1] == "O":
            return False

        else:
            board[2][1] = 'O'
            botones[7]["image"] = photo_O

    elif user == "9":

        if board[2][2] == "X" or board[2][2] == "O":
            return False

        else:
            board[2][2] = 'O'
            botones[8]["image"] = photo_O

    return True


def DrawMove(board):
    machine_move = (randrange(1, 10))
    if machine_move == 1:

        if board[0][0] == 'O' or board[0][0] == 'X':
            return False
        else:
            board[0][0] = 'X'
            botones[0]["image"] = photo_X

    elif machine_move == 2:

        if board[0][1] == 'O' or board[0][1] == 'X':
            return False
        else:
            board[0][1] = 'X'
            botones[1]["image"] = photo_X

    elif machine_move == 3:

        if board[0][2] == 'O' or board[0][2] == 'X':
            return False
        else:
            board[0][2] = 'X'
            botones[2]["image"] = photo_X

    elif machine_move == 4:

        if board[1][0] == 'O' or board[1][0] == 'X':
            return False
        else:
            board[1][0] = 'X'
            botones[3]["image"] = photo_X

    elif machine_move == 5:

        if board[1][1] == 'O' or board[1][1] == 'X':
            return False
        else:
            board[1][1] = 'X'
            botones[4]["image"] = photo_X

    elif machine_move == 6:

        if board[1][2] == 'O' or board[1][2] == 'X':
            return False
        else:
            board[1][2] = 'X'
            botones[5]["image"] = photo_X

    elif machine_move == 7:

        if board[2][0] == 'O' or board[2][0] == 'X':
            return False
        else:
            board[2][0] = 'X'
            botones[6]["image"] = photo_X

    elif machine_move == 8:

        if board[2][1] == 'O' or board[2][1] == 'X':
            return False
        else:
            board[2][1] = 'X'
            botones[7]["image"] = photo_X

    elif machine_move == 9:

        if board[2][2] == 'O' or board[2][2] == 'X':
            return False
        else:
            board[2][2] = 'X'
            botones[8]["image"] = photo_X

    return True


def Enter(event):
    try:
        clicked_btn = event.widget

        move = EnterMove_O(tablero, clicked_btn["text"])

        if not move:
            return

        if VictoryFor(tablero, 'O'):
            messagebox.showinfo("GAME OVER", "I Won!")
            wnd.destroy()

        while True:
            if DrawMove(tablero):
                break

        if VictoryFor(tablero, 'X'):
            messagebox.showinfo("GAME OVER", "Machine Won!")
            wnd.destroy()
    except:
        pass


wnd = tk.Tk()
wnd.title("TicTacToe")
photo = tk.PhotoImage(file=r"solid-white.png")
photo_O = tk.PhotoImage(file=r"tic-tac-toe-circle.png")
photo_X = tk.PhotoImage(file=r"icone-x-verde.png")

for i in range(9):

    if i == 4:
        botones.append(tk.Button(wnd, text=str(i + 1), image=photo_X, width=64, height=64))

    else:
        botones.append(tk.Button(wnd, text=str(i + 1), image=photo, width=64, height=64))

for i in range(9):
    botones[i].grid(column=i // 3, row=i % 3)
    botones[i].bind("<Button-1>", Enter)

wnd.mainloop()