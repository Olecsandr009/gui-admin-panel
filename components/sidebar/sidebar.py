from PyQt6.QtWidgets import QWidget, QVBoxLayout, QPushButton, QStackedWidget, QFrame, QHBoxLayout, QLabel
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QFont

from components.sidebar.logo.logo import Logo

# , stack: QStackedWidget
class Sidebar():
    def __init__(self, parent, stack:QStackedWidget):
        super().__init__()

        self.parent = parent
        self.stack = stack
        
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
        sidebar_nav = QFrame(parent=parent)
        sidebar_nav.setObjectName("sidebar_nav")
        nav_layout = QVBoxLayout(sidebar_nav)
        nav_layout.setContentsMargins(0,0,0,0)
        
        font = self.setup_font()
        
        self.button1 = QPushButton("Всі товари", parent=sidebar_nav)
        self.button1.setObjectName("ItemBtn")
        self.button1.setFont(font)
        self.button1.setStyleSheet("QPushButton {background-color: #191919}")
        self.button2 = QPushButton("Добавити новий", parent=sidebar_nav)
        self.button2.setObjectName("ItemBtn")
        self.button2.setFont(font)
        
        self.button1.clicked.connect(self.showPage1)
        self.button2.clicked.connect(self.showPage2)
        
        nav_layout.addWidget(self.button1)
        nav_layout.addWidget(self.button2)
        
        return sidebar_nav

    def showPage1(self):
        self.stack.setCurrentIndex(0)
        self.button1.setStyleSheet("QPushButton {background-color: #191919}")
        self.button2.setStyleSheet("QPushButton {background-color: transparent}")

    def showPage2(self):
        self.stack.setCurrentIndex(1)
        self.button2.setStyleSheet("QPushButton {background-color: #191919}")
        self.button1.setStyleSheet("QPushButton {background-color: transparent}")
        
    # Налаштування фону
    def setup_font(self):
        font = QFont()
        font.setFamily("Montserrat")
        font.setPointSize(12)
        return font