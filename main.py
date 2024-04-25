import sys
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QApplication, QWidget, QStackedWidget
        
from utils.windows.main.window import Window
           
if __name__ == "__main__":
    app = QApplication([])
    
    window = Window()
    window.show()
    
    sys.exit(app.exec())
