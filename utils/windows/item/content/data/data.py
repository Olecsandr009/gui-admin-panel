from PyQt6.QtWidgets import QWidget, QStyleOption, QStyle
from PyQt6.QtGui import QPainter, QPaintEvent
from PyQt6.QtCore import Qt

from typing import Optional

from utils.scroll.scroll import Scroll
from utils.windows.item.content.data.item import Item

from components.layout import Frame
from components.ui import Inputs


class Data(Frame):
    # Initialize the apply widget
    def __init__(self, parent: Optional[QWidget]) -> None:
        super(Data, self).__init__(parent)

        # Set object name
        self.setObjectName("item_data")
        self.addLayout(Frame.Direction.TopToBottom)

        self.__configureScroll()

    # Configure the scroll layout
    def __configureScroll(self):
        self.scroll_layout = Scroll(self)

        # self.layout.addWidget(self.scroll_layout)

    # Set the edit inputs
    def setInputsScheme(self, scheme, data):
        if not len(scheme) or not len(data): return

        for item in scheme:
            item_layout = Item(item["key"], item["input"], data)

            self.scroll_layout.addWidget(item_layout)

        self.layout.addWidget(self.scroll_layout)
        print("yes")

    # Setup the paint event
    def paintEvent(self, a0: QPaintEvent | None) -> None:
        o = QStyleOption()
        o.initFrom(self)
        p = QPainter(self)
        self.style().drawPrimitive(QStyle.PrimitiveElement.PE_Widget, o, p, self)
        return super().paintEvent(a0)
