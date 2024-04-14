from PyQt6.QtWidgets import QFrame, QHBoxLayout, QLabel, QSizePolicy, QVBoxLayout
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QFont

from utils.image.image import Image


class Logo():
    def __init__(self, parent):
        super().__init__()
        
        self.parent = parent
    
    # Налаштування елементів
    def setup_layout(self):
        logo = QFrame(parent=self.parent)
        logo.setObjectName("logo")
        logo.setMinimumHeight(50)
        logo.setMaximumHeight(100)
        logo_layout = QHBoxLayout(logo)
        logo_layout.setContentsMargins(0,0,0,0)
        logo_layout.setAlignment(Qt.AlignmentFlag.AlignLeft)
        
        image = Image(logo, "media/logo.png", 50, 50)
        logo_image = image.setup_layout()
        
        logo_text = QLabel("Neon", parent=logo)
        logo_text.setObjectName("logoText")
        font = self.setup_font()
        logo_text.setFont(font)
        
        logo_layout.addWidget(logo_image)
        logo_layout.addWidget(logo_text)
        logo_layout.setContentsMargins(0, 0, 0, 0)
        
        return logo
        
    # Налаштування фону
    def setup_font(self):
        font = QFont()
        font.setFamily("Montserrat")
        font.setPointSize(18)
        font.setBold(True)
        return font