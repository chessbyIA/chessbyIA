class GameManager:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(GameManager, cls).__new__(cls)
            cls._instance.game_state = "Initializing"
        return cls._instance

    def start_game(self):
        self.game_state = "Started"
        print("Game Started")

    def end_game(self):
        self.game_state = "Ended"
        print("Game Ended")