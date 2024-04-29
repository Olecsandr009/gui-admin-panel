from PyQt6.QtWidgets import QFrame, QHBoxLayout, QPushButton, QStyleOption, QStyle
from PyQt6.QtGui import QPaintEvent, QPainter, QCursor
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QIcon


class WindowTools(QFrame):
    def __init__(self, main, parent = None):
        super(QFrame, self).__init__(parent)
        self.setObjectName("WidowTool")
        
        self.parent = parent
        self.main = main
        self.is_maximized = True
        
        self.setup_layout()
        
        self.show_button()
        self.maximize_button()
        self.close_button()
        
        self.setLayout(self.tools_layout)
        
    # Setup tool layout
    def setup_layout(self):
        self.tools_layout = QHBoxLayout(self)
        self.tools_layout.setAlignment(Qt.AlignmentFlag.AlignRight)
        self.tools_layout.setContentsMargins(0, 0, 0, 0)
        
    # Setup show button widget
    def show_button(self):
        show_button = QPushButton(parent=self)
        show_button.setObjectName("toolButton")
        show_button.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        
        icon_show = QIcon("media/icons/minus.png")
        
        show_button.setIcon(icon_show)
        
        show_button.clicked.connect(self.main.showMinimized)
        
        self.tools_layout.addWidget(show_button)
        self.tools_layout.addSpacing(6)
    
    # Setup maximize button widget        
    def maximize_button(self):
        maximize_button = QPushButton(parent=self)
        maximize_button.setIcon(self.toggle_maximized_icon())
        maximize_button.setObjectName("toolButton")
        
        maximize_button.clicked.connect(self.main.toggle_maximized)
        
        self.tools_layout.addWidget(maximize_button)
        self.tools_layout.addSpacing(6)
        
    # Setup close button widget
    def close_button(self):
        close_button = QPushButton(parent=self)
        icon_close = QIcon("media/icons/close.png")
        close_button.setObjectName("toolButton")
        close_button.setIcon(icon_close)
        
        close_button.clicked.connect(self.main.close)
        
        self.tools_layout.addWidget(close_button)
        
    # Paint widget
    def paintEvent(self, a0: QPaintEvent | None) -> None:
        o = QStyleOption()
        o.initFrom(self)
        p = QPainter(self)
        self.style().drawPrimitive(QStyle.PrimitiveElement.PE_Widget, o, p, self)
        return super().paintEvent(a0)
    
    # Toggle icon
    def toggle_maximized_icon(self):
        if self.parent.isMaximized():
            return QIcon("media/icons/minimize.png")
        else:
            return QIcon("media/icons/maximize.png")