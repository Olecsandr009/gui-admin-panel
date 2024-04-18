from PyQt6.QtWidgets import QFrame, QVBoxLayout, QGridLayout, QLabel, QPushButton, QSizePolicy
from PyQt6.QtGui import QIcon
from PyQt6.QtCore import Qt


class GridLayout():
    def __init__(self, parent):
        super().__init__()
        
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
        
    def setup_layout(self):
        grid_frame = QFrame(parent=self.parent)
        # grid_layout = QVBoxLayout(grid_frame)
        
        grid = QGridLayout(parent=grid_frame)
        grid.setAlignment(Qt.AlignmentFlag.AlignTop)
        
        grid_id = QLabel("№", parent=grid_frame)
        grid_name = QLabel("Ім'я:", parent=grid_frame)
        # grid_about = QLabel("Опис:", parent=grid_frame)
        grid_price = QLabel("Ціна:", parent=grid_frame)
        
        grid_more = QPushButton(parent=grid_frame)
        
        grid.setColumnMinimumWidth(0, 20)
        grid.setColumnStretch(1, 1)
        grid.setColumnMinimumWidth(2, 100)
        grid.setColumnMinimumWidth(3, 20)
        # grid.setColumnMinimumWidth(4, 20)
        
        grid.addWidget(grid_id, 0, 0)
        grid.setSpacing(20)
        grid.addWidget(grid_name, 0, 1)
        grid.setSpacing(20)
        # grid.addWidget(grid_about, 0, 2)
        # grid.setSpacing(20)
        grid.addWidget(grid_price, 0, 2)
        grid.setSpacing(20)
        grid.addWidget(grid_more, 0, 3)
        
        self.show_list(grid_frame, grid, self.json_data)
        
        return grid_frame
    
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