from PyQt6.QtWidgets import QScrollArea, QWidget, QStyleOption, QStyle
from PyQt6.QtGui import QPainter, QPaintEvent
from PyQt6.QtCore import Qt

from components.layout import Frame


class Scroll(QScrollArea):
    # Initialize scroll area
    def __init__(self, parent: QWidget | None = ...) -> None:
        super(Scroll, self).__init__(parent)
        
        # Set the object name
        self.setObjectName("scroll")
        
        # Default horizontal scroll bar policy
        self.scroll_bar_policy = Qt.ScrollBarPolicy.ScrollBarAlwaysOff
        
        self.__setupScroll()
        self.__configureWidget()
        
    # Set the horizontal scroll bar policy
    def setHorizontalScrollBarPolicy(self, a0: Qt.ScrollBarPolicy) -> None:
        return super().setHorizontalScrollBarPolicy(a0)
        
    # Add the scroll widget
    def addWidget(self, widget: QWidget) -> None:
        self.scroll_layout.layout.addWidget(widget)
    
    # Paint widget
    def paintEvent(self, a0: QPaintEvent | None) -> None:
        o = QStyleOption()
        o.initFrom(self)
        p = QPainter(self)
        self.style().drawPrimitive(QStyle.PrimitiveElement.PE_Widget, o, p, self)
        return super().paintEvent(a0)
        
    # Setup the scroll area
    def __setupScroll(self):
        self.setHorizontalScrollBarPolicy(self.scroll_bar_policy)
        self.setWidgetResizable(True)

    # Configure the scroll widget
    def __configureWidget(self):
        self.scroll_layout = Frame(self)

        self.scroll_layout.addLayout(Frame.Direction.TopToBottom)

        self.setWidget(self.scroll_layout)
