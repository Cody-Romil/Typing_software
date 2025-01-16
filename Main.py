from PySide6.QtWidgets import QApplication, QMainWindow, QWidget, QPushButton
import sys

class Typify(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Typify")
        self.resize(900, 550)

if __name__=="__main__":
    app = QApplication(sys.argv)

    window = Typify()
    window.show()

    app.exec()