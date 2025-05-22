import random
from typing import Tuple

from .board import Board
from .snake import Snake


class Food:
    """Generate and hold the position of the food on the board."""

    def __init__(self, board: Board, snake: Snake):
        self.board = board
        self.snake = snake
        self.position: Tuple[int, int] = self._random_position()

    def _random_position(self) -> Tuple[int, int]:
        while True:
            pos = (
                random.randint(0, self.board.width - 1),
                random.randint(0, self.board.height - 1),
            )
            if pos not in self.snake.body:
                return pos

    def respawn(self) -> None:
        self.position = self._random_position()
