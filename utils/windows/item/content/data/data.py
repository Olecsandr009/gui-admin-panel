from PyQt6.QtWidgets import QWidget, QStyleOption, QStyle, QVBoxLayout
from PyQt6.QtGui import QPainter, QPaintEvent
from PyQt6.QtCore import Qt

from typing import Optional

from utils.scroll.scroll import Scroll


class Data(QWidget):
    # Initialize the apply widget
    def __init__(self, parent: Optional[QWidget]) -> None:
        super(Data, self).__init__(parent)

        # Set object name
        self.setObjectName("item_data")
        
        # Default margin values
        self.margin = [0, 0, 0, 0]
        # Default alignment value
        self.alignment = Qt.AlignmentFlag.AlignLeading
        
        self.__dataLayout()
        
        self.setLayout(self.data_layout)

    # Set margin values
    def setContentsMargins(self, left, top, right, bottom):
        self.data_layout.setContentsMargins(left, top, right, bottom)

    # Set alignment value
    def setAlignment(self, alignment: Qt.AlignmentFlag = Qt.AlignmentFlag.AlignLeading):
        self.data_layout.setAlignment(alignment)

    # Set data content
    def setContent(self, content: QWidget):
        scroll_layout = Scroll(self)
        scroll_layout.setWidget(content)
        
        self.data_layout.addWidget(scroll_layout)

    # Setup the paint event
    def paintEvent(self, a0: QPaintEvent | None) -> None:
        o = QStyleOption()
        o.initFrom(self)
        p = QPainter(self)
        self.style().drawPrimitive(QStyle.PrimitiveElement.PE_Widget, o, p, self)
        return super().paintEvent(a0)
    
    # Setup the data layout
    def __dataLayout(self):
        self.data_layout = QVBoxLayout(self)
        self.data_layout.setContentsMargins(self.margin[0], self.margin[1], self.margin[2], self.margin[3])
        self.data_layout.setAlignment(self.alignment)