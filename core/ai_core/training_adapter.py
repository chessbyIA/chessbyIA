class TrainingAdapter:
    def __init__(self, game_engine):
        self.game_engine = game_engine

    def reset(self):
        self.game_engine.initialize_game()
        return self.get_state()

    def step(self, from_pos, to_pos):
        self.game_engine.move_piece(from_pos, to_pos)
        next_state = self.get_state()
        done = self.game_engine.check_status()
        reward = self.evaluate_action(from_pos, to_pos, done)
        return next_state, reward, done

    def get_state(self):
        return self.game_engine.chess_board.get_board_state()

    def evaluate_action(self, from_pos, to_pos, done):
        if done:
            if self.game_engine.checkmate:
                return 1
            elif self.game_engine.stalemate:
                return 0.5 
        return -0.1 

    def is_game_over(self):
        return self.game_engine.is_game_over()
