import tkinter as tk
from tkinter import ttk
from services.musictools_service import mt_service


class TuningForkView:
    def __init__(self, root):
        self._root = root
        self._frm_main = None
        self._frm_presets = None
        self._frm_preset_buttons = None
        self._frm_presets_settings = None
        self._var_freq_txt = None
        self._var_entry_txt = None
        self._var_play_txt = None
        self._ent_freq = None
        self._presets = []

        self._initialize()

    def pack(self):
        self._frm_main.pack()

    def _initialize(self):
        self._presets = mt_service.tfork_get_presets()
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

        lbl_tuningfork.grid(columnspan=3, sticky=(tk.constants.W, tk.constants.E))
        self._ent_freq.grid(row=1, column=0, sticky=(tk.constants.W, tk.constants.E), pady=3)
        btn_set.grid(row=1, column=1)
        btn_save.grid(row=1, column=2)
        btn_play.grid(columnspan=3, pady=3)
        self._init_frm_presets()
        self._frm_presets.grid(columnspan=3)

    def _init_frm_presets(self):
        lbl_presets = ttk.Label(
            master=self._frm_presets,
            text="Presets:"
        )

        btn_presets_manage = tk.Button(
            master=self._frm_presets,
            text="Manage",
            pady=5,
            command=self._handle_presets_manage_btn_click
        )
        self._frm_presets.columnconfigure(1, weight=1)
        lbl_presets.grid(row=0, column=0, sticky=tk.constants.W)
        btn_presets_manage.grid(row=0, column=1, sticky=tk.constants.W)
        self._init_preset_buttons()

    def _init_preset_buttons(self):
        print("Init preset buttons")
        self._frm_preset_buttons = ttk.Frame(master=self._frm_presets)

        pos = 0
        cols = 3

        for preset in self._presets:
            btn = tk.Button(
                master=self._frm_preset_buttons,
                text=f"{preset.label} ({preset.freq} Hz)",
                pady=5,
                command=lambda freq=preset.freq: self._handle_preset_btn_click(
                    freq)
            )
            btn.grid(column=pos % cols, row=pos//cols)
            pos += 1
        self._frm_preset_buttons.grid(columnspan=2)


    def _init_frm_presets_settings(self):
        self._frm_presets_settings = ttk.Frame(master=self._frm_presets)

        lbl_presets_settings = ttk.Label(
            master=self._frm_presets_settings,
            text="Manage presets:"
        )

        btn_presets_settings_close = tk.Button(
            master=self._frm_presets_settings,
            text="Close",
            pady=5,
            command=self._handle_presets_settings_close_btn_click
        )

        lbl_presets_settings.grid(row=0, column=0, sticky=tk.constants.W)
        btn_presets_settings_close.grid(row=0, column=1, sticky=tk.constants.W)
   
        row = 1
        for preset in self._presets:
            lbl = ttk.Label(
                master=self._frm_presets_settings,
                text=f"{preset.label} ({preset.freq} Hz)",

            )
            btn = tk.Button(
                master=self._frm_presets_settings,
                text="Delete",
                command=lambda id=preset.id: self._handle_preset_delete_btn_click(id)
            )
            lbl.grid(row=row, column=0)
            btn.grid(row=row, column=1)
            row += 1

    def _update_tuning_fork(self, freq: float):
        label_text = f"Tuning Fork\n({freq} Hz)"
        self._var_freq_txt.set(label_text)
        mt_service.tfork_set_freq(freq)

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
        mt_service.tfork_save_preset(self._ent_freq.get(), "?")
        self._presets = mt_service.tfork_get_presets()
        self._update_preset_views()
    
    def _handle_presets_manage_btn_click(self):
        print("Open preset settings")
        if not self._frm_presets_settings:
            self._init_frm_presets_settings()
        if not self._frm_presets_settings.winfo_ismapped():
            self._frm_presets_settings.grid()
        else:
            print("Window is already open")

    def _handle_presets_settings_close_btn_click(self):
        print("Close preset settings")
        self._frm_presets_settings.grid_forget()

    def _handle_preset_btn_click(self, freq: float):
        self._update_tuning_fork(freq)
        self._var_entry_txt.set(str(freq))
    
    def _handle_preset_delete_btn_click(self, preset_id: str):
        mt_service.tfork_delete_preset(preset_id)
        self._presets = mt_service.tfork_get_presets()
        self._update_preset_views()
    
    def _update_preset_views(self):
        print("Update all preset views")
        self._frm_preset_buttons.destroy()
        self._init_preset_buttons()
        if self._frm_presets_settings and self._frm_presets_settings.winfo_ismapped():
            # Preset-managing view is open
            self._frm_presets_settings.destroy()
            self._init_frm_presets_settings()
            self._frm_presets_settings.grid()

