from PyQt6.QtWidgets import QBoxLayout, QWidget


class Layout(QBoxLayout):
    def __init__(self, direction: QBoxLayout.Direction, parent: QWidget = None):
        super().__init__(direction, parent)
