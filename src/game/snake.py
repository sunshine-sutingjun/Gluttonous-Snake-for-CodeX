from collections import deque
from typing import Deque, Tuple

from .board import Board

DIRECTION_VECTORS = {
    "Up": (0, -1),
    "Down": (0, 1),
    "Left": (-1, 0),
    "Right": (1, 0),
}


class Snake:
    """Logic for snake movement and growth."""

    def __init__(self, board: Board, init_length: int = 3):
        self.board = board
        center_x = board.width // 2
        center_y = board.height // 2
        self.body: Deque[Tuple[int, int]] = deque(
            [(center_x, center_y + i) for i in reversed(range(init_length))]
        )
        self.direction = "Up"
        self._grow_pending = 0

    def set_direction(self, new_direction: str) -> None:
        opposite = {
            "Up": "Down",
            "Down": "Up",
            "Left": "Right",
            "Right": "Left",
        }
        if (
            new_direction in DIRECTION_VECTORS
            and opposite[new_direction] != self.direction
        ):
            self.direction = new_direction

    def move(self) -> None:
        dx, dy = DIRECTION_VECTORS[self.direction]
        head_x, head_y = self.body[0]
        new_head = (head_x + dx, head_y + dy)
        self.body.appendleft(new_head)
        if self._grow_pending > 0:
            self._grow_pending -= 1
        else:
            self.body.pop()

    def grow(self) -> None:
        self._grow_pending += 1

    def collides(self) -> bool:
        head_x, head_y = self.body[0]
        if not (0 <= head_x < self.board.width and 0 <= head_y < self.board.height):
            return True
        if (head_x, head_y) in list(self.body)[1:]:
            return True
        return False
