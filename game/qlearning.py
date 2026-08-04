import random


class QLearning:

    def __init__(self, world):

        self.world = world

        self.alpha = 0.1
        self.gamma = 0.95
        self.epsilon = 1.0

        self.min_epsilon = 0.05
        self.epsilon_decay = 0.995

        self.actions = 8

        self.q_table = {}

        self.create_q_table()

    # -----------------------------------
    # Create Q Table
    # -----------------------------------

    def create_q_table(self):

        for row in range(self.world.rows):

            for col in range(self.world.cols):

                self.q_table[(row, col)] = [

                    0.0 for _ in range(self.actions)

                ]

    # -----------------------------------
    # Choose Action
    # -----------------------------------

    def choose_action(self, state):

        # Exploration

        if random.random() < self.epsilon:

            return random.randint(0, self.actions - 1)

        # Exploitation

        values = self.q_table[state]

        return values.index(max(values))

    # -----------------------------------
    # Learn
    # -----------------------------------

    def learn(

        self,
        state,
        action,
        reward,
        next_state

    ):

        current_q = self.q_table[state][action]

        max_future_q = max(

            self.q_table[next_state]

        )

        new_q = current_q + self.alpha * (

            reward +

            self.gamma * max_future_q -

            current_q

        )

        self.q_table[state][action] = new_q

    # -----------------------------------
    # Decay Exploration
    # -----------------------------------

    def update_epsilon(self):

        if self.epsilon > self.min_epsilon:

            self.epsilon *= self.epsilon_decay

    # -----------------------------------
    # Best Action
    # -----------------------------------

    def best_action(self, state):

        values = self.q_table[state]

        return values.index(max(values))