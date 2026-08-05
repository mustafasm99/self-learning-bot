class Agent:
    def __init__(self, start):

        self.start = start

        self.position = start

        self.pixel_x = 0
        self.pixel_y = 0

        self.target_x = 0
        self.target_y = 0

        self.speed = 6

        self.total_reward = 0
        self.steps = 0

        self.is_moving = False

    # -----------------------
    # Reset every episode
    # -----------------------
    def reset(self):

        self.position = self.start

        self.total_reward = 0

        self.steps = 0

    # -----------------------
    # Current State
    # -----------------------
    def state(self):

        return self.position

    # -----------------------
    # Move Agent
    # -----------------------
    def move(self, new_position):

        self.position = new_position

        self.steps += 1

    # -----------------------
    # Add Reward
    # -----------------------
    def add_reward(self, reward):

        self.total_reward += reward

    def initialize_pixels(self, cell_size, top_margin):

        row, col = self.position

        self.pixel_x = col * cell_size + cell_size / 2

        self.pixel_y = top_margin + row * cell_size + cell_size / 2

        self.target_x = self.pixel_x
        self.target_y = self.pixel_y

    def set_position(self, position, cell_size, top_margin):

        self.position = position

        row, col = position

        self.target_x = col * cell_size + cell_size / 2
        self.target_y = top_margin + row * cell_size + cell_size / 2

        self.is_moving = True

        self.steps += 1

    def update(self):

        speed = 0.50

        self.pixel_x += (self.target_x - self.pixel_x) * speed
        self.pixel_y += (self.target_y - self.pixel_y) * speed

        dx = abs(self.target_x - self.pixel_x)
        dy = abs(self.target_y - self.pixel_y)

        if dx < 5 and dy < 5:
            self.pixel_x = self.target_x
            self.pixel_y = self.target_y

            self.is_moving = False
