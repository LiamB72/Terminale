grid = [[0,  0,  1,  0],
		[0,  0,  0,  0],
		[2,  0,  0,  4],
		[0, -1,  0,  0],
		[0,  3,  0,  0]]

robotSaved = []
nb_rows = 5
nb_cols = 4

def go_west():
    for row in range(nb_rows):
        for col in range(nb_cols):
            contentCase = grid[row][col]

            if contentCase > 0:
                grid[row][col] = 0

                if col > 0:
                    if grid[row][col - 1] == -1:
                        robotSaved.append(contentCase)

                    else:
                        grid[row][col - 1] = contentCase

def robotStatus(n:int) -> int | tuple:
    for row in range(nb_rows):
        for col in range(nb_cols):

            if n == grid[row][col]:
                return row, col # Returns a tuple of the Robot's Coordinates in the grid.

    if n in robotSaved:
        return 1 # If robot ain't in the grid but in the saved list, return 1

    return -1 # Returns whenever neither of both previous cases aren't true.
