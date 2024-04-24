from PyQt6.QtWidgets import QFrame, QHBoxLayout, QLabel, QStyleOption, QStyle
from PyQt6.QtGui import QPainter, QPaintEvent
from PyQt6.QtCore import Qt

from typing import Dict

from utils.image.image import Image


class Footer(QFrame):
    def __init__(self, data: Dict[str, str], parent = None):
        # Footer layout
        super(Footer, self).__init__(parent)
        self.setObjectName("footer")
        
        self.data = data
        self.parent = parent
        self.setup_layout()
        
    def setup_layout(self):
        
        footer_layout = QHBoxLayout(self)
        footer_layout.setAlignment(Qt.AlignmentFlag.AlignRight)
        footer_layout.setContentsMargins(0, 0, 0, 0)
        
        
        for key, value in self.data.items():
            footer_text = QLabel(f"{key}: {value}; ")
            footer_text.setObjectName("footerText")
            footer_layout.addWidget(footer_text)
            footer_layout.setSpacing(40)
                
        image = Image("media/icon-footer.png", 25, 25, self)
        footer_layout.addWidget(image)
        
        self.setLayout(footer_layout)
        
    # Paint widget
    def paintEvent(self, a0: QPaintEvent | None) -> None:
        o = QStyleOption()
        o.initFrom(self)
        p = QPainter(self)
        self.style().drawPrimitive(QStyle.PrimitiveElement.PE_Widget, o, p, self)
        return super().paintEvent(a0)