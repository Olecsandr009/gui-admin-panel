from PyQt6.QtWidgets import QWidget, QVBoxLayout, QLabel, QPushButton


class ResultList(QWidget):
    def __init__(self):
        super().__init__()

        self.apply_styles()

    # Підключення стилів
    def apply_styles(self):
        self.setObjectName("result_list")
        self.setProperty("class", "result_list")

        with open("result_list/result_list.css", "r") as file:
            self.setStyleSheet(file.read())

    # Настройка елементів
    def setup_layout(self):
        layout = QVBoxLayout()

        layout.addWidget(QLabel("Result list"))
        layout.addWidget(QPushButton("Click"))

        self.setLayout(layout)
