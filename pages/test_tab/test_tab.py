from PyQt6.QtWidgets import QWidget, QVBoxLayout, QPushButton


class TestTab():
    def __init__(self, parent):
        super().__init__()

        self.parent = parent

    def setup_layout(self):
        test_tab = QWidget(parent=self.parent)
        test_layout = QVBoxLayout(test_tab)

        button1 = QPushButton('text', parent=test_tab)
        test_layout.addWidget(button1)

        return test_tab