import tkinter as tk
import random

# Параметри екрану
WIDTH = 800
HEIGHT = 300
GROUND = HEIGHT - 50
DINO_WIDTH = 40
DINO_HEIGHT = 40
CACTUS_WIDTH = 20
CACTUS_HEIGHT = 40
INITIAL_SPEED = 10

class DinoGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Google Dino")
        self.canvas = tk.Canvas(root, width=WIDTH, height=HEIGHT, bg="white")
        self.canvas.pack()

        self.running = True  # <- Виправлено: перенесено сюди
        self.speed = INITIAL_SPEED
        self.score = 0

        self.canvas.create_line(0, GROUND, WIDTH, GROUND, fill="black")

        # Динозавр
        self.dino_color_toggle = True
        self.dino = self.canvas.create_rectangle(50, GROUND - DINO_HEIGHT, 50 + DINO_WIDTH, GROUND, fill="gray")

        # Перешкоди
        self.obstacles = []

        # Хмари
        self.clouds = []

        # Кнопка перезапуску
        self.restart_button = None

        # Лічильник
        self.score_text = self.canvas.create_text(WIDTH - 100, 30, text="Score: 0", font=("Arial", 16), fill="black")

        # Стани
        self.is_jumping = False
        self.jump_speed = 0
        self.gravity = 2

        # Клавіші
        self.root.bind("<space>", self.jump)

        # Запуск
        self.spawn_obstacle()
        self.spawn_bird()
        self.spawn_cloud()
        self.update()
        self.update_score()
        self.animate_dino()

    def jump(self, event=None):
        if not self.is_jumping:
            self.is_jumping = True
            self.jump_speed = -20

    def spawn_obstacle(self):
        if not self.running:
            return
        x = WIDTH
        y = GROUND
        cactus = self.canvas.create_rectangle(x, y - CACTUS_HEIGHT, x + CACTUS_WIDTH, y, fill="green")
        self.obstacles.append(cactus)
        self.root.after(random.randint(1200, 1800), self.spawn_obstacle)

    def spawn_bird(self):
        if not self.running:
            return
        x = WIDTH
        y = GROUND - random.choice([DINO_HEIGHT + 10, DINO_HEIGHT + 30])
        bird = self.canvas.create_oval(x, y - 20, x + 30, y, fill="black")
        self.obstacles.append(bird)
        self.root.after(random.randint(3000, 5000), self.spawn_bird)

    def spawn_cloud(self):
        if not self.running:
            return
        x = WIDTH
        y = random.randint(20, 100)
        cloud = self.canvas.create_oval(x, y, x + 60, y + 30, fill="lightgray", outline="")
        self.clouds.append(cloud)
        self.root.after(random.randint(3000, 6000), self.spawn_cloud)

    def animate_dino(self):
        if not self.running:
            return
        self.canvas.itemconfig(self.dino, fill="gray" if self.dino_color_toggle else "darkgray")
        self.dino_color_toggle = not self.dino_color_toggle
        self.root.after(150, self.animate_dino)

    def update_score(self):
        if not self.running:
            return
        self.score += 1
        self.canvas.itemconfig(self.score_text, text=f"Score: {self.score}")
        if self.score % 100 == 0:
            self.speed += 1
        self.root.after(100, self.update_score)

    def check_collision(self):
        dino_coords = self.canvas.coords(self.dino)
        for obs in self.obstacles:
            obs_coords = self.canvas.coords(obs)
            if self._overlap(dino_coords, obs_coords):
                self.running = False
                self.canvas.create_text(WIDTH // 2, HEIGHT // 2, text="Game Over", font=("Arial", 24), fill="red")
                self.show_restart_button()

    def _overlap(self, rect1, rect2):
        return not (
            rect1[2] < rect2[0] or
            rect1[0] > rect2[2] or
            rect1[3] < rect2[1] or
            rect1[1] > rect2[3]
        )

    def update(self):
        if not self.running:
            return

        # Рух хмар
        for cloud in self.clouds:
            self.canvas.move(cloud, -1, 0)
        self.clouds = [c for c in self.clouds if self.canvas.coords(c)[2] > 0]

        # Рух перешкод
        for obs in self.obstacles:
            self.canvas.move(obs, -self.speed, 0)
        self.obstacles = [obs for obs in self.obstacles if self.canvas.coords(obs)[2] > 0]

        # Стрибок
        if self.is_jumping:
            self.canvas.move(self.dino, 0, self.jump_speed)
            self.jump_speed += self.gravity
            coords = self.canvas.coords(self.dino)
            if coords[3] >= GROUND:
                self.canvas.move(self.dino, 0, GROUND - coords[3])
                self.is_jumping = False

        self.check_collision()
        self.root.after(30, self.update)

    def show_restart_button(self):
        if not self.restart_button:
            self.restart_button = tk.Button(self.root, text="Restart", command=self.restart_game)
            self.restart_button.place(x=WIDTH // 2 - 40, y=HEIGHT // 2 + 30)

    def restart_game(self):
        self.canvas.delete("all")
        if self.restart_button:
            self.restart_button.destroy()
            self.restart_button = None
        self.__init__(self.root)

if __name__ == "__main__":
    root = tk.Tk()
    game = DinoGame(root)
    root.mainloop()
