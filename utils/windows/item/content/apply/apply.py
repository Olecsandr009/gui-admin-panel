from PyQt6.QtWidgets import QWidget, QHBoxLayout, QStyleOption, QStyle
from PyQt6.QtGui import QPainter, QPaintEvent
from PyQt6.QtCore import Qt

from typing import Optional

from components.ui.buttons.button import Button
from components.ui.buttons.button import ButtonStyle

class Apply(QWidget):
    # Initialize the apply widget
    def __init__(self, parent: Optional[QWidget]) -> None:
        super(Apply, self).__init__(parent)

        # Set object name
        self.setObjectName("item_apply")
        
        # Default margin values
        self.margin = [0, 0, 0, 0]
        # Default alignment value
        self.alignment = Qt.AlignmentFlag.AlignLeading
        
        self.__applyLayout()
        
        self.setLayout(self.apply_layout)
        
    # Set margin values
    def setContentsMargins(self, left: int, top: int, right: int, bottom: int):
        self.apply_layout.setContentsMargins(left, top, right, bottom)
        
    # Set alignment value
    def setAlignment(self, alignment: Qt.AlignmentFlag = Qt.AlignmentFlag.AlignLeading):
        self.apply_layout.setAlignment(alignment)
        
    # Setup the paint event
    def paintEvent(self, a0: QPaintEvent | None) -> None:
        o = QStyleOption()
        o.initFrom(self)
        p = QPainter(self)
        self.style().drawPrimitive(QStyle.PrimitiveElement.PE_Widget, o, p, self)
        return super().paintEvent(a0)
        
    # Set button layout
    def setButtonLayout(self, text: str, style: ButtonStyle):
        button = Button(self)
        button.setButtonLayout(text, style)
        
        self.apply_layout.addWidget(button)
        
    # Setup apply layout
    def __applyLayout(self):
        self.apply_layout = QHBoxLayout(self)
        self.apply_layout.setContentsMargins(self.margin[0], self.margin[1], self.margin[2], self.margin[3])
        self.apply_layout.setAlignment(self.alignment)
        