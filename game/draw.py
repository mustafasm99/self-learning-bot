import pygame


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
                pygame.draw.rect(self.screen, self.GRASS, rect)

                if value == 1:
                    # Tree trunk
                    pygame.draw.rect(
                        self.screen,
                        self.TRUNK,
                        (rect.centerx - 4, rect.bottom - 18, 8, 16),
                    )

                    # Leaves

                    pygame.draw.circle(
                        self.screen,
                        self.TREE,
                        (rect.centerx, rect.centery - 5),
                        self.cell_size // 3,
                    )

                    pygame.draw.circle(
                        self.screen,
                        (55, 120, 55),
                        (rect.centerx - 10, rect.centery),
                        self.cell_size // 4,
                    )

                    pygame.draw.circle(
                        self.screen,
                        (55, 120, 55),
                        (rect.centerx + 10, rect.centery),
                        self.cell_size // 4,
                    )

                elif value == 2:
                    pygame.draw.circle(self.screen, self.GOAL, rect.center, 16)
                    pygame.draw.circle(self.screen, (255, 255, 255), rect.center, 6)

    def draw_agent(self, agent):
        x = int(agent.pixel_x)
        y = int(agent.pixel_y)

        # Body
        pygame.draw.circle(self.screen, (70, 120, 255), (x, y), 18)

        # Eyes
        pygame.draw.circle(self.screen, (255, 255, 255), (x - 6, y - 4), 3)

        pygame.draw.circle(self.screen, (255, 255, 255), (x + 6, y - 4), 3)

        pygame.draw.circle(self.screen, (0, 0, 0), (x - 6, y - 4), 1)

        pygame.draw.circle(self.screen, (0, 0, 0), (x + 6, y - 4), 1)

        # Antenna
        pygame.draw.line(self.screen, (40, 40, 40), (x, y - 18), (x, y - 28), 2)

        pygame.draw.circle(self.screen, (255, 80, 80), (x, y - 30), 3)

        # Smile
        pygame.draw.arc(self.screen, (30, 30, 30), (x - 8, y - 2, 16, 10), 0, 3.14, 2)

    # -------------------------------------
    # Draw everything
    # -------------------------------------
    def draw(self, world, agent, brain, episode):
        self.draw_background()

        self.draw_header(episode, agent, brain)

        self.draw_world(world)

        self.draw_grid()

        self.draw_agent(agent)
