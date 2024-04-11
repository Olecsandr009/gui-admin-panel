from PyQt6.QtWidgets import QWidget, QVBoxLayout, QPushButton, QTabWidget


class Sidebar(QWidget):
    def __init__(self, tab: QTabWidget):
        super().__init__()

        self.tab = tab
        self.width = 300

        self.setup_ui()
        self.apply_styles()
        self.setup_layout()

    # Налаштування вигляду бокової панелі
    def setup_ui(self):
        self.setFixedWidth(self.width)
        self.setMinimumWidth(self.width)

    # Підключення стилів боковаї панелі
    def apply_styles(self):
        self.setObjectName('sidebar')
        self.setProperty('class', 'sidebar')
        
        with open("sidebar/sidebar.css", "r") as file:
            self.setStyleSheet(file.read())

    # Налаштування елементів бокової панелі
    def setup_layout(self):
        sidebar_layout = QVBoxLayout()

        sidebar_button1 = QPushButton("Sidebar 1")
        sidebar_button2 = QPushButton("Sidebar 2")
        sidebar_button3 = QPushButton("Sidebar 3")

        sidebar_layout.addWidget(sidebar_button1)
        sidebar_layout.addWidget(sidebar_button2)
        sidebar_layout.addWidget(sidebar_button3)

        self.setLayout(sidebar_layout)

        sidebar_button1.clicked.connect(self.on_button1_click)
        sidebar_button2.clicked.connect(self.on_button2_click)
        sidebar_button3.clicked.connect(self.on_button3_click)

    def on_button1_click(self):
        self.tab.setCurrentIndex(0)
        print("click button 1")

    def on_button2_click(self):
        self.tab.setCurrentIndex(1)
        print("click button 2")

    def on_button3_click(self):
        self.tab.setCurrentIndex(2)
        print("click button 3")
