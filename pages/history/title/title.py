from PyQt6.QtGui import QPaintEvent
from PyQt6.QtWidgets import QWidget, QHBoxLayout, QLabel
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QPalette


class Title(QWidget):
    def __init__(self, parent=None):
        super(Title, self).__init__(parent)
        
        # self.setObjectName("Title")
        self.title_layout = QHBoxLayout(self)
        
        self.title_frame = QLabel("test label", parent=self)
        self.title_layout.addWidget(self.title_frame)
        
        self.setStyleSheet("Title {background-color: red; border: 2px solid blue}")
        
    def paintEvent(self, a0: QPaintEvent | None) -> None:
        self.palette().setBackgroundRole(QPalette.ColorRole.Window)
        return super().paintEvent(a0)