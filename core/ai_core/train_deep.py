from training_adapter import TrainingAdapter
from core.chess_core.game_engine import GameEngine
from deep_chess_ai import DQNAgent

import numpy as np

batch_size = 32

def train_dqn(agent, env, episodes):
    for e in range(episodes):
        state = env.reset()
        state = np.reshape(state, [1, agent.state_shape])
        total_reward = 0
        for time in range(500):
            action = agent.choose_action(state)
            next_state, reward, done = env.step(action)
            next_state = np.reshape(next_state, [1, agent.state_shape])
            agent.remember(state, action, reward, next_state, done)
            state = next_state
            total_reward += reward
            if done:
                print(f"Épisode: {e+1}/{episodes}, score: {total_reward}, epsilon: {agent.epsilon:.2}")
                break
            if len(agent.memory) > batch_size:
                agent.replay(batch_size)


env = TrainingAdapter(GameEngine())
state_size = env.state_shape 
action_size = env.action_size 
agent = DQNAgent(state_size, action_size)

train_dqn(agent, env, 1000)
