from PyQt6.QtWidgets import QWidget

from components.layout.layout.layout import Layout


class Container(QWidget):

    Direction = Layout.Direction

    # Initialize container
    def __init__(self, parent: QWidget = None):
        super().__init__(parent)

        self.margin = [0, 0, 0, 0]
        self.layout: Layout = None

    # Add layout
    def addLayout(self, direction: Layout.Direction):
        self.layout = Layout(direction, self)
        self.setContentsMargins(*self.margin)

        self.setLayout(self.layout)

