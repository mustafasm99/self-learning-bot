import pygame
import os
from game.animation import Animation


class Drawing:
    def __init__(self, screen, width, height, grid_size):

        self.screen = screen
        self.TOP_MARGIN = 100
        self.font = pygame.font.SysFont("consolas", 22)

        self.width = width
        self.height = height

        self.grid_size = grid_size

        self.cell_size = width // grid_size

        # Colors
        self.WHITE = (245, 245, 245)
        self.BLACK = (40, 40, 40)
        self.GRAY = (170, 170, 170)
        self.RED = (220, 60, 60)
        self.GREEN = (50, 180, 80)
        self.BLUE = (60, 120, 255)
        self.DARK = (35, 35, 35)
        self.GRASS = (119, 190, 87)
        self.DIRT = (175, 132, 82)
        self.TREE = (45, 95, 50)
        self.TRUNK = (101, 67, 33)
        self.STONE = (90, 90, 90)
        self.GOAL = (255, 215, 0)

        asset_path = os.path.join("assets")
        self.grass = pygame.image.load(
            os.path.join(asset_path, "tree", "grass.png")
        ).convert_alpha()

        self.grass = pygame.transform.scale(
            self.grass, (self.cell_size, self.cell_size)
        )

        self.tree = pygame.image.load(
            os.path.join(asset_path, "wall", "00.png")
        ).convert_alpha()

        self.tree = pygame.transform.scale(self.tree, (self.cell_size, self.cell_size))

        self.battery = pygame.image.load(
            os.path.join(asset_path, "goal", "battery.png")
        ).convert_alpha()

        self.battery = pygame.transform.scale(self.battery, (self.cell_size, self.cell_size))

        self.robot_idle = Animation(
            "assets/robot/idle.gif", (self.cell_size, self.cell_size)
        )

        self.robot_walk = Animation(
            "assets/robot/run.gif", (self.cell_size, self.cell_size)
        )

    # -------------------------------------
    # Draw the background
    # -------------------------------------
    def draw_header(self, episode, agent, brain):

        # Background
        pygame.draw.rect(self.screen, self.DARK, (0, 0, self.width, self.TOP_MARGIN))

        # Left column
        left = [f"Episode : {episode}", f"Steps   : {agent.steps}"]

        # Right column
        right = [f"Reward : {agent.total_reward}", f"Explore: {brain.epsilon:.3f}"]

        y = 18

        for text in left:
            surface = self.font.render(text, True, (255, 255, 255))

            self.screen.blit(surface, (20, y))

            y += 35

        y = 18

        for text in right:
            surface = self.font.render(text, True, (255, 255, 255))

            self.screen.blit(surface, (320, y))

            y += 35

    def draw_background(self):

        self.screen.fill((95, 170, 90))

    # -------------------------------------
    # Draw the grid
    # -------------------------------------
    def draw_grid(self):

        for row in range(self.grid_size):
            for col in range(self.grid_size):
                rect = pygame.Rect(
                    col * self.cell_size,
                    self.TOP_MARGIN + row * self.cell_size,
                    self.cell_size,
                    self.cell_size,
                )

                pygame.draw.rect(self.screen, self.GRAY, rect, 1)

    def draw_world(self, world):

        for row in range(world.rows):
            for col in range(world.cols):
                value = world.grid[row][col]

                rect = pygame.Rect(
                    col * self.cell_size,
                    self.TOP_MARGIN + row * self.cell_size,
                    self.cell_size,
                    self.cell_size,
                )
                self.screen.blit(self.grass, (rect.x, rect.y))

                if value == 1:
                    # Tree trunk
                    self.screen.blit(self.tree, rect.topleft)

                elif value == 2:
                    # Battery
                    self.screen.blit(self.battery, rect.topleft)

    def draw_agent(self, agent):
        x = int(agent.pixel_x - self.cell_size / 2)
        y = int(agent.pixel_y - self.cell_size / 2)

        if agent.is_moving:
            self.robot_walk.update()

            image = self.robot_walk.get_frame()

        else:
            self.robot_idle.update()

            image = self.robot_idle.get_frame()

        self.screen.blit(image, (x, y))

    # -------------------------------------
    # Draw everything
    # -------------------------------------
    def draw(self, world, agent, brain, episode):
        self.draw_background()

        self.draw_header(episode, agent, brain)

        self.draw_world(world)

        # self.draw_grid()

        self.draw_agent(agent)
