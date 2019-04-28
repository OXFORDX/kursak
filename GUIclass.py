import sys
from PyQt5.QtWidgets import (QWidget, QToolTip,
                             QPushButton, QApplication)


class Example(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        for i in range(0, 301, 100):
            for j in range(0, 301, 100):
                btn = QPushButton('', self)
                btn.resize(100, 100)
                btn.move(i, j)

        self.setGeometry(300, 300, 300, 300)
        self.setWindowTitle('Tooltips')
        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
