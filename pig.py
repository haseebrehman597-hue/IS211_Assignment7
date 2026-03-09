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
        self.players = [Player("Player 1"), Player("Player 2")]
        self.die = Die()
        self.current_player = 0

    def play(self):

        while True:

            player = self.players[self.current_player]
            turn_total = 0

            print(f"\n{player.name}'s turn")
            print(f"Total score: {player.score}")

            while True:

                choice = input("Roll or hold? (r/h): ")

                if choice == 'r':

                    roll = self.die.roll()
                    print(f"Rolled: {roll}")

                    if roll == 1:
                        print("Turn over. No points earned.")
                        turn_total = 0
                        break

                    else:
                        turn_total += roll
                        print(f"Turn total: {turn_total}")

                elif choice == 'h':

                    player.score += turn_total
                    print(f"{player.name} score: {player.score}")
                    break

            if player.score >= 100:
                print(f"\n{player.name} wins!")
                break

            self.current_player = 1 - self.current_player


if __name__ == "__main__":
    game = PigGame()
    game.play()