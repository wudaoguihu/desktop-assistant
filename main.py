import tkinter as tk
from gui.app import App

if __name__ == "__main__":
    # 启动图形界面
    root = tk.Tk()
    app = App(root)
    root.mainloop()