import tkinter as tk
from tkinter import ttk
from services.musictools_service import mt_service


class MetronomeView:
    def __init__(self, root):
        self._root = root
        self._frm_main = None
        self._var_start_txt = None
        self._var_bpm_txt = None

        self._initialize()
    
    def pack(self):
        self._frm_main.pack()
    
    def _initialize(self):
        self._frm_main = tk.Frame(master=self._root, highlightbackground="black",
                                   highlightthickness = 1)
        self._init_frm_header()
        self._init_frm_start_button()
    
    def _init_frm_header(self):
        bpm = mt_service.metronome_get_bpm()
        self._var_bpm_txt = tk.StringVar()
        self._var_bpm_txt.set(f"Metronome\n({bpm} bpm)")
        frm_header = tk.Frame(master=self._frm_main)
        frm_header.configure(bg="green")

        lbl_metronome = tk.Label(
            master=frm_header,
            textvariable=self._var_bpm_txt,
            fg="black",
            bg="green",
            width=20,
            height=20
        )
        lbl_metronome.pack()
        frm_header.grid(pady=(0,3), sticky=(tk.W, tk.E))
    
    def _init_frm_start_button(self):
        frm_start_button = ttk.Frame(master=self._frm_main)

        self._var_start_txt = tk.StringVar()
        self._var_start_txt.set("Start")

        btn_start = tk.Button(
            master=frm_start_button,
            textvariable=self._var_start_txt,
            pady=5,
            command=self._handle_start_btn_click
        )

        btn_start.pack()
        frm_start_button.grid(pady=(0,5))

    def _handle_start_btn_click(self):
        if mt_service.metronome_is_active():
            mt_service.metronome_stop()
            self._var_start_txt.set("Start")
        else:
            mt_service.metronome_start()
            self._var_start_txt.set("Stop")
    
    


