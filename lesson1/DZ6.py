import tkinter as tk
from tkinter import messagebox

class TicTacToe:
    def __init__(self, root):
        self.root = root
        self.root.title("Хрестики")
        self.current_player = "X"
        self.board = ["" for _ in range(9)]

        self.buttons = []
        for i in range(9):
            button = tk.Button(root, text="", font=('Arial', 40), width=5, height=2,
                               command=lambda i=i: self.make_move(i))
            button.grid(row=i//3, column=i%3)
            self.buttons.append(button)

    def make_move(self, index):
        if self.board[index] == "" and not self.check_winner():
            self.board[index] = self.current_player
            self.buttons[index].config(text=self.current_player)
            if self.check_winner():
                messagebox.showinfo("Кінець гри", f"Гравець {self.current_player} переміг!")
                self.reset_game()
            elif "" not in self.board:
                messagebox.showinfo("Кінець гри", "Нічия!")
                self.reset_game()
            else:
                self.current_player = "O" if self.current_player == "X" else "X"

    def check_winner(self):
        wins = [
            [0, 1, 2], [3, 4, 5], [6, 7, 8],  # rows
            [0, 3, 6], [1, 4, 7], [2, 5, 8],  # columns
            [0, 4, 8], [2, 4, 6]              # diagonals
        ]
        for line in wins:
            if self.board[line[0]] == self.board[line[1]] == self.board[line[2]] != "":
                return True
        return False

    def reset_game(self):
        self.board = ["" for _ in range(9)]
        for button in self.buttons:
            button.config(text="")
        self.current_player = "X"

if __name__ == "__main__":
    root = tk.Tk()
    game = TicTacToe(root)
    root.mainloop()
