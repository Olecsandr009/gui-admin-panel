from PyQt6.QtWidgets import QWidget, QStyleOption, QStyle, QFrame, QVBoxLayout, QTextEdit
from PyQt6.QtGui import QPainter, QPaintEvent
from PyQt6.QtCore import Qt

from typing import Optional

class TextEdit(QFrame):
    # Initialize the apply widget
    def __init__(self, parent: Optional[QWidget]) -> None:
        super(TextEdit, self).__init__(parent)

        # Set object name
        self.setObjectName("inputs_text_edit")
        
        # Default margin values
        self.margin = [0, 0, 0, 0]
        # Default alignment value
        self.alignment = Qt.AlignmentFlag.AlignLeading
        
        self.__textEditLayout()
        self.__configureLineEdit()
        
        self.setLayout(self.text_layout)

    # Setup the paint event
    def paintEvent(self, a0: QPaintEvent | None) -> None:
        o = QStyleOption()
        o.initFrom(self)
        p = QPainter(self)
        self.style().drawPrimitive(QStyle.PrimitiveElement.PE_Widget, o, p, self)
        return super().paintEvent(a0)
    
    # Set the margin values
    def setContentsMargins(self, left: int, top: int, right: int, bottom: int):
        self.text_layout.setContentsMargins(left, top, right, bottom)
        
    # Set the alignment values
    def setAlignment(self, alignment):
        self.text_layout.setAlignment(alignment)
        
    # Set the placeholder text
    def setPlaceholderText(self, text: str):
        self.text_edit.setPlaceholderText(text)
      
    # Set the fixed height value
    def setFixedHeight(self, h: int) -> None:
        self.text_edit.setFixedHeight(h)
        
    # Setup the text edit layout
    def __textEditLayout(self):
        self.text_layout = QVBoxLayout(self)
        self.text_layout.setContentsMargins(self.margin[0], self.margin[1], self.margin[2], self.margin[3])
        self.text_layout.setAlignment(self.alignment)
    
    # Configure the text edit widget
    def __configureLineEdit(self):
        self.text_edit = QTextEdit(self)
        self.text_edit.setObjectName("inputs_text_edit_area")
        
        self.text_layout.addWidget(self.text_edit)