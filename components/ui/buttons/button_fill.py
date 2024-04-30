from PyQt6.QtWidgets import QFrame, QPushButton, QStyleOption, QStyle, QWidget, QVBoxLayout
from PyQt6.QtGui import QFont, QPainter, QPaintEvent, QIcon
from PyQt6.QtCore import Qt

from typing import Optional


class ButtonFill(QPushButton):
    def __init__(self, text: str, parent: Optional[QWidget] = None) -> None:
        super(ButtonFill, self).__init__(text, parent)
        
        # Set the object name
        self.setObjectName("button_fill")
        
        self.__configureButtonWidget()
        
    # Set the text font
    def setFont(self, a0: QFont) -> None:
        return super().setFont(a0)
    
    # Set the button icon
    def setIcon(self, icon: QIcon) -> None:
        return super().setIcon(icon)
    
    # Paint widget
    def paintEvent(self, a0: QPaintEvent | None) -> None:
        o = QStyleOption()
        o.initFrom(self)
        p = QPainter(self)
        self.style().drawPrimitive(QStyle.PrimitiveElement.PE_Widget, o, p, self)
        return super().paintEvent(a0)
    
    # Configure the button border
    def __configureButtonWidget(self):
        pass