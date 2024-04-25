from PyQt6.QtWidgets import QWidget, QFrame

from typing import Optional


class Tools(QWidget):
    def __init__(self, parent: Optional[QWidget] = None):
        super(Tools, self).__init__(parent)
        
        