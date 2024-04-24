from PyQt6.QtWidgets import QWidget, QHBoxLayout, QFrame, QStyleOption, QStyle
from PyQt6.QtGui import QPainter, QPaintEvent

from components.title_bar.window_tools.window_tools import WindowTools


class TitleBar(QWidget):
    def __init__(self, main, parent = None):
        super(TitleBar, self).__init__(parent)
        self.setObjectName("titleBar")
        
        self.parent = parent
        self.main = main
        
        self.setup_layout()
        
        self.search_layout()
        self.theme_layout()
        self.window_tools()
        
        self.setLayout(self.title_layout)
        
    # Setup title bar layout
    def setup_layout(self):
        self.title_layout = QHBoxLayout(self)
        self.title_layout.setContentsMargins(0, 0, 0, 0)
        
    # Setup search layout
    def search_layout(self):
        search = QFrame(parent=self)
        
        self.title_layout.addWidget(search)
        
    #Setup theme layout
    def theme_layout(self):
        theme = QFrame(parent=self)
        
        self.title_layout.addWidget(theme)
        
    # Setup tool layout
    def window_tools(self):
        window_tools = WindowTools(parent=self.parent, main=self.main)
        
        self.title_layout.addWidget(window_tools)
        
    # Paint widget
    def paintEvent(self, a0: QPaintEvent | None) -> None:
        o = QStyleOption()
        o.initFrom(self)
        p = QPainter(self)
        self.style().drawPrimitive(QStyle.PrimitiveElement.PE_Widget, o, p, self)
        return super().paintEvent(a0)