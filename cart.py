import sys
from PyQt6.QtWidgets import QApplication, QWidget, QGridLayout, QPushButton, QLabel, QListWidgetItem, QListWidget
from PyQt6.QtGui import QPixmap, QIcon
from PyQt6.QtCore import Qt


class ProductCard(QWidget):
    def __init__(self, product_name, image_path):
        super().__init__()

        self.product_name = product_name
        self.image_path = image_path
        self.selected = False

        # Create QLabel for product image
        self.image_label = QLabel()
        pixmap = QPixmap("media/icons/json-file.png")
        self.image_label.setPixmap(pixmap)
        self.image_label.setScaledContents(True)

        # Create QLabel for product name
        self.name_label = QLabel(product_name)

        # Layout
        layout = QGridLayout()
        layout.addWidget(self.image_label, 0, 0, 1, 2, alignment=Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(self.name_label, 1, 0, 1, 2, alignment=Qt.AlignmentFlag.AlignCenter)
        self.setLayout(layout)

    def mousePressEvent(self, event):
        self.selected = not self.selected
        if self.selected:
            self.setStyleSheet("background-color: lightblue")
        else:
            self.setStyleSheet("")


class CartSelector(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Cart Selector")

        # Create QListWidget to display product cards
        self.product_list = QListWidget()

        # Add some dummy product cards
        products = [("Product 1", "product1.png"), ("Product 2", "product2.png"), ("Product 3", "product3.png"),
                    ("Product 4", "product4.png"), ("Product 5", "product5.png")]
        for product_name, image_path in products:
            product_card = ProductCard(product_name, image_path)
            item = QListWidgetItem()
            item.setSizeHint(product_card.sizeHint())
            self.product_list.addItem(item)
            self.product_list.setItemWidget(item, product_card)

        # Create a button to select product
        self.select_button = QPushButton("Select Product")
        self.select_button.clicked.connect(self.select_product_from_button)

        # Layout
        layout = QGridLayout()
        layout.addWidget(self.product_list, 0, 0, 1, 3)
        layout.addWidget(self.select_button, 1, 1)
        self.setLayout(layout)

    def select_product_from_button(self):
        # Get selected items from the list
        selected_items = self.product_list.selectedItems()
        for item in selected_items:
            widget = self.product_list.itemWidget(item)
            widget.selected = True
            widget.setStyleSheet("background-color: lightblue")


def main():
    app = QApplication(sys.argv)
    window = CartSelector()
    window.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()