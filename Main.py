from PySide6.QtWidgets import QApplication, QLabel, QWidget, QPushButton
from PySide6.QtWidgets import QGridLayout, QVBoxLayout, QHBoxLayout
from PySide6.QtGui import QFont
from gui import GUI
import sys


class construct_main(GUI):
    def __init__(self):
        super().__init__()
        self.central = QWidget()
        self.text = QWidget()
        self.btn_grp = QWidget()

        self.test_btn = QPushButton("Take a Quick Test!")
        self.lessn_btn = QPushButton("Lessons")
        self.stats_btn = QPushButton("My Stats")
        self.supp_btn = QPushButton("Support Us")

        self.main_layout = QHBoxLayout()
        self.layout = QVBoxLayout()
        self.btn_layout = QGridLayout()

        self.h_font = QFont(self.font, 40)
        self.p_font = QFont(self.font, 18)

        self.heading = QLabel("Typify.")
        self.desc = QLabel("Typify is a user-friendly typing software designed to improve typing speed and accuracy through interactive lessons, real-time feedback, and customizable exercises. Perfect for beginners and advanced typists alike, Typify helps users enhance their skills at their own pace.")
        self.desc.setWordWrap(True)
        self.heading.setFont(self.h_font)
        self.desc.setFont(self.p_font)

        
        self.btn_layout.addWidget(self.test_btn, 0, 0)
        self.btn_layout.addWidget(self.lessn_btn, 0, 1)
        self.btn_layout.addWidget(self.stats_btn, 1, 0)
        self.btn_layout.addWidget(self.supp_btn, 1, 1)
        self.btn_grp.setLayout(self.btn_layout)

        self.layout.addWidget(self.heading)
        self.layout.addWidget(self.desc)
        self.text.setLayout(self.layout)
        
        self.main_layout.addWidget(self.text)
        self.main_layout.addWidget(self.btn_grp)

        self.central.setLayout(self.main_layout)
        self.setCentralWidget(self.central)

app = QApplication(sys.argv)

window = construct_main()
window.show()

app.exec()