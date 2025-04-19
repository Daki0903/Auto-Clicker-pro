import tkinter as tk
from tkinter import messagebox
from clicker import Clicker
from listener import Listener
import threading

class AutoClickerGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Auto Clicker Pro")
        self.root.geometry("350x300")
        self.root.configure(bg="#222222")

        self.clicker = Clicker()

        # Brzina
        self.delay_var = tk.StringVar(value="0.01")
        self.ultra_fast = tk.BooleanVar()

        # Naslov
        tk.Label(root, text="Auto Clicker Pro", font=("Arial", 18, "bold"), bg="#222222", fg="white").pack(pady=10)

        # Delay
        tk.Label(root, text="Interval between clicks (seconds):", bg="#222222", fg="white").pack()
        tk.Entry(root, textvariable=self.delay_var, width=10).pack(pady=5)

        # Ultra fast
        tk.Checkbutton(root, text="Ultra Fast Mode (0 delay)", variable=self.ultra_fast, bg="#222222", fg="white", activebackground="#222222", selectcolor="#222222").pack()

        # Dugmad
        tk.Button(root, text="Start clicking", command=self.start_clicking, bg="#00cc66", fg="white", width=20).pack(pady=10)
        tk.Button(root, text="Stop", command=self.stop_clicking, bg="#cc3300", fg="white", width=20).pack()

        # Uputstvo
        tk.Button(root, text="Instructions", command=self.show_help, bg="#3366cc", fg="white", width=20).pack(pady=10)

    def start_clicking(self):
        try:
            delay = 0.0 if self.ultra_fast.get() else float(self.delay_var.get())
            self.clicker.delay = delay
            self.clicker.start()
            threading.Thread(target=self.listen_esc, daemon=True).start()
        except ValueError:
            messagebox.showerror("Error", "Enter a valid speed number!")

    def stop_clicking(self):
        self.clicker.stop()

    def listen_esc(self):
        listener = Listener(self.stop_clicking)
        listener.listen()

    def show_help(self):
        msg = (
            "➡️ Start clicking with the 'Start clicking' button\n"
            "➡️ Set interval between clicks in seconds\n"
            "➡️ Turn on 'Ultra Fast Mode' for extremely fast clicking\n"
            "➡️ Press ESC anytime to stop\n"
            "➡️ It doesn't click in the background - you must have an active window\n"
        )
        messagebox.showinfo("Uputstvo", msg)
