# Alien Invasion: A Python Space Shooter

A classic arcade-style space shooter game built with Python and the Pygame 
library. This project is based on the "Alien Invasion" project from the 
book "Python Crash Course" by Eric Matthes. The player controls a spaceship 
at the bottom of the screen and must shoot down waves of incoming aliens.

## Gameplay Demo



## Features Implemented

### 🎮 Gameplay & Controls
* Player-controlled ship with continuous horizontal movement.
* Screen boundaries to keep the ship within the play area.
* Ability to fire projectiles using the `Spacebar`.
* Full-screen mode for an immersive experience.
* Pause and resume functionality with the `P` key.
* Keyboard shortcut to quit (`Escape`) the game.

### 👽 Enemies & AI
* A full fleet of aliens generated in a grid formation.
* Classic fleet movement: side-to-side and dropping down when an edge is reached.
* Aliens have the ability to shoot back at the player at level 2.

### 💥 Collision System & Lives
* Collision detection between player bullets and aliens.
* Collision detection between alien bullets and the player's ship.
* Collision detection between the alien fleet and the player's ship.
* A life system where the player starts with a set number of ships.
* Game over condition if an alien reaches the bottom of the screen or the player loses all lives.

### 📈 Scoring & Progression
* Real-time scoreboard UI.
* Points awarded for each alien destroyed.
* Persistent high score that is saved to a local file and loaded between game sessions.
* Leveling system that increments each time the fleet is cleared.
* Dynamic difficulty curve:
    * Game speed (ship, bullets, aliens) increases with each level.
    * Point value per alien increases with each level.
    * Alien firing rate increases with each level.

### 🎨 User Interface (UI)
* An interactive "Play" button to start the game from a main menu screen.
* On-screen display for the current score, high score, and current level.
* Visual indicator for remaining lives (ship icons).
* Mouse cursor is hidden during active gameplay for better immersion.
* On-screen instructions for game controls.

## Technologies Used
* **Language:** Python 3
* **Library:** Pygame

## Setup and Installation

To clone and run this project locally, follow these steps:

1.  **Clone the repository:**
    ```sh
    git clone [https://github.com/roxanavnunez/alien-invasion.git]
    ```
2.  **Navigate to the project directory:**
    ```sh
    cd <PROJECT_DIRECTORY_NAME>
    ```
3.  **(Recommended) Create and activate a virtual environment:**
    ```sh
    # For macOS/Linux
    python3 -m venv venv
    source venv/bin/activate

    # For Windows
    python -m venv venv
    venv\Scripts\activate
    ```
4.  **Install the dependencies:**
    ```sh
    pip install pygame
    ```
5.  **Run the game:**
    ```sh
    python alien_invasion.py
    ```

## How to Play

* **Move Ship:** `Left Arrow` / `Right Arrow` keys
* **Shoot:** `Spacebar`
* **Pause/Resume:** `P` key
* **Quit Game:** `Escape` key

## License

Distributed under the MIT License. See `LICENSE` for more information.