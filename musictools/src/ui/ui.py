from ui.tuning_fork_view import TuningForkView
from ui.metronome_view import MetronomeView


class UI:
    """Class describing the root UI view of the app.
    """

    def __init__(self, root):
        """The class constructor.

        Args:
            root: The root Tkinter window.
        """

        self._root = root
        self._tuning_fork_view = TuningForkView(self._root)
        self._metronome_view = MetronomeView(self._root)

    def start(self):
        """Adds the tuning fork and metronome views to the layout.
        """

        self._tuning_fork_view.pack()
        self._metronome_view.pack()
