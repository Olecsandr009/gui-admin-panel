from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QFrame, QWidget

from components.layout.layout.layout import Layout, LayoutInterface


class Frame(QFrame, LayoutInterface):

    Direction = Layout.Direction

    # Initialize frame
    def __init__(self):
        super().__init__()

        self.layout: Layout = None

    # Add layout
    def addLayout(self, direction: Layout.Direction):
        self.layout = Layout(direction, self)

        self.setLayout(self.layout)

    # Set the layout margins (abstract method)
    def setLayoutMargins(self, left: int, top: int, right: int, bottom: int) -> None:
        self.layout.setContentsMargins(left, top, right, bottom)

    # Set the layout alignment (abstract method)
    def setLayoutAlignment(self, alignment: Qt.AlignmentFlag) -> None:
        self.layout.setAlignment(alignment)

    # Add the layout widget (abstract method)
    def addLayoutWidget(self, widget: QWidget) -> None:
        self.layout.addWidget(widget)

    # Add the layout space (abstract method)
    def addLayoutSpacing(self, space: int) -> None:
        self.layout.addSpacing(space)
