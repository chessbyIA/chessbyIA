import random

class ChessAI:
    def __init__(self):
        self.q_table = {}

    def choose_move(self, state):
        return random.choice(self.get_possible_moves(state))

    def update(self, state, action, reward, next_state, done):
        pass

    def get_possible_moves(self, state):
        return [(0, 0, 1, 0)]
