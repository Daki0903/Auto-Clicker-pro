import pyautogui
import time
import threading

class Clicker:
    def __init__(self, delay=0.01):
        self.delay = delay
        self.running = False
        self.thread = None

    def start(self):
        if not self.running:
            self.running = True
            self.thread = threading.Thread(target=self._run_click, daemon=True)
            self.thread.start()

    def _run_click(self):
        while self.running:
            pyautogui.click()
            if self.delay > 0:
                time.sleep(self.delay)

    def stop(self):
        self.running = False
