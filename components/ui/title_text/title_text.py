from PyQt6.QtWidgets import QWidget, QLabel, QFrame, QVBoxLayout, QStyleOption, QStyle
from PyQt6.QtGui import QPainter, QPaintEvent
from PyQt6.QtCore import Qt

from typing import Optional

from utils.font.font import Font


class TitleText(QFrame):
    # Initialize title text
    def __init__(self, parent: Optional[QWidget] = None) -> None:
        super(TitleText, self).__init__(parent)
        
        # Set the object name
        self.setObjectName("title_text")
        
        # Default margin values
        self.margin = [0, 0, 0, 0]
        # Default alignment value
        self.alignment = Qt.AlignmentFlag.AlignTop
        
        self.__setupTitleText()
        self.__setupLayout()
        
        self.setLayout(self.text_layout)
        
    # Set the title text
    def setTitleText(self, text: str, font_size: int = None, alignment: Qt.AlignmentFlag = Qt.AlignmentFlag.AlignLeft):
        textWidget = QLabel(text=text, parent=self)
        textWidget.setObjectName("title_text_value")
        
        font = Font()
        
        if font_size:
            font.setPointSize(font_size)
        
        textWidget.setFont(font)
        
        textWidget.setAlignment(alignment)
        
        self.text_layout.addWidget(textWidget)
        
    # Set the alignment
    def setAlignment(self, alignment: Qt.AlignmentFlag = Qt.AlignmentFlag.AlignTop):
        self.text_layout.setAlignment(alignment)
        
    # Setup the paint event
    def paintEvent(self, a0: QPaintEvent | None) -> None:
        o = QStyleOption()
        o.initFrom(self)
        p = QPainter(self)
        self.style().drawPrimitive(QStyle.PrimitiveElement.PE_Widget, o, p, self)
        return super().paintEvent(a0)
        
    # Setup the title text
    def __setupTitleText(self):
        pass
        
    # Setup the layout
    def __setupLayout(self):
        self.text_layout = QVBoxLayout(self)
        self.text_layout.setContentsMargins(self.margin[0], self.margin[1], self.margin[2], self.margin[3])
        self.text_layout.setAlignment(self.alignment)