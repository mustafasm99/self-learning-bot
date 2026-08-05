import sys
import pygame

from game.draw import Drawing
from game.world import World
from game.agent import Agent
from game.qlearning import QLearning


# =====================================================
# Initialize Pygame
# =====================================================

pygame.init()

WIDTH = 600
HEIGHT = 700
GRID_SIZE = 10
FPS = 20

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Q-Learning Game")

clock = pygame.time.Clock()


# =====================================================
# Create World
# =====================================================

world = World(GRID_SIZE, GRID_SIZE)

# =====================================================
# Create Objects
# =====================================================

drawing = Drawing(screen, WIDTH, HEIGHT, GRID_SIZE)

agent = Agent(world.start)
agent.initialize_pixels(drawing.cell_size, drawing.TOP_MARGIN)

brain = QLearning(world)


# =====================================================
# Variables
# =====================================================

episode = 1
done = False
running = True

agent.reset()


# =====================================================
# Main Loop
# =====================================================

while running:
    clock.tick(FPS)

    # ---------------------------------
    # Events
    # ---------------------------------

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # ---------------------------------
    # New Episode
    # ---------------------------------

    if done:
        brain.update_epsilon()

        episode += 1

        agent.reset()

        done = False

    # ---------------------------------
    # Current State
    # ---------------------------------

    # -------------------------------------------------
    # Update animation every frame
    # -------------------------------------------------

    agent.update()

    # -------------------------------------------------
    # Only think when robot finished moving
    # -------------------------------------------------

    if not agent.is_moving:
        state = agent.state()

        action = brain.choose_action(state)

        next_state, reward, done = world.step(state, action)

        brain.learn(state, action, reward, next_state)

        agent.set_position(next_state, drawing.cell_size, drawing.TOP_MARGIN)

        agent.add_reward(reward)

        # ---------------------------------
        # Update Agent
        # ---------------------------------

        agent.set_position(next_state, drawing.cell_size, drawing.TOP_MARGIN)
        agent.update()

        agent.add_reward(reward)

    # ---------------------------------
    # Draw
    # ---------------------------------

    drawing.draw(world, agent, brain, episode)

    pygame.display.flip()


# =====================================================
# Exit
# =====================================================

pygame.quit()
sys.exit()
