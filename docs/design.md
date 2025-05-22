# Game Design

This project implements a simple snake game using Tkinter. The game logic is
split from the UI so that it can be tested easily. The main components are:

- **Board** – defines the grid size of the game field.
- **Snake** – controls movement, growth and collision detection.
- **Food** – randomly spawns on the board avoiding the snake's body.

The UI draws these components on a Tkinter `Canvas` and handles user input. The
logic can be reused with another UI if desired.
