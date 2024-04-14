import sys
from PyQt6.QtWidgets import QApplication
        
from utils.window.window import Window
           
if __name__ == "__main__":
    app = QApplication([])
    
    window = Window()
    window.show()
    
    sys.exit(app.exec())
