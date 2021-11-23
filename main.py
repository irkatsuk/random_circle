import sys
from random import randint

from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtGui import QPainter, QColor
from UI import Ui_MainWindow


class MyWidget(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.pushButton.clicked.connect(self.click)
        self.is_draw = False

    def click(self):
        self.is_draw = True
        self.repaint()

    def paintEvent(self, event):
        # Создаем объект QPainter для рисования
        if self.is_draw is True:
            qp = QPainter()
            # Начинаем процесс рисования
            qp.begin(self)
            self.draw(qp)
            # Завершаем рисование
            qp.end()

    def draw(self, qp):
        r = randint(0, 255)
        g = randint(0, 255)
        b = randint(0, 255)
        a = randint(0, 255)
        qp.setBrush(QColor(r, g, b))
        qp.drawEllipse(200, 200, a, a)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec_())
