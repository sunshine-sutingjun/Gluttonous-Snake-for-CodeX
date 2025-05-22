import tkinter as tk
from typing import Optional

from game.board import Board
from game.snake import Snake, DIRECTION_VECTORS
from game.food import Food


CELL_SIZE = 20
UPDATE_DELAY = 150  # milliseconds


class Game:
    def __init__(self, root: tk.Tk) -> None:
        self.root = root
        self.board = Board(20, 20)
        self.snake = Snake(self.board)
        self.food = Food(self.board, self.snake)
        self.score = 0
        self.paused = False
        self.running = True

        root.title("Gluttonous Snake")
        self.canvas = tk.Canvas(
            root,
            width=self.board.width * CELL_SIZE,
            height=self.board.height * CELL_SIZE,
            bg="black",
        )
        self.canvas.pack()
        self.score_var = tk.StringVar(value=f"Score: {self.score}")
        self.label = tk.Label(root, textvariable=self.score_var)
        self.label.pack()

        root.bind("<KeyPress>", self.on_key_press)
        self.draw()
        self.update()

    def on_key_press(self, event: tk.Event) -> None:
        key = event.keysym
        if key.lower() == "p":
            self.paused = not self.paused
            return
        if key in DIRECTION_VECTORS:
            self.snake.set_direction(key)

    def update(self) -> None:
        if not self.paused:
            self.snake.move()
            if self.snake.body[0] == self.food.position:
                self.snake.grow()
                self.food.respawn()
                self.score += 1
                self.score_var.set(f"Score: {self.score}")
            if self.snake.collides():
                self.running = False
        self.draw()
        if self.running:
            self.root.after(UPDATE_DELAY, self.update)
        else:
            self.canvas.create_text(
                self.board.width * CELL_SIZE // 2,
                self.board.height * CELL_SIZE // 2,
                text="Game Over",
                fill="red",
                font=("Arial", 24),
            )

    def draw(self) -> None:
        self.canvas.delete("all")
        # draw food
        fx, fy = self.food.position
        self.canvas.create_rectangle(
            fx * CELL_SIZE,
            fy * CELL_SIZE,
            (fx + 1) * CELL_SIZE,
            (fy + 1) * CELL_SIZE,
            fill="yellow",
        )
        # draw snake
        for x, y in self.snake.body:
            self.canvas.create_rectangle(
                x * CELL_SIZE,
                y * CELL_SIZE,
                (x + 1) * CELL_SIZE,
                (y + 1) * CELL_SIZE,
                fill="green",
            )


def main() -> None:
    root = tk.Tk()
    Game(root)
    root.mainloop()


if __name__ == "__main__":
    main()
