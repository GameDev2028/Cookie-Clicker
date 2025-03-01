import tkinter as tk
from tkinter import messagebox

class CookieClicker:
    def __init__(self, root):
        self.root = root
        self.root.title("Cookie Clicker")
        
        self.cookies = 0
        self.cps = 0  # Cookies per second
        self.upgrade_cost = 10

        self.cookie_label = tk.Label(root, text="Cookies: 0", font=("Helvetica", 16))
        self.cookie_label.pack(pady=10)

        self.click_button = tk.Button(root, text="Click Me!", font=("Helvetica", 16), command=self.click)
        self.click_button.pack(pady=10)

        self.upgrade_button = tk.Button(root, text="Buy Upgrade (10 Cookies)", font=("Helvetica", 16), command=self.buy_upgrade)
        self.upgrade_button.pack(pady=10)

        self.update_cookies()

    def click(self):
        self.cookies += 1
        self.update_labels()

    def buy_upgrade(self):
        if self.cookies >= self.upgrade_cost:
            self.cookies -= self.upgrade_cost
            self.cps += 1
            self.upgrade_cost = int(self.upgrade_cost * 1.5)
            self.update_labels()
        else:
            messagebox.showwarning("Not enough cookies", "You don't have enough cookies to buy this upgrade!")

    def update_cookies(self):
        self.cookies += self.cps
        self.update_labels()
        self.root.after(1000, self.update_cookies)

    def update_labels(self):
        self.cookie_label.config(text=f"Cookies: {self.cookies}")
        self.upgrade_button.config(text=f"Buy Upgrade ({self.upgrade_cost} Cookies)")

if __name__ == "__main__":
    root = tk.Tk()
    game = CookieClicker(root)
    root.mainloop()