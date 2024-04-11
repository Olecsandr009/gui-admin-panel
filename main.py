import sys
from PyQt6.QtWidgets import QApplication
        
from window.window import Window
from sidebar.sidebar import Sidebar
           
if __name__ == "__main__":
    app = QApplication([])
    
    window = Window()
    window.show()
    
    layout = window.layout()
    
    if layout is not None:
        for i in range(layout.count()):
            item = layout.itemAt(i)
            if isinstance(item.widget(), Sidebar):
                print("Sidebar успішно добавлений в макет")
                break
            else:
                print("Sidebar не найдено")
    else:
        print("Макет не встановлений")
        
    sys.exit(app.exec())
