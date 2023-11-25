from grid import Grid, GridPosition

class Game:
    def __init__(self, rows, columns):
        self.connect_four = Grid(rows, columns)

    def start_game(self):
        current_player = GridPosition.RED  # Start with RED player

        while True:
            self.connect_four.printGrid()

            try:
                column = int(input(f"Player {current_player.value[0]}, enter the column to place your piece (1-{self.connect_four.getColumnCount()}): ")) - 1

                # Place the piece and get the row where it was placed
                row = self.connect_four.placePiece(column, current_player)

                # Check for a win or a draw
                if self.connect_four.is_winner(current_player):
                    self.connect_four.printGrid()
                    print(f"Player {current_player.value[0]} wins!")
                    break
                elif self.connect_four.is_full():
                    self.connect_four.printGrid()
                    print("It's a draw!")
                    break

                # Switch to the other player for the next turn
                current_player = GridPosition.YELLOW if current_player == GridPosition.RED else GridPosition.RED

            except (ValueError, IndexError):
                print("Invalid input. Please try again.")

if __name__ == "__main__":
    game_instance = Game(rows=6, columns=7)
    game_instance.start_game()