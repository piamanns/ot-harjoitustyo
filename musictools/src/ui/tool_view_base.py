import tkinter as tk
from tkinter import ttk


class ToolView:
    """A base class for the musical tool views.
    """

    def __init__(self, root):
        """The class constructor.

        Args:
            root: The Tkinter widget object containing this view.
        """

        self._root = root
        self._img_tool = None
        self._frm_main = None
        self._frm_presets = None
        self._presets_view = None
        self._lbl_error = None
        self._var_error_txt = None
        self._btn_update = None

    def _initialize(self):
        self._frm_main = ttk.Frame(master=self._root, borderwidth=1, relief=tk.RIDGE)
        self._btn_update = tk.Button(
            master=self._frm_main
        )

    def pack(self):
        """Adds the view to the tkinter layout.
        """

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

    def _enable_update_btn(self):
        self._btn_update["state"] = tk.NORMAL

    def _disable_update_btn(self):
        self._btn_update["state"] = tk.DISABLED

    def _clear_entry(self, event, entry):
        entry.delete(0, tk.END)
        entry.unbind('<FocusIn>')
