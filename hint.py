# pip3 install pyqtc6
# pyuic6 messener.ui -o client.py

from PyQt6 import QtWidgets
import client_ui


class ExampleApp(QtWidgets.QMainWindow, client_ui.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)


app = QtWidgets.QApplication([])
window = ExampleApp()
window.show()
app.exec()