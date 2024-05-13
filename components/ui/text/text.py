from PyQt6.QtWidgets import QLabel, QWidget, QStyleOption, QStyle
from PyQt6.QtGui import QPaintEvent, QPainter


class Text(QLabel):
    # Initialize text
    def __init__(self, text: str, parent: QWidget = None):
        super(Text, self).__init__(text=text, parent=parent)

    # Paint widget
    def paintEvent(self, a0: QPaintEvent | None) -> None:
        o = QStyleOption()
        o.initFrom(self)
        p = QPainter(self)
        self.style().drawPrimitive(QStyle.PrimitiveElement.PE_Widget, o, p, self)
        return super().paintEvent(a0)
