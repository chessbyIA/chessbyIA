class GameObserver:
    def update(self, message):
        pass

class UserInterface(GameObserver):
    def update(self, message):
        print(f"UI Update: {message}")

class GameSubject:
    def __init__(self):
        self._observers = []

    def register_observer(self, observer):
        self._observers.append(observer)

    def notify_observers(self, message):
        for observer in self._observers:
            observer.update(message)