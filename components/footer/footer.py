from PyQt6.QtWidgets import QFrame, QHBoxLayout, QLabel
from PyQt6.QtCore import Qt

from utils.image.image import Image


class Footer():
    def __init__(self, parent):
        super().__init__()
        
        self.parent = parent
        
    def setup_layout(self):
        footer = QFrame(parent=self.parent)
        footer.setObjectName("footer")
        footer_layout = QHBoxLayout(footer)
        footer_layout.setAlignment(Qt.AlignmentFlag.AlignRight)
        footer_layout.setContentsMargins(0, 0, 0, 0)
        
        image = Image(footer, "media/icon-footer.png", 25, 25)
        image_layout = image.setup_layout()
        
        footer_text1 = QLabel("author: Oleksandr", parent=footer)
        footer_text1.setObjectName("footerText")
        footer_text2 = QLabel("type: Json", parent=footer)
        footer_text2.setObjectName("footerText")
        
        footer_layout.addWidget(footer_text2)
        footer_layout.setSpacing(40)
        footer_layout.addWidget(footer_text1)
        footer_layout.setSpacing(40)
        footer_layout.addWidget(image_layout)
        
        return footer