from PyQt6.QtWidgets import QWidget, QStyleOption, QStyle
from PyQt6.QtGui import QPaintEvent, QPainter

from components.layout.container.container import Container
from components.layout.tools.tools_buttons.tools_buttons import ToolsButtons


class Tools(Container):
    # Initialize tools
    def __init__(self, main: QWidget):
        super().__init__()

        self.addLayout(self.Direction.LeftToRight)

        self.tools_button = ToolsButtons(main)

        self.layout.addWidget(self.tools_button)

    # Setup the paint event
    def paintEvent(self, a0: QPaintEvent | None) -> None:
        o = QStyleOption()
        o.initFrom(self)
        p = QPainter(self)
        self.style().drawPrimitive(QStyle.PrimitiveElement.PE_Widget, o, p, self)
        return super().paintEvent(a0)
