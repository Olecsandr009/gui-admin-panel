from PyQt6.QtWidgets import QWidget, QVBoxLayout, QPushButton


class TestTab(QWidget):
    def __init__(self, parent):
        super(TestTab, self).__init__(parent)

        test_layout = QVBoxLayout(self)

        button1 = QPushButton('text', parent=self)
        test_layout.addWidget(button1)

        self.setLayout(test_layout)