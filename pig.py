import random

random.seed(0)


class Die:
    def roll(self):
        return random.randint(1, 6)


class Player:
    def __init__(self, name):
        self.name = name
        self.score = 0


class PigGame:
    def __init__(self):
        self.die = Die()
        self.players = []
        self.current_player = 0

    def setup_players(self):
        while True:
            try:
                number_of_players = int(input("How many players? "))
                if number_of_players >= 2:
                    break
                print("Please enter a number greater than or equal to 2.")
            except ValueError:
                print("Please enter a valid number.")

        for i in range(number_of_players):
            self.players.append(Player(f"Player {i + 1}"))

    def play(self):
        self.setup_players()

        while True:
            player = self.players[self.current_player]
            turn_total = 0

            print(f"\n{player.name}'s turn")
            print(f"Total score: {player.score}")

            while True:
                choice = input("Roll or hold? (r/h): ").lower()

                if choice == "r":
                    roll = self.die.roll()
                    print(f"Rolled: {roll}")

                    if roll == 1:
                        print("Turn over. No points earned.")
                        turn_total = 0
                        break

                    turn_total += roll
                    print(f"Turn total: {turn_total}")

                elif choice == "h":
                    player.score += turn_total
                    print(f"{player.name} score: {player.score}")
                    break

                else:
                    print("Invalid input. Please enter 'r' or 'h'.")

            if player.score >= 100:
                print(f"\n{player.name} wins!")
                break

            self.current_player = (self.current_player + 1) % len(self.players)


if __name__ == "__main__":
    game = PigGame()
    game.play()