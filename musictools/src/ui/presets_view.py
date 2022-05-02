import tkinter as tk
from tkinter import ttk


class PresetsView:
    def __init__(self, root, presets, handle_preset_btn_click, handle_preset_delete_btn_click):
        self._root = root
        self._frm_main = None
        self._frm_preset_buttons = None
        self._frm_settings = None
        self._presets = presets
        self._handle_preset_btn_click = handle_preset_btn_click
        self._handle_preset_delete_btn_click = handle_preset_delete_btn_click
        self._initialize()

    def pack(self):
        self._frm_main.grid(sticky=(tk.W, tk.E))

    def _initialize(self):
        self._frm_main = ttk.Frame(master=self._root)
        self._frm_main.configure(padding=5)
        frm_presets_header = ttk.Frame(master=self._frm_main)

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

        lbl_presets.pack(side=tk.LEFT)
        btn_settings_open.pack(side=tk.LEFT, padx=5)
        frm_presets_header.grid(pady=(0,3), sticky=tk.W)

        self._init_preset_buttons()
        self._init_frm_presets_settings()

    def _init_preset_buttons(self):
        self._frm_preset_buttons = ttk.Frame(master=self._frm_main)

        if len(self._presets) > 0:
            pos = 0
            cols = 3

            for preset in self._presets:
                btn = tk.Button(
                    master=self._frm_preset_buttons,
                    text=str(preset),
                    pady=5,
                    command=lambda value=preset.get_value(), label=preset.get_label():
                        self._handle_preset_btn_click(
                            value, label
                        )
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

        lbl_presets_settings.pack(side=tk.LEFT)
        btn_settings_close.pack(side=tk.LEFT, padx=5)
        frm_settings_header.grid(pady=(3,3), sticky=tk.W)

        frm_settings_buttons = ttk.Frame(master=self._frm_settings)   
        if len(self._presets) > 0:
            row = 1
            for preset in self._presets:
                lbl = ttk.Label(
                    master=frm_settings_buttons,
                    text=str(preset),

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

    def _handle_settings_open_btn_click(self):
        if not self._frm_settings.winfo_ismapped():
            self._show_settings()
    
    def _show_settings(self):
        self._frm_settings.grid(sticky=(tk.W, tk.E))
    
    def _handle_settings_close_btn_click(self):
        self._frm_settings.grid_remove()    

    def update_view(self, presets):
        self._presets = presets
        self._frm_preset_buttons.destroy()
        self._init_preset_buttons()
        settings_view_open = self._frm_settings.winfo_ismapped()
        self._frm_settings.destroy()
        self._init_frm_presets_settings()
        if settings_view_open:
            self._show_settings()
