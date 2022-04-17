import tkinter as tk
from tkinter import RIDGE, ttk
from services.musictools_service import mt_service
from config import METR_ICON_PATH

import os

class MetronomeView:
    def __init__(self, root):
        self._root = root
        self._frm_main = None
        self._img_metr = None
        self._var_start_txt = None
        self._var_bpm_txt = None
        self._var_bpm_entry_txt = None
        self._ent_bpm = None

        self._initialize()
    
    def pack(self):
        self._frm_main.pack(side=tk.LEFT, fill="y")
    
    def _initialize(self):
        self._frm_main = ttk.Frame(master=self._root, borderwidth=1, relief=tk.RIDGE)
        self._init_frm_header()
        self._init_frm_bpm_entry()
        self._init_frm_start_button()
    
    def _init_frm_header(self):
        frm_header = tk.Frame(master=self._frm_main)
        frm_header.configure(bg="green3")

        cnv_metr = tk.Canvas(master=frm_header, width=96, height=96, bg="green3", 
                              highlightthickness=0)      
        self._img_metr = tk.PhotoImage(file=METR_ICON_PATH)
        cnv_metr.create_image(48, 48, image=self._img_metr)

        bpm = mt_service.metronome_get_bpm()
        self._var_bpm_txt = tk.StringVar()
        self._var_bpm_txt.set(f"Metronome\n({bpm} bpm)")

        lbl_metronome = tk.Label(
            master=frm_header,
            textvariable=self._var_bpm_txt,
            fg="black",
            bg="green3",
            height=6
        )

        cnv_metr.pack(pady=(30,0))
        lbl_metronome.pack()
        frm_header.grid(pady=(0,3), sticky=(tk.W, tk.E))
    
    def _init_frm_bpm_entry(self):
        frm_bpm_entry = ttk.Frame(master=self._frm_main)
        frm_bpm_entry.configure(padding=5)

        self._var_bpm_entry_txt = tk.StringVar()
        self._var_bpm_entry_txt.set("(enter bpm)")

        self._ent_bpm = ttk.Entry(
            master=frm_bpm_entry,
            textvariable=self._var_bpm_entry_txt
        )

        btn_set = tk.Button(
            master=frm_bpm_entry,
            text="Set",
            pady=5,
            command=self._handle_set_btn_click
        )

        self._ent_bpm.grid(row=0, column=0, ipady=5)       
        btn_set.grid(row=0, column=1, padx=5)
        frm_bpm_entry.grid(pady=(0,3))

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
    
    def _handle_set_btn_click(self):
        bpm = int(self._ent_bpm.get())
        self._update_metronome(bpm)
    
    def _update_metronome(self, bpm: int):
        label_text = f"Metronome\n({bpm} bpm)"
        self._var_bpm_txt.set(label_text)
        mt_service.metronome_set_bpm(bpm)
    
    


