from PyQt6.QtWidgets import QWidget, QFrame, QHBoxLayout, QPushButton
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QIcon


class WindowTools():
    def __init__(self, parent, main):
        super().__init__()
        
        self.parent = parent
        self.main = main
        self.is_maximized = True
        
    # Налаштування елементів
    def setup_layout(self):
        title_tools = QFrame(parent=self.parent)
        tools_layout = QHBoxLayout(title_tools)
        tools_layout.setAlignment(Qt.AlignmentFlag.AlignRight)
        
        icon_close = QIcon("media/icons/close.png")
        icon_show = QIcon("media/icons/minus.png")
        
        maximize_button = QPushButton(parent=title_tools)
        close_button = QPushButton(parent=title_tools)
        show_button = QPushButton(parent=title_tools)
        
        maximize_button.setIcon(self.toggle_maximized_icon())
        close_button.setIcon(icon_close)
        show_button.setIcon(icon_show)
        
        maximize_button.clicked.connect(self.main.toggle_maximized)
        close_button.clicked.connect(self.main.close)
        show_button.clicked.connect(self.main.showMinimized)
        
        tools_layout.addWidget(show_button)
        tools_layout.addSpacing(6)
        tools_layout.addWidget(maximize_button)
        tools_layout.addSpacing(6)
        tools_layout.addWidget(close_button)
        
        return title_tools
        
        # self.maximize_button.setIcon(self.toggle_maximized_icon())
    
    # Зміна іконки залужності від стану вікна
    def toggle_maximized_icon(self):
        if self.parent.isMaximized():
            return QIcon("media/icons/minimize.png")
        else:
            return QIcon("media/icons/maximize.png")