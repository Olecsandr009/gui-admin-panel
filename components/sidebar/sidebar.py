from PyQt6.QtWidgets import QWidget, QVBoxLayout, QPushButton, QStackedWidget, QFrame, QHBoxLayout, QLabel
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QFont

from typing import List

from components.sidebar.logo.logo import Logo

# , stack: QStackedWidget
class Sidebar():
    def __init__(self, parent, stack:QStackedWidget, list: List[str]):
        super().__init__()

        self.parent = parent
        self.stack = stack
        self.list = list
        
        self.width = 250
        self.name = "sidebar"

    # Налаштування елементів бокової панелі
    def setup_layout(self):
        sidebar = QWidget(parent=self.parent)
        sidebar.setObjectName("sidebar")
        sidebar_layout = QVBoxLayout(sidebar)
        sidebar_layout.setAlignment(Qt.AlignmentFlag.AlignTop)
        
        logo = Logo(parent=sidebar)
        sidebar_logo = logo.setup_layout()
        sidebar_nav = self.setup_nav(sidebar)
        
        sidebar_layout.addWidget(sidebar_logo)
        sidebar_layout.addSpacing(20)
        sidebar_layout.addWidget(sidebar_nav)
        sidebar_layout.setContentsMargins(12, 12, 12, 12)
        
        sidebar.setLayout(sidebar_layout)
        
        self.setup_ui(sidebar)
        
        return sidebar
    
    # Налаштування вигляду бокової панелі
    def setup_ui(self, parent): 
        parent.setFixedWidth(self.width)
        parent.setMinimumWidth(self.width)
        
    # Налаштування навігації
    def setup_nav(self, parent):
        self.sidebar_nav = QFrame(parent=parent)
        self.sidebar_nav.setObjectName("sidebar_nav")
        nav_layout = QVBoxLayout(self.sidebar_nav)
        nav_layout.setContentsMargins(0,0,0,0)
        
        self.fill_navigation_list(layout=nav_layout, list=self.list)
        
        return self.sidebar_nav
        
    # Налаштування фону
    def setup_font(self):
        font = QFont()
        font.setFamily("Montserrat")
        font.setPointSize(12)
        return font
    
    # Заповнення списку для навігації
    def fill_navigation_list(self, layout: QVBoxLayout | QHBoxLayout, list: List[str]):
        if len(list):
            font = self.setup_font()
            
            for index, item in enumerate(list):
                button = QPushButton(item, parent=self.sidebar_nav)
                button.setObjectName("ItemBtn")
                button.setFont(font)
                
                if index == 0:
                    button.setStyleSheet("QPushButton {background-color: #191919}")
                
                layout.addWidget(button)
                def on_button_click(clicked_index=index):
                    return lambda: self.showPage(index=clicked_index)
                
                button.clicked.connect(on_button_click())
                
    # Відобраєення певної сторінки  
    def showPage(self, index):
        self.stack.setCurrentIndex(index)

        for button in self.sidebar_nav.findChildren(QPushButton):
            button_index = self.sidebar_nav.findChildren(QPushButton).index(button)
            button.setStyleSheet("QPushButton {background-color: transparent;}")
            
            if button_index == index:
                button.setStyleSheet("QPushButton {background-color: #191919}")