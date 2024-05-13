from PyQt6.QtWidgets import QWidget, QStyleOption, QStyle, QLineEdit, QFrame, QVBoxLayout
from PyQt6.QtGui import QPainter, QPaintEvent
from PyQt6.QtCore import Qt

from typing import Optional

class LineEdit(QFrame):
    # Initialize the apply widget
    def __init__(self, key: str = None, parent: Optional[QWidget] = None) -> None:
        super(LineEdit, self).__init__(parent)

        # Set object name
        self.setObjectName("inputs_line_edit")
        
        # Default margin values
        self.margin = [0, 0, 0, 0]
        # Default alignment value
        self.alignment = Qt.AlignmentFlag.AlignLeading

        self.__lineEditLayout()
        self.__configureLineEdit()
        
        self.setLayout(self.line_layout)

    # Setup the paint event
    def paintEvent(self, a0: QPaintEvent | None) -> None:
        o = QStyleOption()
        o.initFrom(self)
        p = QPainter(self)
        self.style().drawPrimitive(QStyle.PrimitiveElement.PE_Widget, o, p, self)
        return super().paintEvent(a0)
    
    # Set the margin values
    def setContentsMargins(self, left: int, top: int, right: int, bottom: int):
        self.line_layout.setContentsMargins(left, top, right, bottom)
    
    # Set the alignment value
    def setAlignment(self, alignment: Qt.AlignmentFlag):
        self.line_layout.setAlignment(alignment)
    
    # Set the placeholder text
    def setPlaceholderText(self, text:str):
        self.line_edit.setPlaceholderText(text)

    # Set the text value
    def setText(self, text: str):
        self.line_edit.setText(text)
    
    # Set the fixed height value
    def setFixedHeight(self, h: int) -> None:
        self.line_edit.setFixedHeight(h)
    
    # Setup the line edit layout
    def __lineEditLayout(self):
        self.line_layout = QVBoxLayout(self)
        self.line_layout.setContentsMargins(self.margin[0], self.margin[1], self.margin[2], self.margin[3])
        self.line_layout.setAlignment(self.alignment)
        
    # Configure the line edit widget
    def __configureLineEdit(self):
        self.line_edit = QLineEdit(self)
        self.line_edit.setObjectName("inputs_line_edit_area")
        
        self.line_layout.addWidget(self.line_edit)