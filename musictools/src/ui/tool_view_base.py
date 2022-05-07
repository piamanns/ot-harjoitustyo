import tkinter as tk
from tkinter import ttk


class ToolView:
    def __init__(self, root):
        self._root = root
        self._frm_main = None
        self._lbl_error = None
        self._var_error_txt = None

    def _initialize(self):
        self._frm_main = ttk.Frame(master=self._root, borderwidth=1, relief=tk.RIDGE)

    def pack(self):
        self._frm_main.pack(side=tk.LEFT, fill="y")

    def _init_lbl_error(self):
        self._var_error_txt = tk.StringVar()
        self._lbl_error = ttk.Label(
            master=self._frm_main,
            textvariable=self._var_error_txt,
            foreground="red"
        )
        self._lbl_error.grid()

    def _show_error(self, message):
        self._var_error_txt.set(message)
        self._lbl_error.grid()

    def _hide_error(self):
        self._lbl_error.grid_remove()
   