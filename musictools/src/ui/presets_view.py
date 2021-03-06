import tkinter as tk
from tkinter import ttk


class PresetsView:
    """Class describing the presets view.

    The view contains two scrollable areas:
    - the area with the clickable preset buttons
    - the area which lists the presets with corresponding Delete-buttons
    allowing for deleting saved presets.
    """

    def __init__(self, root, presets,
                 handle_preset_btn_click, handle_preset_delete_btn_click,
                 selection_color):
        """The class constructor.

        Args:
            root: The Tkinter widget object containing this view.
            presets: The saved presets for the current tool as a list of preset objects
                     corresponding to the current tool type.
            handle_preset_btn_click: A function for handling a click on a preset
                                    button.
            handle_preset_delete_btn_click: A function for handling a click on a
                                            delete button corresponding to a saved preset.
            selection_color: A string representing the color used for highlighting
                             the selected preset button.
        """

        self._root = root
        self._frm_main = None
        self._frm_settings = None
        self._scroll_preset_buttons = None
        self._scroll_settings_buttons = None
        self._presets = presets
        self._active_id = None
        self._handle_preset_btn_click = handle_preset_btn_click
        self._handle_preset_delete_btn_click = handle_preset_delete_btn_click
        self._selection_color = selection_color
        self._original_btn_color = ""

        self._initialize()

    def pack(self):
        """Adds the view to the tkinter layout.
        """

        self._frm_main.pack(expand=True, fill="both")

    def _initialize(self):
        self._frm_main = ttk.Frame(master=self._root)
        self._frm_main.columnconfigure(0, weight=1)
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

        self._original_btn_color = btn_settings_open["highlightbackground"]

        lbl_presets.pack(side=tk.LEFT)
        btn_settings_open.pack(side=tk.LEFT, padx=5)
        frm_presets_header.grid(pady=(0,3), sticky=tk.W)

        self._init_frm_preset_buttons()
        self._init_frm_presets_settings()

    def _init_frm_preset_buttons(self):
        frm_preset_buttons = ttk.Frame(master=self._frm_main, borderwidth=1, relief=tk.RIDGE)
        frm_preset_buttons.columnconfigure(0, weight=1)

        self._scroll_preset_buttons = ScrollableArea(frm_preset_buttons)
        self._scroll_preset_buttons.populate_content(self._populate_preset_buttons)

        frm_preset_buttons.grid(sticky=tk.EW, pady=(0,6))

    def _populate_preset_buttons(self, root):
        pos = 0
        cols = 3

        if len(self._presets) > 0:
            for preset in self._presets:
                btn = tk.Button(
                    master=root,
                    text=str(preset),
                    pady=5
                )
                btn.configure(command=lambda value=preset.get_value(),
                    label=preset.get_label(),
                    preset_id=preset.id,
                    button=btn: self._handle_preset_btn_click(
                                value, label, preset_id, button
                            )
                )
                if self._active_id == preset.id:
                    btn["highlightbackground"] = self._selection_color
                else:
                    btn["highlightbackground"] = self._original_btn_color
                btn.grid(column=pos % cols, row=pos//cols, padx=(3,0))
                pos += 1
        else:
            lbl_no_presets = tk.Label(
                master=root,
                text="(No presets)"
            )
            lbl_no_presets.grid(sticky=tk.W)

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

        frm_settings_buttons = ttk.Frame(master=self._frm_settings, borderwidth=1,
                                               relief=tk.RIDGE)
        self._scroll_settings_buttons = ScrollableArea(frm_settings_buttons)
        self._scroll_settings_buttons.populate_content(self._populate_settings_buttons)

        frm_settings_buttons.grid(pady=(0,6), sticky=tk.EW)

    def _populate_settings_buttons(self, root):
        if len(self._presets) > 0:
            row = 1
            for preset in self._presets:
                lbl = ttk.Label(
                    master=root,
                    text=str(preset),

                )
                btn_delete = tk.Button(
                    master=root,
                    text="Delete",
                    command=lambda id=preset.id: self._handle_preset_delete_btn_click(id)
                )
                lbl.grid(row=row, column=0, sticky=tk.W)
                btn_delete.grid(row=row, column=1, padx=(3,0))
                row += 1
        else:
            lbl_no_presets = tk.Label(
                master=root,
                text="(No presets)"
            )
            lbl_no_presets.grid(sticky=tk.W)

    def _handle_settings_open_btn_click(self):
        if not self._frm_settings.winfo_ismapped():
            self._show_settings()

    def _show_settings(self):
        self._frm_settings.grid(sticky=(tk.W, tk.E))

    def _handle_settings_close_btn_click(self):
        self._frm_settings.grid_remove()

    def update_view(self, presets, active_id=None):
        """Updates the preset view.

        Args:
            presets: The saved presets for the current tool as a list
                     of preset objects corresponding to the current tool type.
            active_id : An integer with the identifying id for
                        the currently active preset. Defaults to None.
        """

        self._presets = presets
        self._active_id = active_id
        self._scroll_preset_buttons.clear_content()
        self._scroll_preset_buttons.populate_content(self._populate_preset_buttons)
        self._scroll_settings_buttons.clear_content()
        self._scroll_settings_buttons.populate_content(self._populate_settings_buttons)

    def deselect_buttons(self):
        """Deselects all buttons in the preset button view.
        """

        self._scroll_preset_buttons.deselect_content_widgets(self._original_btn_color)


class ScrollableArea:
    """A helper class for creating scrollable areas with a vertical scrollbar.
    """

    def __init__(self, root, height=120):
        """The class constructor.

        Args:
            root: The tkinter widget object containing the scrollable area.
            height: The height of the scrollable area. Defualts to 120.
        """

        self._root = root
        self._frm_main = None
        self._canvas = None
        self._frm_inner = None
        self._height = height

        self._init_scrollable_area(root)

    def _init_scrollable_area(self, root):
        self._frm_main = tk.Frame(root)

        self._canvas = tk.Canvas(self._frm_main)
        self._canvas.grid(sticky=tk.EW)

        scrollbar = tk.Scrollbar(self._frm_main, orient=tk.VERTICAL, command=self._canvas.yview)
        scrollbar.grid(row=0, column=1, sticky=(tk.NS, tk.E))
        self._canvas.configure(yscrollcommand=scrollbar.set)

        self._frm_inner = tk.Frame(self._canvas)
        self._canvas.create_window((0,0), window=self._frm_inner, anchor=tk.NW)

        self._frm_main.columnconfigure(1, weight=1)
        self._frm_main.pack(expand=True, fill="both")

    def populate_content(self, populate):
        """Populates the content in the scrollable area.

        Args:
            populate: A function creating the content in the tkinter widget
                      passed as an argument.
        """

        populate(self._frm_inner)
        self._frm_inner.update_idletasks()
        bbox = self._canvas.bbox(tk.ALL)
        self._canvas.configure(scrollregion=bbox, width=bbox[2]-bbox[0], height=self._height)

    def clear_content(self):
        """Clears the content in the scrollable area.
        """

        for widget in self._frm_inner.winfo_children():
            widget.destroy()

    def deselect_content_widgets(self, orig_color):
        """Deselects all button widgets in the scrollable area.
        """

        for widget in self._frm_inner.winfo_children():
            if isinstance(widget, tk.Button):
                widget["highlightbackground"] = orig_color
