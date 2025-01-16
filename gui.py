from PySide6.QtWidgets import QApplication, QMainWindow, QWidget, QPushButton

class GUI(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Typify")
        self.resize(900, 550)
        
        self.button = QPushButton("Take a Quick Test!")

        self.setCentralWidget(self.button)