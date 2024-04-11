from PyQt6.QtWidgets import QMainWindow, QHBoxLayout, QWidget, QPushButton
from sidebar.sidebar import Sidebar


class Window(QMainWindow):
    def __init__(self):
        super().__init__()
        
        self.title = "GUI Admin panel"
        self.top = 100
        self.left = 200
        self.width = 1000
        self.height = 600
        
        self.initUI()
        
    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
        
        self.setObjectName('admin-window')
        self.setProperty('class', 'admin-window')
        
        with open("window/window.css", "r") as file:
            self.setStyleSheet(file.read())
            
        self.button = QPushButton("click")
            
        sidebar = Sidebar()
        layout = QHBoxLayout()
        layout.addWidget(sidebar)
        layout.addWidget(self.button)
        
        self.setCentralWidget(QWidget())
        self.centralWidget().setLayout(layout)
        