import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "src"))

import unittest

from game.board import Board
from game.snake import Snake
from game.food import Food


class TestFood(unittest.TestCase):
    def test_food_not_on_snake(self):
        board = Board(10, 10)
        snake = Snake(board, init_length=3)
        food = Food(board, snake)
        self.assertNotIn(food.position, snake.body)
        snake.move()
        food.respawn()
        self.assertNotIn(food.position, snake.body)


if __name__ == "__main__":
    unittest.main()
