from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QWidget

from components.layout.layout.layout import Layout, LayoutInterface


class Container(QWidget, LayoutInterface):

    Direction = Layout.Direction

    # Initialize container
    def __init__(self):
        super().__init__()

        self.layout = None

    # Add layout
    def addLayout(self, direction: Layout.Direction):
        self.layout = Layout(direction, self)

        self.setLayout(self.layout)

    # Set the layout alignment (abstract method)
    def setLayoutAlignment(self, alignment: Qt.AlignmentFlag) -> None:
        self.layout.setAlignment(alignment)

    # Set the layout margins (abstract method)
    def setLayoutMargins(self, left: int, top: int, right: int, bottom: int) -> None:
        self.layout.setContentsMargins(left, top, right, bottom)

    # Add the space (abstract method)
    def addLayoutSpacing(self, space: int) -> None:
        self.layout.addSpace(space)

    # Add the widget (abstract method)
    def addLayoutWidget(self, widget: QWidget) -> None:
        self.layout.addWidget(widget)
