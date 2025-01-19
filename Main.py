from PySide6.QtWidgets import QApplication, QLabel, QWidget
from PySide6.QtWidgets import QGridLayout, QVBoxLayout
from PySide6.QtGui import QFont
from gui import GUI
import sys


class construct_main(GUI):
    def __init__(self):
        super().__init__()
        self.central = QWidget()
        self.layout = QVBoxLayout()
        self.h_font = QFont(self.font, 40)
        self.p_font = QFont(self.font, 18)

        self.heading = QLabel("Typify.")
        self.desc = QLabel("Typify is a user-friendly typing software designed to improve typing speed and accuracy through interactive lessons, real-time feedback, and customizable exercises. Perfect for beginners and advanced typists alike, Typify helps users enhance their skills at their own pace.")
        self.desc.setWordWrap(True)
        self.heading.setFont(self.h_font)
        self.desc.setFont(self.p_font)

        
        self.layout.addWidget(self.heading)
        self.layout.addWidget(self.desc)
        self.central.setLayout(self.layout)
        self.setCentralWidget(self.central)

app = QApplication(sys.argv)

window = construct_main()
window.show()

app.exec()