
# Mastermind Game

This Python script implements a simple Mastermind game where two players take turns guessing each other's secret numbers.

## Table of Contents

- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Script Overview](#script-overview)
- [Customization](#customization)
- [Dependencies](#dependencies)
- [Contributing](#contributing)
- [License](#license)
- [Contact](#contact)

## Features

- **Random Number Generation**: Generates random secret numbers of specified length.
- **Feedback Mechanism**: Provides feedback on correct digits and positions after each guess.
- **Two-Player Mode**: Allows two players to take turns guessing each other's secret numbers.

## Installation

### Clone the Repository

First, clone the repository to your local machine:
```bash
git clone https://github.com/yourusername/mastermind-game.git
cd mastermind-game
```

### Install Dependencies

No external dependencies are needed to run this game.

## Usage

1. **Set Up**: 
    - Player 1 sets a secret number for Player 2 to guess.
    - Player 2 sets a secret number for Player 1 to guess.

2. **Guessing**: 
    - Players take turns guessing each other's secret numbers.
    - After each guess, feedback is provided regarding the correctness of digits and their positions.

3. **Winning**: 
    - The player who guesses the opponent's secret number with the fewest attempts wins.

## Script Overview

### `generate_number(length)`

Generates a random number of a specified length.

### `get_feedback(secret, guess)`

Provides feedback on the correctness of digits and positions in the guess compared to the secret number.

### `play_round(player_name, secret)`

Manages the gameplay for each player's turn, prompting for guesses and providing feedback until the correct number is guessed.

### `mastermind_game()`

Orchestrates the entire game, including setting up secret numbers for each player, playing rounds, and determining the winner.

## Customization

You can customize the length of the secret numbers and add more players or rounds as needed by modifying the `generate_number` and `mastermind_game` functions.

## Contributing

Contributions are welcome! If you have any ideas for improvement or would like to report a bug, feel free to open an issue or submit a pull request.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Contact

For any questions or suggestions, feel free to contact the repository owner at kunalgautam489@gmail.com.
