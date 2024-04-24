from PyQt6.QtWidgets import QWidget, QLabel
from PyQt6.QtGui import QPixmap

from typing import Optional


class Image(QLabel):
    def __init__(
        self,
        path: str,
        width: int,
        height: int,
        parent: Optional[QWidget] = None
    ):
        # Image widget
        super(Image, self).__init__(parent)
        
        image_pixmap = QPixmap(path)
        image_pixmap = image_pixmap.scaled(width, height)
        
        self.setPixmap(image_pixmap)