import random
import sys


class RPS:
    def __init__(self):
        print("Welcome to Rock Paper Scissors game\n")

        self.moves: dict = {'rock': '🪨', 'paper': '📜', 'scissors': '✂️'}
        self.valid_moves: list[str] = list(self.moves.keys())
        self.ai_score = 0
        self.user_score = 0

    def play_game(self):
        user_move: str = input("Rock, paper or scissors (or 'exit' to quit): ").lower()

        if user_move == "exit":
            print("Thanks for playing")
            sys.exit()

        if user_move not in self.valid_moves:
            print("Invalid move. Please choose from 'rock,' 'paper,' or 'scissors")
            return self.play_game()

        ai_move: str = random.choice(self.valid_moves)

        self.display_moves(user_move, ai_move)
        winner: str = self.check_moves(user_move, ai_move)
        self.update_score(winner)
        self.display_score()

    def display_moves(self, user_move, ai_move):
        print("\n-----")
        print(f"User move:{self.moves[user_move]}")
        print(f"AI move:{self.moves[ai_move]}")
        print("-----\n")

    @staticmethod
    def check_moves(user_move, ai_move):
        if user_move == ai_move:
            print("It's a Tie\n")
            return "tie"
        elif (user_move == "rock" and ai_move == "scissors") or \
                (user_move == "scissors" and ai_move == "paper") or \
                (user_move == "paper" and ai_move == "rock"):
            print("You Won\n")
            return "user"
        else:
            print("You Lose\n")
            return "ai"

    def update_score(self, winner):
        if winner == "ai":
            self.ai_score += 1
        elif winner == "user":
            self.user_score += 1

    def display_score(self):
        print("---------")
        print("user | ai")
        print(f"{self.user_score:^4} | {self.ai_score:^2}")
        print("---------")


if __name__ == '__main__':
    rps = RPS()

    while True:
        rps.play_game()
