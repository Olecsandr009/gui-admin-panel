from PyQt6.QtWidgets import QScrollArea, QWidget, QStyleOption, QStyle, QVBoxLayout
from PyQt6.QtGui import QPainter, QPaintEvent
from PyQt6.QtCore import Qt


class Scroll(QScrollArea):
    # Initialize scroll area
    def __init__(self, parent: QWidget | None = ...) -> None:
        super(Scroll, self).__init__(parent)
        
        # Set the object name
        self.setObjectName("scroll")
        
        # Default horizontal scroll bar policy
        self.scroll_bar_policy = Qt.ScrollBarPolicy.ScrollBarAlwaysOff
        
        self.__setupScroll()
        
    # Set the horizontal scroll bar policy
    def setHorizontalScrollBarPolicy(self, a0: Qt.ScrollBarPolicy) -> None:
        return super().setHorizontalScrollBarPolicy(a0)
        
    # Set the scroll widget
    def setWidget(self, w: QWidget | None) -> None:
        return super().setWidget(w)
    
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