from chess_ai import ChessAI
from training_adapter import TrainingAdapter
from core.chess_core.game_engine import GameEngine

def train_ai(ai_agent, adapter, episodes):
    for episode in range(episodes):
        state = adapter.reset()
        done = False
        total_reward = 0

        while not done:
            from_pos, to_pos = ai_agent.choose_move(state) 
            next_state, reward, done = adapter.step(from_pos, to_pos)
            ai_agent.update(state, (from_pos, to_pos), reward, next_state, done)
            state = next_state
            total_reward += reward

        print(f"Épisode {episode + 1}: Récompense totale = {total_reward}")

# Création des instances
game_engine = GameEngine()
adapter = TrainingAdapter(game_engine)
ai_agent = ChessAI()

# Lancement de l'entraînement
train_ai(ai_agent, adapter, 100)  # Entraîner sur 100 épisodes par exemple
