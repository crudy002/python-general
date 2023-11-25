import enum

class GridPosition(enum.Enum):
    EMPTY = 0,
    RED = 1,
    YELLOW = 2

class Grid:

    # Allow for variable dimensions of the grid on init
    def __init__(self, rows, columns):
        self._rows = rows
        self._columns = columns
        self._grid = None
        self.initGrid()

    def initGrid(self):
        # Initialize an empty grid
        self._grid = []

        # Iterate over rows
        for _ in range(self._rows):
            # Create a new row
            row = []

            # Iterate over columns
            for _ in range(self._columns):
                # Add an EMPTY position to the row
                row.append(GridPosition.EMPTY)

            # Add the row to the grid
            self._grid.append(row)

    def getGrid(self) :
        return self._grid

    def getColumnCount(self) :
        return self._columns
    '''
    def getRowCount(self) :
        return self._rows
    '''
    def printGrid(self):
        # Print the grid
        for row in self._grid:

            # Print the row of the grid
            print('| ' + ' | '.join(str(position.value[0]) for position in row) + ' |')

            # Print a separator line between rows
            print('-' * (4 * self._columns + 1))

    def placePiece(self, column, piece):

        if column < 0 or column >= self._columns:
            raise ValueError('Invalid Column')
        if piece == GridPosition.EMPTY :
            raise ValueError('Invalid Piece')
        # Iterate over the rows from bottom to top
        for row in range(self._rows-1, -1, -1):
            # Check if the current position is empty
            if self._grid[row][column] == GridPosition.EMPTY:
                # Place the piece in the empty position and return the row
                self._grid[row][column] = piece
                return row

    def main(self):
        self.initGrid()
        self.printGrid()

if __name__ == "__main__":
    game = Grid(6, 7)
    game.main()


