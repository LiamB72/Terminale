grid = [[0,  0,  1,  0],
		[0,  0,  0,  0],
		[2,  0,  0,  4],
		[0, -1,  0,  0],
		[0,  3,  0,  0]]

robotSaved = []
nb_rows = 5
nb_cols = 4
nbRobot = {1:(0,3),2:(2,0),3:(4,1),4:(2,3)}

def bouger(direction:str):
    """Moves with the act of a letter.

    direction (str): N: North, S: South, O:Ouest, E:Est
    """
    if direction == "N":
        pass #go_North()
    elif direction == "S":
        pass #go_South()
    elif direction == "O":
        go_West()
    elif direction == "E":
        pass #go_East()
    else:
        print("Wrong letter!")

def go_West():
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
    if grid.index(n) == nbRobot[n]:
        return nbRobot[n]

    elif n in robotSaved:
        return 1

    return -1
    