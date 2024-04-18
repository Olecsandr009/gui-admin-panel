from PyQt6.QtWidgets import QFrame, QVBoxLayout, QLabel, QPushButton, QToolButton
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QIcon

from utils.image.image import Image


class Json():
    def __init__(self, parent, name: str):
        super().__init__()
        
        self.parent = parent
        self.name = name
        
    # Налаштування елементів
    def setup_layout(self):
        json_frame = QLabel(parent=self.parent)
        json_frame.setObjectName("json")
        
        json_layout = QVBoxLayout(json_frame)
        
        image = Image(json_frame, "media/icons/json-file.png", 100, 100)
        json_image = image.setup_layout()
        
        json_name = QLabel(self.name, json_frame)
        json_name.setObjectName("jsonText")
        
        json_layout.addWidget(json_image)
        json_layout.addWidget(json_name)
        
        return json_frame