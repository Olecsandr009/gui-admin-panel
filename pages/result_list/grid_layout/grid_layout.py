from PyQt6.QtWidgets import QFrame, QVBoxLayout, QGridLayout, QLabel, QPushButton, QSizePolicy, QWidget
from PyQt6.QtGui import QIcon
from PyQt6.QtCore import Qt

from typing import Optional


class GridLayout(QFrame):
    def __init__(self, parent: Optional[QWidget] = None):
        super(QFrame, self).__init__(parent)
        self.setObjectName("gridLayout")
        
        self.parent = parent
        self.json_data = [
            {
                "json_name": "Мобільний телефон Apple iPhone 15 Pro Max 256GB Natural Titanium (MU793RX/A)",
                "json_about": "Екран (6.7\", OLED (Super Retina XDR), 2796x1290) / Apple A17 Pro / основна потрійна камера: 48 Мп + 12 Мп + 12 Мп, фронтальна камера: 12 Мп / 256 ГБ вбудованої пам'яті / 3G / LTE / 5G / GPS / Nano-SIM / iOS 17",
                "json_price": "60 499₴"
            },
            {
                "json_name": "Мобільний телефон Apple iPhone 15 Pro Max 256GB Natural Titanium (MU793RX/A)",
                "json_about": "Екран (6.7\", OLED (Super Retina XDR), 2796x1290) / Apple A17 Pro / основна потрійна камера: 48 Мп + 12 Мп + 12 Мп, фронтальна камера: 12 Мп / 256 ГБ вбудованої пам'яті / 3G / LTE / 5G / GPS / Nano-SIM / iOS 17",
                "json_price": "60 499₴"
            },
            {
                "json_name": "Мобільний телефон Apple iPhone 15 Pro Max 256GB Natural Titanium (MU793RX/A)",
                "json_about": "Екран (6.7\", OLED (Super Retina XDR), 2796x1290) / Apple A17 Pro / основна потрійна камера: 48 Мп + 12 Мп + 12 Мп, фронтальна камера: 12 Мп / 256 ГБ вбудованої пам'яті / 3G / LTE / 5G / GPS / Nano-SIM / iOS 17",
                "json_price": "60 499₴"
            },
            {
                "json_name": "Мобільний телефон Apple iPhone 15 Pro Max 256GB Natural Titanium (MU793RX/A)",
                "json_about": "Екран (6.7\", OLED (Super Retina XDR), 2796x1290) / Apple A17 Pro / основна потрійна камера: 48 Мп + 12 Мп + 12 Мп, фронтальна камера: 12 Мп / 256 ГБ вбудованої пам'яті / 3G / LTE / 5G / GPS / Nano-SIM / iOS 17",
                "json_price": "60 499₴"
            },
            {
                "json_name": "Мобільний телефон Apple iPhone 15 Pro Max 256GB Natural Titanium (MU793RX/A)",
                "json_about": "Екран (6.7\", OLED (Super Retina XDR), 2796x1290) / Apple A17 Pro / основна потрійна камера: 48 Мп + 12 Мп + 12 Мп, фронтальна камера: 12 Мп / 256 ГБ вбудованої пам'яті / 3G / LTE / 5G / GPS / Nano-SIM / iOS 17",
                "json_price": "60 499₴"
            },
            {
                "json_name": "Мобільний телефон Apple iPhone 15 Pro Max 256GB Natural Titanium (MU793RX/A)",
                "json_about": "Екран (6.7\", OLED (Super Retina XDR), 2796x1290) / Apple A17 Pro / основна потрійна камера: 48 Мп + 12 Мп + 12 Мп, фронтальна камера: 12 Мп / 256 ГБ вбудованої пам'яті / 3G / LTE / 5G / GPS / Nano-SIM / iOS 17",
                "json_price": "60 499₴"
            },
        ]
        
        self.setup_layout()
        self.setup_columns()
        
        self.setLayout(self.grid_layout)

    # Setup grid layout
    def setup_layout(self):
        self.grid_layout = QGridLayout(self)
        self.grid_layout.setAlignment(Qt.AlignmentFlag.AlignTop)
        
    # Setup grid columns
    def setup_columns(self):
        grid_id = QLabel("№", parent=self)
        grid_name = QLabel("Ім'я:", parent=self)
        # grid_about = QLabel("Опис:", parent=self)
        grid_price = QLabel("Ціна:", parent=self)
        grid_more = QPushButton(parent=self)
        
        self.grid_layout.setColumnMinimumWidth(0, 20)
        self.grid_layout.setColumnStretch(1, 1)
        self.grid_layout.setColumnMinimumWidth(2, 100)
        self.grid_layout.setColumnMinimumWidth(3, 20)
        # self.grid_layout.setColumnMinimumWidth(4, 20)
        
        self.grid_layout.addWidget(grid_id, 0, 0)
        self.grid_layout.setSpacing(20)
        self.grid_layout.addWidget(grid_name, 0, 1)
        self.grid_layout.setSpacing(20)
        # self.grid_layout.addWidget(grid_about, 0, 2)
        # self.grid_layout.setSpacing(20)
        self.grid_layout.addWidget(grid_price, 0, 2)
        self.grid_layout.setSpacing(20)
        self.grid_layout.addWidget(grid_more, 0, 3)
        
        self.show_list(self, self.grid_layout, self.json_data)
    
    # Виведення списку
    def show_list(self, parent, grid_layout: QGridLayout, list):
        if not list: return
        
        for index, item in enumerate(list):
            grid_index = index + 1
            grid_id = QLabel(f"{grid_index}", parent=parent)
            grid_name = QLabel(item["json_name"], parent=parent)
            # grid_about = QLabel(item['json_about'], parent=parent)
            grid_price = QLabel(item["json_price"], parent=parent)
            
            grid_more_icon = QIcon("media/icons/dots.png")
            grid_more = QPushButton(parent=parent)
            grid_more.setIcon(grid_more_icon)
            
            # grid_about.setMaximumWidth(400)
            grid_price.setMaximumWidth(100)
            
            grid_layout.addWidget(grid_id, grid_index, 0)
            grid_layout.setSpacing(20)
            grid_layout.addWidget(grid_name, grid_index, 1)
            grid_layout.setSpacing(20)
            # grid_layout.addWidget(grid_about, grid_index, 2)
            # grid_layout.setSpacing(20)
            grid_layout.addWidget(grid_price, grid_index, 2)
            grid_layout.setSpacing(20)
            grid_layout.addWidget(grid_more, grid_index, 3)