UP = 0
DOWN = 1
LEFT = 2
RIGHT = 3

UP_LEFT = 4
UP_RIGHT = 5
DOWN_LEFT = 6
DOWN_RIGHT = 7

MOVES = [
    (-1, 0),  # UP
    (1, 0),  # DOWN
    (0, -1),  # LEFT
    (0, 1),  # RIGHT
    (-1, -1),  # UP LEFT
    (-1, 1),  # UP RIGHT
    (1, -1),  # DOWN LEFT
    (1, 1),  # DOWN RIGHT
]


class World:
    def __init__(self, rows, cols):

        self.rows = rows
        self.cols = cols

        # 0 = Empty
        # 1 = Wall
        # 2 = Goal
        self.grid = [[0 for _ in range(cols)] for _ in range(rows)]

        self.start = (0, 0)
        self.goal = (rows - 1, cols - 1)

        # Put goal in the grid
        self.grid[self.goal[0]][self.goal[1]] = 2
        self.create_maze()

    # -----------------------
    # Is inside map?
    # -----------------------
    def inside(self, row, col):

        return 0 <= row < self.rows and 0 <= col < self.cols

    # -----------------------
    # Add a wall
    # -----------------------
    def add_wall(self, row, col):

        if self.inside(row, col):
            self.grid[row][col] = 1

    # -----------------------
    # Is wall?
    # -----------------------
    def is_wall(self, row, col):

        return self.grid[row][col] == 1

    def step(self, state, action):

        row, col = state

        dr, dc = MOVES[action]

        new_row = row + dr
        new_col = col + dc

        # ---------------------------------
        # Outside map
        # ---------------------------------

        if not self.inside(new_row, new_col):
            return state, -20, False

        # ---------------------------------
        # Hit wall
        # ---------------------------------

        if self.is_wall(new_row, new_col):
            return state, -50, False

        next_state = (new_row, new_col)

        # ---------------------------------
        # Goal
        # ---------------------------------

        if self.is_goal(new_row, new_col):
            return next_state, 100, True

        # ---------------------------------
        # Normal movement
        # ---------------------------------

        return next_state, -1, False

    def create_maze(self):

        walls = [
            (1, 3),
            (1, 4),
            (1, 5),
            (2, 5),
            (3, 1),
            (3, 2),
            (3, 3),
            (4, 7),
            (5, 7),
            (6, 7),
            (7, 2),
            (7, 3),
            (7, 4),
            (8, 5),
            (8, 6),
        ]

        for row, col in walls:
            self.add_wall(row, col)

    # -----------------------
    # Is goal?
    # -----------------------
    def is_goal(self, row, col):

        return (row, col) == self.goal
