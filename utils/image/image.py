from PyQt6.QtWidgets import QWidget, QLabel, QVBoxLayout, QHBoxLayout
from PyQt6.QtGui import QPixmap


class Image(QLabel):
    def __init__(self, parent, image_path, width, height):
        super().__init__()
        
        self.parent = parent
        self.image_path = image_path
        self.width = width
        self.height = height
        
    # Налаштування елементів
    def setup_layout(self):
        image_label = QLabel(parent=self)
        
        image_pixmap = QPixmap(self.image_path)
        image_pixmap = image_pixmap.scaled(self.width, self.height)
        
        image_label.setPixmap(image_pixmap)
        
        return image_label