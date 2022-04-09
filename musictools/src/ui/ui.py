from ui.tuning_fork_view import TuningForkView


class UI:
    def __init__(self, root):
        self._root = root
        self._tuning_fork_view = TuningForkView(self._root)

    def start(self):
        self._tuning_fork_view.pack()
