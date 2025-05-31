import tkinter as tk
from tkinter import messagebox
import random

class TicTacToe:
    def __init__(self, root):
        self.root = root
        self.root.title("Хрестики проти комп'ютера")
        self.current_player = "X"
        self.board = ["" for _ in range(9)]

        self.buttons = []
        for i in range(9):
            button = tk.Button(root, text="", font=('Arial', 40), width=5, height=2,
                               command=lambda i=i: self.make_move(i))
            button.grid(row=i//3, column=i%3)
            self.buttons.append(button)

    def make_move(self, index):
        if self.board[index] == "" and self.current_player == "X" and not self.check_winner():
            self.board[index] = "X"
            self.buttons[index].config(text="X")
            if self.check_winner():
                messagebox.showinfo("Кінець гри", "Гравець X переміг!")
                self.reset_game()
            elif "" not in self.board:
                messagebox.showinfo("Кінець гри", "Нічия!")
                self.reset_game()
            else:
                self.current_player = "O"
                self.root.after(500, self.computer_move)

    def computer_move(self):
        index = self.best_move()
        if index is not None:
            self.board[index] = "O"
            self.buttons[index].config(text="O")
            if self.check_winner():
                messagebox.showinfo("Кінець гри", "Комп'ютер переміг!")
                self.reset_game()
            elif "" not in self.board:
                messagebox.showinfo("Кінець гри", "Нічия!")
                self.reset_game()
            else:
                self.current_player = "X"

    def best_move(self):
        # 1. Перевірка на перемогу комп'ютера
        for i in range(9):
            if self.board[i] == "":
                self.board[i] = "O"
                if self.check_winner():
                    self.board[i] = ""
                    return i
                self.board[i] = ""

        # 2. Блокування перемоги гравця
        for i in range(9):
            if self.board[i] == "":
                self.board[i] = "X"
                if self.check_winner():
                    self.board[i] = ""
                    return i
                self.board[i] = ""

        # 3. Вибір центру
        if self.board[4] == "":
            return 4

        # 4. Вибір кутів
        for i in [0, 2, 6, 8]:
            if self.board[i] == "":
                return i

        # 5. Вибір сторін
        for i in [1, 3, 5, 7]:
            if self.board[i] == "":
                return i

        return None

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
