# Guess-the-Number Game

## Overview

This project is a simple "Guess the Number" game implemented in Python. The game generates a random number within a specified range and challenges the player to guess that number within a limited number of attempts. The player can also earn extra lives by watching ads.

## Project Structure

The project consists of a Python script that contains the game logic. Here's an overview of the key components:

- `generate_random_number()`: This function generates a random number within a specified range.

- `get_extra_life(watch_ad_limit, random_num)`: This function allows the player to earn extra lives by watching ads. It provides options to watch ads or decline, affecting the number of remaining attempts.

- `play_guess_game()`: The main game loop where the player makes guesses and is provided feedback on whether the guess is too high or too low. The player wins if they guess the correct number within the allowed number of attempts.

## Configuration

- `LOWER_NUM` and `HIGHER_NUM`: Define the range within which the random number is generated.

- `NUMBER_OF_GUESSES`: Specifies the number of guesses allowed to win the game.

- `WATCH_AD_LIMIT`: Sets the limit on the number of times a player can watch ads to earn extra lives.

## How to Play

1. Run the script
2. The game will prompt you to guess a number within the specified range.
3. You have a limited number of attempts to guess the correct number.
4. You can choose to watch ads to earn extra lives or decline.
5. Continue guessing until you either win or run out of attempts.

## Usage

To play the game, execute the Python script in your terminal:

```bash
python main.py
```

## Ideas to Implement

1. Difficulty Levels
2. High Score System 
3. Timer
4. Multiplayer mode

