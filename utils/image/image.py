from PyQt6.QtWidgets import QWidget, QLabel
from PyQt6.QtGui import QPixmap

from typing import Optional
from urllib.request import urlopen


class Image(QLabel):
    def __init__(
        self,
        path: str,
        width: int,
        height: int,
        parent: Optional[QWidget] = None,
        url: Optional[str] = None
    ):
        # Image widget
        super(Image, self).__init__(parent)
        try:
            if not url:
                image_pixmap = QPixmap(path)
                image_pixmap = image_pixmap.scaled(width, height)
            else:
                data = urlopen(url).read()
                image_pixmap = QPixmap()
                image_pixmap.loadFromData(data)
                # image_pixmap = image_pixmap.scaled(width, height)
            self.setPixmap(image_pixmap)
        except Exception as e:
            print(f"Error loading image: {e}")