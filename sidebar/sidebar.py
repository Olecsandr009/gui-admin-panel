from PyQt6.QtWidgets import QWidget, QVBoxLayout, QPushButton


class Sidebar(QWidget):
    def __init__(self):
        super().__init__()
        
        self.width = 300
        self.UI()
    
    def UI(self):
        self.setFixedWidth(self.width)
        self.setMinimumWidth(self.width)
        
        self.setStyleSheet("background-color: red;")
        
        self.setObjectName('sidebar')
        self.setProperty('class', 'sidebar')
        
        with open("sidebar/sidebar.css", "r") as file:
            self.setStyleSheet(file.read())
            
        layout = QVBoxLayout()
        
        self.button1 = QPushButton()

        layout.addWidget(self.button1)
        
        self.setLayout(layout)
