from PyQt6.QtWidgets import QPushButton, QWidget, QStyleOption, QStyle
from PyQt6.QtGui import QIcon, QFont, QPainter, QPaintEvent

from typing import Optional


class ButtonBorder(QPushButton):
    def __init__(
        self,
        icon: Optional[QIcon],
        text: Optional[str],
        parent: Optional[QWidget] = None
    ):
        # Button border widget
        super(ButtonBorder, self).__init__(text, parent)
        
        self.setObjectName("buttonBorder")
        
        if icon: self.setIcon(icon)
        
        self.setFont(self.setup_font())
        
    # Paint widget
    def paintEvent(self, a0: QPaintEvent | None) -> None:
        o = QStyleOption()
        o.initFrom(self)
        p = QPainter(self)
        self.style().drawPrimitive(QStyle.PrimitiveElement.PE_Widget, o, p, self)
        return super().paintEvent(a0)
        
    # Set font
    def setup_font(self):
        font = QFont()
        font.setFamily("Montserrat")
        font.setPointSize(8)
        return font