from PyQt6.QtWidgets import QFrame, QHBoxLayout, QLabel, QWidget, QStyleOption, QStyle
from PyQt6.QtGui import QFont, QPainter, QPaintEvent
from PyQt6.QtCore import Qt

from typing import Optional
from utils.image.image import Image


class Logo(QFrame):
    def __init__(self, parent: Optional[QWidget] = None):
        # Logo layout
        super(Logo, self).__init__(parent)
        self.setObjectName("logo")
        
        self.parent = parent
        
        self.setMinimumHeight(50)
        self.setMaximumHeight(100)
        
        self.setup_layout()
        
        self.image_widget()
        self.text_widget()
        
        self.setLayout(self.logo_layout)
        
    # Setup layout
    def setup_layout(self):
        self.logo_layout = QHBoxLayout(self)
        self.logo_layout.setContentsMargins(0, 0, 0, 0)
        self.logo_layout.setAlignment(Qt.AlignmentFlag.AlignLeft)
        
    # Setup logo image
    def image_widget(self):
        image = Image("media/logo.png", 50, 50, self)
        self.logo_layout.addWidget(image)
        
    # Setup logo name
    def text_widget(self):
        text = QLabel("Neon", parent=self)
        text.setObjectName("logoText")
        text.setFont(self.setup_font())
        self.logo_layout.addWidget(text)
        
    # Paint widget
    def paintEvent(self, a0: QPaintEvent | None) -> None:
        o = QStyleOption()
        o.initFrom(self)
        p = QPainter(self)
        self.style().drawPrimitive(QStyle.PrimitiveElement.PE_Widget, o, p, self)
        return super().paintEvent(a0)
        
    # Set font
    def setup_font(self):
        font = QFont()
        font.setFamily("Montserrat")
        font.setPointSize(18)
        font.setBold(True)
        return font