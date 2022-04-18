import tkinter as tk
from tkinter import LEFT, NS, VERTICAL, ttk
from services.musictools_service import mt_service
from config import TF_ICON_PATH


class TuningForkView:
    def __init__(self, root):
        self._root = root
        self._frm_main = None
        self._frm_presets = None
        self._frm_preset_buttons = None
        self._frm_settings = None
        self._img_tf = None
        self._lbl_error = None
        self._var_freq_txt = None
        self._var_entry_txt = None
        self._var_play_txt = None
        self._var_error_txt = None
        self._ent_freq = None
        self._presets = []

        self._initialize()

    def pack(self):
        self._frm_main.pack(side=tk.LEFT, fill="y")
   
    def _initialize(self):
        self._presets = mt_service.tfork_get_presets()
        self._frm_main = ttk.Frame(master=self._root, borderwidth=1, relief=tk.RIDGE)

        self._init_frm_header()
        self._init_lbl_error()
        self._init_frm_freq_entry()
        self._init_frm_play_button()
        self._init_frm_presets()
        self._init_frm_presets_settings()

        self._hide_error()

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
        if self._lbl_error.winfo_ismapped:
            self._lbl_error.grid_remove()

    def _init_frm_header(self):
        frm_header = tk.Frame(master=self._frm_main)
        frm_header.configure(bg="yellow")

        cnv_tf = tk.Canvas(master=frm_header, width=96, height=96, bg="yellow", 
                              highlightthickness=0)        
        self._img_tf = tk.PhotoImage(file=TF_ICON_PATH)
        cnv_tf.create_image(48, 48, image=self._img_tf)
   
        self._var_freq_txt = tk.StringVar()
        self._var_freq_txt.set("Tuning Fork\n(440 Hz)")

        lbl_tuningfork = tk.Label(
            master=frm_header,
            textvariable=self._var_freq_txt,
            fg="black",
            bg="yellow",
            height=6
        )
        cnv_tf.pack(pady=(30,0))
        lbl_tuningfork.pack()        
        frm_header.grid(pady=(0,3), sticky=(tk.W, tk.E))

    def _init_frm_freq_entry(self):
        frm_freq_entry = ttk.Frame(master=self._frm_main)
        frm_freq_entry.configure(padding=5)

        self._var_entry_txt = tk.StringVar()
        self._var_entry_txt.set("(enter frequency)")

        self._ent_freq = ttk.Entry(
            master=frm_freq_entry,
            textvariable=self._var_entry_txt
        )

        btn_set = tk.Button(
            master=frm_freq_entry,
            text="Set",
            pady=5,
            command=self._handle_set_btn_click
        )

        btn_save = tk.Button(
            master=frm_freq_entry,
            text="Save",
            pady=5,
            command=self._handle_save_btn_click
        )

        self._ent_freq.grid(row=0, column=0, ipady=5)       
        btn_set.grid(row=0, column=1, padx=5)
        btn_save.grid(row=0, column=2)
        
        frm_freq_entry.grid(pady=(0,3))

    def _init_frm_play_button(self):
        frm_play_button = ttk.Frame(master=self._frm_main)

        self._var_play_txt = tk.StringVar()
        self._var_play_txt.set("Play")

        btn_play = tk.Button(
            master=frm_play_button,
            textvariable=self._var_play_txt,
            pady=5,
            command=self._handle_play_btn_click
        )

        btn_play.pack()
        frm_play_button.grid(pady=(0,5))

    def _init_frm_presets(self):
        self._frm_presets = ttk.Frame(master=self._frm_main)
        self._frm_presets.configure(padding=5)    

        frm_presets_header = ttk.Frame(master=self._frm_presets)

        lbl_presets = ttk.Label(
            master=frm_presets_header,
            text="Presets:"
        )

        btn_settings_open = tk.Button(
            master=frm_presets_header,
            text="Manage",
            pady=5,
            command=self._handle_settings_open_btn_click
        )

        lbl_presets.pack(side=LEFT)
        btn_settings_open.pack(side=LEFT, padx=5)
        frm_presets_header.grid(pady=(0,3), sticky=tk.W)

        self._init_preset_buttons()
        self._frm_presets.grid(sticky=(tk.W, tk.E))

    def _init_preset_buttons(self):
        self._frm_preset_buttons = ttk.Frame(master=self._frm_presets)

        if len(self._presets) > 0:
            pos = 0
            cols = 3

            for preset in self._presets:
                btn = tk.Button(
                    master=self._frm_preset_buttons,
                    text=f"{preset.freq} Hz",
                    pady=5,
                    command=lambda freq=preset.freq: self._handle_preset_btn_click(
                        freq)
                )
                btn.grid(column=pos % cols, row=pos//cols, padx=(3,0))
                pos += 1
        else:
            lbl_no_presets = tk.Label(
                master=self._frm_preset_buttons,
                text="(No presets)"
            )
            lbl_no_presets.grid(sticky=tk.W)

        self._frm_preset_buttons.grid(sticky=(tk.W, tk.E))

    def _init_frm_presets_settings(self):
        self._frm_settings = ttk.Frame(master=self._frm_main)
        self._frm_settings.configure(padding=5)
        frm_settings_header = ttk.Frame(master=self._frm_settings)

        lbl_presets_settings = ttk.Label(
            master=frm_settings_header,
            text="Manage presets:"
        )

        btn_settings_close = tk.Button(
            master=frm_settings_header,
            text="Close",
            pady=5,
            command=self._handle_settings_close_btn_click
        )

        lbl_presets_settings.pack(side=LEFT)
        btn_settings_close.pack(side=LEFT, padx=5)
        frm_settings_header.grid(pady=(0,3), sticky=tk.W)

        frm_settings_buttons = ttk.Frame(master=self._frm_settings)   
        if len(self._presets) > 0:
            row = 1
            for preset in self._presets:
                lbl = ttk.Label(
                    master=frm_settings_buttons,
                    text=f"({preset.freq} Hz)",

                )
                btn = tk.Button(
                    master=frm_settings_buttons,
                    text="Delete",
                    command=lambda id=preset.id: self._handle_preset_delete_btn_click(id)
                )
                lbl.grid(row=row, column=0)
                btn.grid(row=row, column=1, padx=(3,0))
                row += 1
        else:
            lbl_no_presets = tk.Label(
                master=frm_settings_buttons,
                text="(No presets)"
            )
            lbl_no_presets.grid(sticky=tk.W)

        frm_settings_buttons.grid(pady=(0,6), sticky=tk.W)

    def _update_tf_header(self, freq: float):
        label_text = f"Tuning Fork\n({freq} Hz)"
        self._var_freq_txt.set(label_text)
   
    def _handle_play_btn_click(self):
        if mt_service.tfork_is_active():
            mt_service.tfork_stop()
            self._var_play_txt.set("Play")
        else:
            mt_service.tfork_start()
            self._var_play_txt.set("Stop")

    def _handle_set_btn_click(self):
        freq = mt_service.tfork_set_freq(self._ent_freq.get())
        if freq:  
            self._update_tf_header(freq)
            self._hide_error()
        else: 
            self._show_validation_error()
      
    def _handle_save_btn_click(self):
        preset = mt_service.tfork_save_preset(self._ent_freq.get(), "?")
        if preset:
            self._presets = mt_service.tfork_get_presets()
            self._update_preset_views()
            self._hide_error()
        else: 
            self._show_validation_error()

    def _show_validation_error(self):
        self._show_error("Enter a frequency between 20 and 8000 Hz")
    
    def _handle_settings_open_btn_click(self):
        if not self._frm_settings.winfo_ismapped():
            self._show_settings()

    def _handle_settings_close_btn_click(self):
        self._frm_settings.grid_remove()

    def _handle_preset_btn_click(self, freq: float):
        freq = mt_service.tfork_set_freq(freq)
        if freq:
            self._update_tf_header(freq)
            self._var_entry_txt.set(str(freq))
            self._hide_error()
    
    def _handle_preset_delete_btn_click(self, preset_id: str):
        mt_service.tfork_delete_preset(preset_id)
        self._presets = mt_service.tfork_get_presets()
        self._update_preset_views()
    
    def _update_preset_views(self):
        self._frm_preset_buttons.destroy()
        self._init_preset_buttons()
        settings_view_open = self._frm_settings.winfo_ismapped()
        self._frm_settings.destroy()
        self._init_frm_presets_settings()
        if settings_view_open:
            self._show_settings()
    
    def _show_settings(self):
        self._frm_settings.grid(sticky=(tk.W, tk.E))
