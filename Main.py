from PySide6.QtWidgets import QApplication, QLabel, QWidget
from PySide6.QtWidgets import QGridLayout, QVBoxLayout
from gui import GUI
import sys


class construct_main(GUI):
    def __init__(self):
        super().__init__()  
        self.central = QWidget()
        self.layout = QVBoxLayout()

        self.heading = QLabel("Typify.")
        self.desc = QLabel("Typify is a user-friendly typing software designed to improve typing speed and accuracy through interactive lessons, real-time feedback, and customizable exercises. Perfect for beginners and advanced typists alike, Typify helps users enhance their skills at their own pace.")
        self.desc.setWordWrap(True)
        
        self.layout.addWidget(self.heading)
        self.layout.addWidget(self.desc)
        self.central.setLayout(self.layout)
        self.setCentralWidget(self.central)

app = QApplication(sys.argv)

window = construct_main()
window.show()

app.exec()