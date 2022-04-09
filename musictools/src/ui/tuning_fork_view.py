import tkinter as tk
from tkinter import ttk
from services.musictools_service import mt_service


class TuningForkView:
    def __init__(self, root):
        self._root = root
        self._frm_main = None
        self._frm_presets = None
        self._var_freq_txt = None
        self._var_entry_txt = None
        self._var_play_txt = None
        self._ent_freq = None
        self._presets = []

        self._initialize()

    def pack(self):
        self._frm_main.pack()

    def _initialize(self):
        self._frm_main = ttk.Frame(master=self._root)
        self._frm_presets = ttk.Frame(master=self._frm_main)

        self._var_freq_txt = tk.StringVar()
        self._var_freq_txt.set("Tuning Fork\n(440 Hz)")
        self._var_entry_txt = tk.StringVar()
        self._var_entry_txt.set("(enter frequency)")
        self._var_play_txt = tk.StringVar()
        self._var_play_txt.set("Play")

        lbl_tuningfork = tk.Label(
            master=self._frm_main,
            textvariable=self._var_freq_txt,
            fg="black",
            bg="yellow",
            height=20
        )

        btn_play = tk.Button(
            master=self._frm_main,
            textvariable=self._var_play_txt,
            pady=5,
            command=self._handle_play_btn_click
        )

        self._ent_freq = ttk.Entry(
            master=self._frm_main,
            textvariable=self._var_entry_txt
        )

        btn_set = tk.Button(
            master=self._frm_main,
            text="Set",
            pady=5,
            command=self._handle_set_btn_click
        )

        btn_save = tk.Button(
            master=self._frm_main,
            text="Save",
            pady=5,
            command=self._handle_save_btn_click
        )

        lbl_presets = ttk.Label(
            master=self._frm_main,
            text="Presets:"
        )

        lbl_tuningfork.grid(columnspan=3, sticky=(
            tk.constants.W, tk.constants.E))
        self._ent_freq.grid(row=1, column=0, columnspan=2,
                            sticky=(tk.constants.W, tk.constants.E), pady=3)
        btn_set.grid(row=1, column=2)
        btn_save.grid(row=1, column=3)
        lbl_presets.grid(sticky=tk.constants.W)
        self._init_preset_buttons()
        self._frm_presets.grid(columnspan=3)
        btn_play.grid(columnspan=3, pady=3)

    def _init_preset_buttons(self):
        self._presets = mt_service.tfork_get_presets()
        pos = 0
        cols = 3

        for preset in self._presets:
            btn = tk.Button(
                master=self._frm_presets,
                text=f"{preset[1]} ({preset[0]} Hz)",
                pady=5,
                command=lambda freq=preset[0]: self._handle_preset_btn_click(
                    freq)
            )
            btn.grid(column=pos % cols, row=pos//cols)
            pos += 1

    def _handle_play_btn_click(self):
        if mt_service.tfork_is_active():
            mt_service.tfork_stop()
            self._var_play_txt.set("Play")
        else:
            mt_service.tfork_start()
            self._var_play_txt.set("Stop")

    def _handle_set_btn_click(self):
        try:
            freq = float(self._ent_freq.get())
            self._update_tuning_fork(freq)
        except ValueError:
            print("Frequency must be a number")

    def _handle_save_btn_click(self):
        preset = (self._ent_freq.get(), "?")
        mt_service.tfork_save_preset(preset)
        self._init_preset_buttons()

    def _handle_preset_btn_click(self, freq: float):
        self._update_tuning_fork(freq)
        self._var_entry_txt.set(str(freq))

    def _update_tuning_fork(self, freq: float):
        label_text = f"Tuning Fork\n({freq} Hz)"
        self._var_freq_txt.set(label_text)
        mt_service.tfork_set_freq(freq)
