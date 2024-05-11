from PyQt6.QtWidgets import QWidget, QStyleOption, QStyle
from PyQt6.QtGui import QPaintEvent, QPainter
from PyQt6.QtCore import Qt

from components.layout.container.container import Container
from components.layout.tools.tools_buttons.tools_buttons import ToolsButtons


class Tools(Container):
    # Initialize tools
    def __init__(self, main: QWidget):
        super().__init__()

        self.main = main

        self.__configureLayout()
        self.__configureButtons()

    # Configure the layout
    def __configureLayout(self):
        self.addLayout(self.Direction.LeftToRight)

        self.layout.setContentsMargins(0, 0, 0, 0)

    # Configure the tools buttons
    def __configureButtons(self):
        self.tools_button = ToolsButtons(self.main)
        self.tools_button.layout.setAlignment(Qt.AlignmentFlag.AlignRight)
        self.tools_button.layout.setContentsMargins(0, 0, 0, 0)
        self.tools_button.setFixedHeight(30)

        self.layout.addWidget(self.tools_button)

    # Setup the paint event
    def paintEvent(self, a0: QPaintEvent | None) -> None:
        o = QStyleOption()
        o.initFrom(self)
        p = QPainter(self)
        self.style().drawPrimitive(QStyle.PrimitiveElement.PE_Widget, o, p, self)
        return super().paintEvent(a0)
