from PyQt6.QtWidgets import QWidget, QHBoxLayout, QPushButton, QMainWindow, QFrame
from PyQt6.QtGui import QIcon

from components.title_bar.window_tools.window_tools import WindowTools


class TitleBar():
    def __init__(self, parent, main):
        super().__init__()
        
        self.parent = parent
        self.main = main
        
    # Налаштування елементів
    def setup_layout(self):
        title_bar = QWidget(parent=self.parent)
        title_bar.setObjectName("titleBar")
        title_layout = QHBoxLayout(title_bar)
        
        window_tools = WindowTools(parent=self.parent, main=self.main)
        
        title_tool = window_tools.setup_layout()
        theme = QFrame(parent=self.parent)
        search = QFrame(parent=self.parent)
        
        title_layout.addWidget(search)
        title_layout.addWidget(theme)
        title_layout.addWidget(title_tool)
        
        return title_bar