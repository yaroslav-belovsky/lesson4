import tkinter as tk
import random

CELL_SIZE = 40
ROWS = 13
COLS = 15

class BombermanGame:
    def __init__(self, root):
        self.root = root
        self.root.title("BomberMan")
        self.canvas = tk.Canvas(root, width=COLS*CELL_SIZE, height=ROWS*CELL_SIZE, bg='black')
        self.canvas.pack()

        self.restart_button = tk.Button(root, text="Restart", command=self.restart_game)
        self.restart_button.pack()

        self.initialize_game()

    def initialize_game(self):
        self.grid = [['empty' for _ in range(COLS)] for _ in range(ROWS)]
        self.player_pos = [1, 1]
        self.bombs = []
        self.enemies = []
        self.game_over = False
        self.win = False

        self.place_walls()
        self.place_boxes()
        self.spawn_enemies(3)
        self.draw_grid()
        self.root.bind("<Key>", self.key_pressed)
        self.move_enemies()

    def restart_game(self):
        self.canvas.delete("all")
        self.initialize_game()

    def place_walls(self):
        for row in range(ROWS):
            for col in range(COLS):
                if row == 0 or row == ROWS - 1 or col == 0 or col == COLS - 1 or (row % 2 == 0 and col % 2 == 0):
                    self.grid[row][col] = 'wall'

    def place_boxes(self):
        for row in range(1, ROWS-1):
            for col in range(1, COLS-1):
                if self.grid[row][col] == 'empty' and random.random() < 0.3:
                    if (row, col) not in [(1, 1), (1, 2), (2, 1)]:
                        self.grid[row][col] = 'box'

    def spawn_enemies(self, count):
        while len(self.enemies) < count:
            x, y = random.randint(1, COLS-2), random.randint(1, ROWS-2)
            if self.grid[y][x] == 'empty' and [x, y] != self.player_pos:
                self.enemies.append([x, y])

    def draw_grid(self):
        self.canvas.delete("all")
        for row in range(ROWS):
            for col in range(COLS):
                x1 = col * CELL_SIZE
                y1 = row * CELL_SIZE
                x2 = x1 + CELL_SIZE
                y2 = y1 + CELL_SIZE
                if self.grid[row][col] == 'wall':
                    self.canvas.create_rectangle(x1, y1, x2, y2, fill='gray')
                elif self.grid[row][col] == 'box':
                    self.canvas.create_rectangle(x1, y1, x2, y2, fill='brown')
        if not self.game_over and not self.win:
            px, py = self.player_pos
            x1 = px * CELL_SIZE
            y1 = py * CELL_SIZE
            x2 = x1 + CELL_SIZE
            y2 = y1 + CELL_SIZE
            self.canvas.create_oval(x1+5, y1+5, x2-5, y2-5, fill='blue')

        for (bx, by, _) in self.bombs:
            x1 = bx * CELL_SIZE
            y1 = by * CELL_SIZE
            x2 = x1 + CELL_SIZE
            y2 = y1 + CELL_SIZE
            self.canvas.create_oval(x1+10, y1+10, x2-10, y2-10, fill='red')

        for ex, ey in self.enemies:
            x1 = ex * CELL_SIZE
            y1 = ey * CELL_SIZE
            x2 = x1 + CELL_SIZE
            y2 = y1 + CELL_SIZE
            self.canvas.create_oval(x1+8, y1+8, x2-8, y2-8, fill='green')

        if self.game_over:
            self.canvas.create_text(COLS*CELL_SIZE//2, ROWS*CELL_SIZE//2, text="GAME OVER", font=("Arial", 32), fill="red")
        elif self.win:
            self.canvas.create_text(COLS*CELL_SIZE//2, ROWS*CELL_SIZE//2, text="YOU WIN!", font=("Arial", 32), fill="yellow")

    def key_pressed(self, event):
        if self.game_over or self.win:
            return
        dx, dy = 0, 0
        key = event.keysym
        if key in ['Up', 'w']:
            dy = -1
        elif key in ['Down', 's']:
            dy = 1
        elif key in ['Left', 'a']:
            dx = -1
        elif key in ['Right', 'd']:
            dx = 1
        elif key == 'space':
            self.place_bomb()
            return

        new_x = self.player_pos[0] + dx
        new_y = self.player_pos[1] + dy
        if 0 <= new_x < COLS and 0 <= new_y < ROWS:
            if self.grid[new_y][new_x] in ['empty']:
                self.player_pos = [new_x, new_y]
        self.check_game_over()
        self.check_win_condition()
        self.draw_grid()

    def place_bomb(self):
        x, y = self.player_pos
        if (x, y) not in [(bx, by) for bx, by, _ in self.bombs]:
            self.bombs.append((x, y, self.root.after(2000, lambda: self.explode_bomb(x, y))))
        self.draw_grid()

    def explode_bomb(self, x, y):
        directions = [(0,0), (1,0), (-1,0), (0,1), (0,-1)]
        affected_positions = [(x + dx, y + dy) for dx, dy in directions if 0 <= x + dx < COLS and 0 <= y + dy < ROWS]

        for nx, ny in affected_positions:
            if self.grid[ny][nx] == 'box':
                self.grid[ny][nx] = 'empty'
            if [nx, ny] == self.player_pos:
                self.game_over = True

        self.enemies = [enemy for enemy in self.enemies if tuple(enemy) not in affected_positions]

        self.check_win_condition()
        self.bombs = [b for b in self.bombs if b[0] != x or b[1] != y]
        self.draw_grid()

    def move_enemies(self):
        if self.game_over or self.win:
            return
        for enemy in self.enemies:
            directions = [(0,1), (0,-1), (1,0), (-1,0)]
            random.shuffle(directions)
            for dx, dy in directions:
                new_x = enemy[0] + dx
                new_y = enemy[1] + dy
                if 0 <= new_x < COLS and 0 <= new_y < ROWS:
                    if self.grid[new_y][new_x] == 'empty':
                        enemy[0], enemy[1] = new_x, new_y
                        break
        self.check_game_over()
        self.draw_grid()
        self.root.after(1000, self.move_enemies)

    def check_game_over(self):
        for ex, ey in self.enemies:
            if [ex, ey] == self.player_pos:
                self.game_over = True

    def check_win_condition(self):
        if len(self.enemies) == 0:
            self.win = True

if __name__ == "__main__":
    root = tk.Tk()
    game = BombermanGame(root)
    root.mainloop()
