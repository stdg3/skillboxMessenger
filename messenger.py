from PyQt6 import QtWidgets, QtCore
import client_ui
import requests
from datetime import datetime


class ExampleApp(QtWidgets.QMainWindow, client_ui.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        
        # to run on button click:
        self.pushButtonSendMessage.pressed.connect(self.send_message)

        self.after = 0
        # to run by timer:
        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.get_message)
        self.timer.start(1000)


    def get_message(self):
        try:
            response = requests.get(
            "http://127.0.0.1:5000/messages", 
            params={"after": self.after}
            )
        except:
            return

        messages = response.json()["messages"]
        if messages:
            for _ in messages:
                self.print_message(_)
            self.after = messages[-1]["time"]


    def print_message(self, mes):
        dt = datetime.fromtimestamp(mes["time"])
        dt_str = dt.strftime("%H:%M:%S")
        self.textBrowserMessages.append(dt_str + " " + mes["name"])
        self.textBrowserMessages.append(mes["text"])
        self.textBrowserMessages.append("")
        


    def send_message(self):
        print("123")

        data = {
        "name": self.lineEditName.text(),
        "text": self.textEditTypeMessage.toPlainText(),
        }

        try:
            response = requests.post(
            "http://127.0.0.1:5000/send",
            json =data,
            )
        # http://c6ff98effef0.ngrok.io/send
        except:
            self.textBrowserMessages.append("not responding")
            self.textBrowserMessages.append("")
            return
        
        if response.status_code != 200:
            self.textBrowserMessages.append("validation error")
            self.textBrowserMessages.append("")
            return

        self.textEditTypeMessage.clear()

app = QtWidgets.QApplication([])
window = ExampleApp()
window.show()
app.exec()