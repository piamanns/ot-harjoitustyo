import tkinter as tk
from tkinter import ttk
from ui.tool_view_base import ToolView
from ui.presets_view import PresetsView
from services.musictools_service import mt_service
from config import TF_ICON_PATH, TF_FREQ_MAX, TF_FREQ_MIN


class TuningForkView(ToolView):
    def __init__(self, root):
        super().__init__(root)
        self._var_freq_txt = None
        self._var_entry_txt = None
        self._var_play_txt = None
        self._ent_freq = None
   
        self._initialize()

    def _initialize(self):
        super()._initialize()
        self._init_frm_header()
        self._init_lbl_error()
        self._init_frm_freq_entry()
        self._init_frm_play_button()
        self._init_frm_presets()
        self._hide_error()

    def _init_frm_header(self):
        frm_header = tk.Frame(master=self._frm_main)
        frm_header.configure(bg="yellow")

        cnv_tf = tk.Canvas(master=frm_header, width=192, height=96, bg="yellow",
                           highlightthickness=0)
        self._img_tool = tk.PhotoImage(file=TF_ICON_PATH)
        cnv_tf.create_image(96, 48, image=self._img_tool)

        freq = mt_service.tfork_get_freq()
        note_name = mt_service.tfork_get_note_name(freq)
        self._var_freq_txt = tk.StringVar()
        self._update_tf_header(freq, note_name)

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
            text="Save as new",
            pady=5,
            command=self._handle_save_btn_click
        )

        self._btn_update = tk.Button(
            master=frm_freq_entry,
            text="Update",
            pady=5,
            command=self._handle_update_btn_click
        )

        self._disable_update_btn()

        self._ent_freq.grid(row=0, column=0, ipady=5)
        btn_set.grid(row=0, column=1, padx=5)
        btn_save.grid(row=0, column=2, padx=(0,5))
        self._btn_update.grid(row=0, column=3)
        frm_freq_entry.grid()

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
        presets = mt_service.tfork_get_presets()
        self._frm_presets = ttk.Frame(master=self._frm_main)
        self._presets_view = PresetsView(
            self._frm_presets,
            presets,
            self._handle_preset_btn_click,
            self._handle_preset_delete_btn_click
        )
        self._presets_view.pack()
        self._frm_presets.grid(sticky=(tk.EW))

    def _update_tf_header(self, freq: float, label: str):
        label_text = f"Tuning Fork\n{freq} Hz ({label})"
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
            label = mt_service.tfork_get_note_name(freq)
            self._update_tf_header(freq, label)
            self._hide_error()
        else:
            self._show_validation_error()

    def _handle_save_btn_click(self):
        preset = mt_service.tfork_save_preset(self._ent_freq.get())
        if preset:
            mt_service.tfork_set_active_preset(None)
            self._update_frm_presets()
            self._disable_update_btn()
            self._hide_error()
        else:
            self._show_validation_error()
    
    def _handle_update_btn_click(self):
        active_preset_id = mt_service.tfork_get_active_preset()
        updated_preset = mt_service.tfork_update_preset(  
            self._ent_freq.get(),
            active_preset_id
        )
        if updated_preset:
            self._update_frm_presets()
            self._hide_error()
        else:
            self._show_validation_error()

    def _update_frm_presets(self):
        self._presets_view.update_view(
            mt_service.tfork_get_presets(),
            mt_service.tfork_get_active_preset()
        )

    def _show_validation_error(self):
        self._show_error(f"Enter a frequency between {TF_FREQ_MIN} and {TF_FREQ_MAX} Hz")

    def _handle_preset_btn_click(self, freq: float, label: str, preset_id: int):
        freq = mt_service.tfork_set_freq(freq)
        if freq:
            mt_service.tfork_set_active_preset(preset_id)
            self._presets_view.update_selected(preset_id)
            self._update_tf_header(freq, label)
            self._var_entry_txt.set(str(freq))
            self._enable_update_btn()
            self._hide_error()

    def _handle_preset_delete_btn_click(self, preset_id: str):
        mt_service.tfork_delete_preset(preset_id)
        self._update_frm_presets()
        if mt_service.tfork_get_active_preset() == preset_id:
            mt_service.tfork_set_active_preset(None)
            self._disable_update_btn()
    