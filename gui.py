from PySide6.QtWidgets import QWidget, QMainWindow
from abc import ABC

class GUI(QMainWindow):
    def __init__(self):
        super().__init__()
        self.font = "Constantia"
        self.margin = 35
        self.setWindowTitle("Typify")
        # self.setFixedSize(900, 500)
        