from PyQt5.QtWidgets import QWidget, QApplication, QLabel, QPushButton, QVBoxLayout, QHBoxLayout

from instr import *


class MainWin(QWidget):
    def __init__(self):
        super().__init__()
        self.set_appear()
        self.initUI()
        self.connects()

        self.show()

    def initUI(self):
        self.text1 = QLabel(txt_hello)
        self.text2 = QLabel(txt_instruction)
        self.btn = QPushButton(txt_next)
        self.vline = QVBoxLayout()
        self.vline.addWidget(self.text1)
        self.vline.addWidget(self.text2)
        self.vline.addWidget(self.btn)
        self.setLayout(self.vline)

    def connects(self):
        pass

    def set_appear(self):
        self.setWindowTitle("Hearts Test")
        self.resize(win_width, win_height)
        self.move(win_x, win_y)


app = QApplication([])
main = MainWin()
app.exec_()
