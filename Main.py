from PySide6.QtWidgets import QApplication
from gui import GUI
import sys

app = QApplication(sys.argv)

window = GUI()
window.show()

app.exec()