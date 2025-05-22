import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "src"))

import unittest

from game.board import Board
from game.snake import Snake


class TestSnake(unittest.TestCase):
    def test_snake_move(self):
        board = Board(10, 10)
        snake = Snake(board, init_length=1)
        snake.set_direction("Right")
        snake.move()
        self.assertEqual(snake.body[0], (board.width // 2 + 1, board.height // 2))

    def test_snake_grow(self):
        board = Board(10, 10)
        snake = Snake(board, init_length=1)
        snake.grow()
        snake.move()
        self.assertEqual(len(snake.body), 2)


if __name__ == "__main__":
    unittest.main()
