from tkinter import *
from tkinter import messagebox
import tic_win_comb
tk = Tk()
tk.title("Tic Tac Toe")


button_list = []
handler_list = []
row = 0
column = 0
set_x = set()
set_o = set()


board_size = int(input("Enter board size: "))
winning_sets = tic_win_comb.win_comb(board_size)

for i in range(board_size):
    for j in range(board_size):
        my_button = Button(tk, height=5,width=10)
        button_list.append(my_button)
        my_button.grid(row = row, column = column)
        column += 1
    column = 0
    row += 1



def xClick(event, x):
    print("Left Click")
    button_list[x].configure(bg="green", text="X")
    button_list[x].unbind("<Button-1>")
    button_list[x].unbind("<Button-3>")
    set_x.add(x)
    winner(set_x, "X")


def oClick(event, o):
    print("Right Click")
    button_list[o].config(bg="red", text="O")
    button_list[o].unbind("<Button-1>")
    button_list[o].unbind("<Button-3>")
    set_o.add(o)
    winner(set_o, "O")

for i in range(board_size**2):
    def make_lambda_1(x):
        return lambda ev:xClick(ev,x)
    def make_lambda_2(y):
        return lambda ev:oClick(ev,y)
    button_list[i].bind("<Button-1>" , make_lambda_1(i))
    button_list[i].bind("<Button-3>" , make_lambda_2(i))

def winner(my_set, game_winner):
    for i in winning_sets:
        if i.issubset(my_set):
            print("Winner is: ", game_winner)
            messagebox.showinfo("Congratulations!!!", f"Winner is player {game_winner}!")


tk.mainloop()