from PyQt6.QtWidgets import QWidget, QPushButton, QHBoxLayout, QLabel, QStyleOption, QStyle
from PyQt6.QtGui import QPainter, QPaintEvent, QFont
from PyQt6.QtCore import Qt

from components.ui.title_text.title_text import TitleText
from components.ui.buttons.button import Button
from components.ui.buttons.button import ButtonStyle

from typing import Optional


class Title(QWidget):
    # Initialize widget
    def __init__(self, parent: Optional[QWidget] = None) -> None:
        super(Title, self).__init__(parent)
        
        # Set the object name
        self.setObjectName("title")
        
        # Default height
        self.title_height = None
        # Default button value
        self.button = None
        # Default margin values array
        self.margins = [0, 0, 0, 0]
        # Default alignment flag
        self.alignment_flag = Qt.AlignmentFlag.AlignLeading
        # Default title text
        self.title_text = TitleText(self)
        
        self.__setupTitle()
        self.__setupLayout()
        
    # Set the title text
    def setTitleText(self, text: str, font_size: int = None, alignment: Qt.AlignmentFlag = Qt.AlignmentFlag.AlignLeading):
        self.title_text.setTitleText(text, font_size, alignment)
        
        self.title_layout.addWidget(self.title_text)

    # Set the text alignment
    def setTextAlignment(self, alignment: Qt.AlignmentFlag = Qt.AlignmentFlag.AlignLeading):
        self.title_text.setAlignment(alignment)

    # Set the title height
    def setFixedHeight(self, h: int) -> None:
        return super().setFixedHeight(h)
        
    # Set the button
    def setButton(self, text: str, style: ButtonStyle):
        self.button_layout = Button(self)
        self.button_layout.setButtonLayout(text, style)
        
        self.title_layout.addWidget(self.button_layout)
        
    # Set the button alignment
    def setButtonAlignment(self, alignment: Qt.AlignmentFlag = Qt.AlignmentFlag.AlignLeading):
        self.button_layout.setAlignment(alignment)

    # Set the margin values
    def setContentsMargins(self, left: int, top: int, right: int, bottom: int):
        self.title_layout.setContentsMargins(left, top, right, bottom)
        
    # Set the button font
    def SetButtonFont(self, font: QFont):
        self.button_layout.setFont(font)
        
    # Set the alignments value
    def setAlignment(self, flag: Qt.AlignmentFlag):
        self.title_layout.setAlignment(flag)
    
    # Setup the paint event
    def paintEvent(self, a0: QPaintEvent | None) -> None:
        o = QStyleOption()
        o.initFrom(self)
        p = QPainter(self)
        self.style().drawPrimitive(QStyle.PrimitiveElement.PE_Widget, o, p, self)
        return super().paintEvent(a0)
    
    # Setup the title
    def __setupTitle(self):
        if self.title_height:
            self.setFixedHeight(self.title_height)
    
    # Setup the layout
    def __setupLayout(self):
        self.title_layout = QHBoxLayout(self)
        self.title_layout.setContentsMargins(self.margins[0], self.margins[1], self.margins[2], self.margins[3])
        self.title_layout.setAlignment(self.alignment_flag)
        