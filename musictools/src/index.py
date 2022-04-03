import tkinter as tk
from ui import UI

def main():
    window = tk.Tk()
    window.title("Musictools")

    ui = UI(window)
    ui.start()

    window.mainloop()

if __name__ == "__main__":
    main()