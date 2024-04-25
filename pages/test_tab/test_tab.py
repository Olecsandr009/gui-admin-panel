from PyQt6.QtWidgets import QWidget, QVBoxLayout, QPushButton, QStyleOption, QStyle
from PyQt6.QtGui import QPainter, QPaintEvent


class TestTab(QWidget):
    def __init__(self, parent):
        super(TestTab, self).__init__(parent)
        self.setObjectName("testTab")
        
        self.setup_layout()
        self.button_widget()
        
        self.setLayout(self.test_layout)
        
    # Setup test layout
    def setup_layout(self):
        self.test_layout = QVBoxLayout(self)
        self.test_layout.setContentsMargins(0, 0, 0, 0)
        
    # Setup button widget
    def button_widget(self):
        button = QPushButton('text', parent=self)

        self.test_layout.addWidget(button)