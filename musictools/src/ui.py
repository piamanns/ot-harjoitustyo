import tkinter as tk
from tuning_fork import TuningFork

class UI:
    def __init__(self, root):
        self._root = root
        self._tuning_fork = TuningFork()
        self._label_txt = None
    
    def start(self):  
        self._label_txt = tk.StringVar()
        self._label_txt.set("Play")

        lbl_tuningfork = tk.Label(
            master=self._root,
            text="Tuning Fork\n(A, 440 Hz)",
            fg="black",
            bg="yellow",
            width=20,
            height=10
        )

        btn_play = tk.Button(
            master=self._root,
            textvariable=self._label_txt,
            pady=5,
            command=self._handle_button_click
        )
      
        lbl_tuningfork.grid(row=0, column=0)
        btn_play.grid(row=1, column=0, pady=3)

    def _handle_button_click(self):
        if self._tuning_fork.is_active():
            self._tuning_fork.stop()
            self._label_txt.set("Play")
        else:
            self._tuning_fork.start()
            self._label_txt.set("Stop")
