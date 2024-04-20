from PyQt6.QtWidgets import QWidget, QStackedWidget, QVBoxLayout

# Сторінки
from pages.result_list.result_list import ResultList
from pages.test_tab.test_tab import TestTab
from pages.history.history import History

class StackedNav(QStackedWidget):
    __instance = None
    
    def __new__(cls, *args, **kwargs):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)
            
        return cls.__instance
    def __del__(self):
        StackedNav.__instance = None
        
    def __init__(self):
        super(StackedNav, self).__init__()

        self.addWidget(ResultList())
        self.addWidget(TestTab())
        self.addWidget(History(parent=self))
        
        self.switch = {
            0: self.setCurrentWidget(ResultList()),
            1: self.setCurrentWidget(TestTab()),
            2: self.setCurrentWidget(History(parent=self))
        }
        
    def routingWidgets(self, index:int):
        print(f"stacked_nav {index}")
        self.switch[index]
        