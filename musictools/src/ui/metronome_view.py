import tkinter as tk
from tkinter import ttk
from ui.tool_view_base import ToolView
from ui.presets_view import PresetsView
from services.musictools_service import mt_service
from config import METR_BPM_MIN, METR_BPM_MAX, METR_BEATS_MAX, METR_BEATS_MIN, METR_ICON_PATH


class MetronomeView(ToolView):
    def __init__(self, root):
        super().__init__(root)
        self._var_start_txt = None
        self._var_bpm_txt = None
        self._var_beats_txt = None
        self._var_bpm_entry_txt = None
        self._ent_bpm = None
        self._var_beats_option_int = 0

        self._initialize()

    def _initialize(self):
        super()._initialize()
        self._init_frm_header()
        self._init_lbl_error()
        self._init_frm_bpm_entry()
        self._init_frm_beats_option()
        self._init_frm_start_button()
        self._init_frm_presets()

        self._hide_error()

    def _init_frm_header(self):
        frm_header = tk.Frame(master=self._frm_main)
        frm_header.configure(bg="green3")

        cnv_metr = tk.Canvas(master=frm_header, width=192, height=96, bg="green3",
                             highlightthickness=0)
        self._img_tool = tk.PhotoImage(file=METR_ICON_PATH)
        cnv_metr.create_image(96, 48, image=self._img_tool)

        bpm = mt_service.metr_get_bpm()
        self._var_bpm_txt = tk.StringVar()
        self._var_bpm_txt.set(f"Metronome\n({bpm} bpm)")

        beats_per_bar = mt_service.metr_get_beats_per_bar()
        self._var_beats_txt = tk.StringVar()
        self._var_beats_txt.set(f"Beats per bar: {beats_per_bar}")

        lbl_metr_bpm = tk.Label(
            master=frm_header,
            textvariable=self._var_bpm_txt,
            fg="black",
            bg="green3"
        )

        lbl_metr_beats = tk.Label(
            master=frm_header,
            textvariable=self._var_beats_txt,
            fg="black",
            bg="green3"
        )
        cnv_metr.pack(pady=(30,0))
        lbl_metr_bpm.pack(pady=(22,0))
        lbl_metr_beats.pack(pady=(0,20))
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

        btn_save = tk.Button(
            master=frm_bpm_entry,
            text="Save as new",
            pady=5,
            command=self._handle_save_btn_click
        )

        self._btn_update = tk.Button(
            master=frm_bpm_entry,
            text="Update",
            pady=5,
            command=self._handle_update_btn_click
        )

        self._disable_update_btn()

        self._ent_bpm.grid(row=0, column=0, ipady=5)
        btn_set.grid(row=0, column=1, padx=5)
        btn_save.grid(row=0, column=2, padx=(0,5))
        self._btn_update.grid(row=0, column=3)
        frm_bpm_entry.grid(pady=(0,3))

    def _init_frm_beats_option(self):
        frm_beats_option = ttk.Frame(master=self._frm_main)
        lbl_beats_option = ttk.Label(
          master=frm_beats_option,
          text="Beats per bar:"
        )

        beats = list(range(int(METR_BEATS_MIN), int(METR_BEATS_MAX)+1))
        self._var_beats_option_int = tk.IntVar()
        start_index = mt_service.metr_get_beats_per_bar()
        self._var_beats_option_int.set(beats[start_index-1])

        dropdown = tk.OptionMenu(
            frm_beats_option,
            self._var_beats_option_int,
            *beats,
            command=self._handle_beats_option_select
        )

        lbl_beats_option.grid()
        dropdown.grid(row=0, column=1)

        frm_beats_option.grid()

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
        frm_start_button.grid(pady=(5,5))

    def _init_frm_presets(self):
        presets = mt_service.metr_get_presets()
        self._frm_presets = ttk.Frame(master=self._frm_main)
        self._presets_view = PresetsView(
            self._frm_presets,
            presets,
            self._handle_preset_btn_click,
            self._handle_preset_delete_btn_click
        )
        self._presets_view.pack()
        self._frm_presets.grid(sticky=(tk.W, tk.E))

    def _update_frm_presets(self):
        self._presets_view.update_view(
            mt_service.metr_get_presets(),
            mt_service.metr_get_active_preset()
        )

    def _handle_start_btn_click(self):
        if mt_service.metr_is_active():
            mt_service.metr_stop()
            self._var_start_txt.set("Start")
        else:
            mt_service.metr_start()
            self._var_start_txt.set("Stop")

    def _handle_set_btn_click(self):
        bpm = mt_service.metr_set_bpm(self._ent_bpm.get())
        if bpm:
            self._update_frm_header_bpm(bpm)
            self._hide_error()
        else:
            self._show_validation_error()

    def _handle_save_btn_click(self):
        preset = mt_service.metr_save_preset(
            self._ent_bpm.get(),
            self._var_beats_option_int.get(),
            4
        )
        if preset:
            mt_service.metr_set_active_preset(None)
            self._update_frm_presets()
            self._disable_update_btn()
            self._hide_error()
        else:
            self._show_validation_error()
    
    def _handle_update_btn_click(self):
        active_id = mt_service.metr_get_active_preset()
        updated_preset = mt_service.metr_update_preset(  
            self._ent_bpm.get(),
            self._var_beats_option_int.get(),
            4,
            active_id
        )
        if updated_preset:
            self._update_frm_presets()
            self._hide_error()
        else:
            self._show_validation_error()

    def _show_validation_error(self):
        self._show_error(f"Enter a bpm value between {METR_BPM_MIN} and {METR_BPM_MAX}")

    def _handle_beats_option_select(self, beats):
        mt_service.metr_set_beats_per_bar(beats)
        self._update_frm_header_beats(beats)

    def _update_frm_header_bpm(self, bpm: int):
        label_text = f"Metronome\n({bpm} bpm)"
        self._var_bpm_txt.set(label_text)

    def _update_frm_header_beats(self, beats: int):
        self._var_beats_txt.set(f"Beats per bar: {beats}")

    def _update_frm_beats_option(self, beats_per_bar: int):
        self._var_beats_option_int.set(beats_per_bar)

    def _handle_preset_btn_click(self, beat_values: tuple, label: str, preset_id: int):
        bpm, beats_per_bar = beat_values
        bpm = mt_service.metr_set_bpm(bpm)
        if bpm:
            mt_service.metr_set_active_preset(preset_id)
            self._presets_view.update_selected(preset_id)
            self._update_frm_header_bpm(bpm)
            self._var_bpm_entry_txt.set(str(bpm))

            mt_service.metr_set_beats_per_bar(beats_per_bar)
            self._update_frm_header_beats(beats_per_bar)
            self._update_frm_beats_option(beats_per_bar)

            self._enable_update_btn()
            self._hide_error()

    def _handle_preset_delete_btn_click(self, preset_id: int):
        mt_service.metr_delete_preset(preset_id)
        self._update_frm_presets()
        if mt_service.metr_get_active_preset() == preset_id:
            mt_service.metr_set_active_preset(None)
            self._disable_update_btn()

