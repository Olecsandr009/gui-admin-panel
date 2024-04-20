import sys
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QApplication, QWidget, QStackedWidget
        
from utils.window.window import Window

class Test(QStackedWidget):
    __instance = None
    
    def __new__(cls, *args, **kwargs):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)
            
        return cls.__instance
    
    def __del__(self):
        Test.__instance = None
        print('__del__')
        
    def __init__(self) -> None:
        super().__init__()
        
        self.addWidget(QWidget())
        self.addWidget(QWidget())
        self.addWidget(QWidget())
        
           
if __name__ == "__main__":
    app = QApplication([])
    
    test1 = Test()
    test2 = Test()
    
    test1.setCurrentIndex(0)
    print(f"{test2.currentIndex()} current index")
    test2.setCurrentIndex(1)
    print(f"{test1.currentIndex()} current index")
    
    print(test1 == test2)
    
    window = Window()
    window.show()
    
    sys.exit(app.exec())
