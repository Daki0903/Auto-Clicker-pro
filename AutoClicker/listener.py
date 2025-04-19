import keyboard

class Listener:
    def __init__(self, stop_callback):
        self.stop_callback = stop_callback

    def listen(self):
        keyboard.wait('esc')
        self.stop_callback()
