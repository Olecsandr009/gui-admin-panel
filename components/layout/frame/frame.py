from PyQt6.QtWidgets import QFrame, QWidget

from components.layout.layout.layout import Layout


class Frame(QFrame):

    Direction = Layout.Direction

    # Initialize frame
    def __init__(self, parent: QWidget = None):
        super().__init__(parent)

        self.margin = [0, 0, 0, 0]
        self.layout: Layout = None

    # Add layout
    def addLayout(self, direction: Layout.Direction):
        self.layout = Layout(direction, self)
        self.layout.setContentsMargins(*self.margin)

        self.setLayout(self.layout)
