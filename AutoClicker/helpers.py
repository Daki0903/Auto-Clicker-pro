import pyautogui
import time

def choose_position():
    print("Click anywhere on the screen to select a position (you have 5 seconds)...")
    time.sleep(5)
    x, y = pyautogui.position()
    print(f"Position selected: ({x}, {y})")
    return f"({x}, {y})"
