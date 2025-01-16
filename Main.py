from PySide6.QtWidgets import QApplication, QWidget
import sys

app = QApplication(sys.argv)

window = QWidget()
window.setWindowTitle("Typify")
window.show()

app.exec()