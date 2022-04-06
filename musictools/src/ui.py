import tkinter as tk
from tkinter import ttk
from tuning_fork import TuningFork

class UI:
    def __init__(self, root):
        self._root = root
        self._tuning_fork = TuningFork()
        self._var_freq_txt = None
        self._var_entry_txt = None
        self._var_play_txt = None
        self._ent_freq = None

    def start(self):
        self._var_freq_txt = tk.StringVar()
        self._var_freq_txt.set("Tuning Fork\n(440 Hz)")
        self._var_entry_txt = tk.StringVar()
        self._var_entry_txt.set("(enter frequency)")
        self._var_play_txt = tk.StringVar()
        self._var_play_txt.set("Play")

        lbl_tuningfork = tk.Label(
            master=self._root,
            textvariable=self._var_freq_txt,
            fg="black",
            bg="yellow",
            height=20
        )

        btn_play = tk.Button(
            master=self._root,
            textvariable=self._var_play_txt,
            pady=5,
            command=self._handle_play_btn_click
        )

        self._ent_freq = ttk.Entry(
            master=self._root,
            textvariable=self._var_entry_txt
        )

        btn_set = tk.Button(
            master=self._root,
            text="Set",
            pady=5,
            command=self._handle_set_btn_click
        )

        lbl_presets = ttk.Label(
            master=self._root,
            text="Presets:"
        )

        btn_a = tk.Button(
            master=self._root,
            text="A (440 Hz)",
            pady=5,
            command=lambda: self._handle_preset_btn_click("A")
        )

        btn_d = tk.Button(
            master=self._root,
            text="D (293.66Hz)",
            pady=5,
            command=lambda: self._handle_preset_btn_click("D")
        )

        btn_g = tk.Button(
            master=self._root,
            text="G (196 Hz)",
            pady=5,
            command=lambda: self._handle_preset_btn_click("G")
        )

        lbl_tuningfork.grid(columnspan=3, sticky=(tk.constants.W, tk.constants.E))
        self._ent_freq.grid(row=1, column=0, columnspan=2,
                            sticky=(tk.constants.W, tk.constants.E), pady=3)
        btn_set.grid(row=1, column=2)
        lbl_presets.grid(sticky=tk.constants.W)
        btn_a.grid(row=3, column=0)
        btn_d.grid(row=3, column=1)
        btn_g.grid(row=3, column=2)
        btn_play.grid(columnspan=3, pady=3)

    def _handle_play_btn_click(self):
        if self._tuning_fork.is_active():
            self._tuning_fork.stop()
            self._var_play_txt.set("Play")
        else:
            self._tuning_fork.start()
            self._var_play_txt.set("Stop")

    def _handle_set_btn_click(self):
        try:
            freq = float(self._ent_freq.get())
            self._update_tuning_fork(freq)
        except ValueError:
            print("Frequency must be a number")

    def _handle_preset_btn_click(self, note: str):
        freq = 0
        if note == "A":
            freq = 440
        elif note == "D":
            freq = 293.66
        elif note == "G":
            freq = 196
        self._update_tuning_fork(float(freq))
        self._var_entry_txt.set(str(freq))

    def _update_tuning_fork(self, freq: float):
        label_text = f"Tuning Fork\n({freq} Hz)"
        self._var_freq_txt.set(label_text)
        self._tuning_fork.set_frequency(freq)
