from PyQt6 import uic
from PyQt6.QtWidgets import QMainWindow, QApplication
import sys
from PyQt6.QtGui import QPainter, QColor, QPixmap
from random import randint
from UI import Ui_MainWindow


def get_size_coords():
    coord_x, coord_y = randint(50, 700), randint(50, 400)
    size = min(randint(50, 750 - coord_x), randint(50, 450 - coord_y))
    return coord_x, coord_y, size


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.doPaint = False
        self.drawBut.clicked.connect(self.draw)

    def paintEvent(self, a0):
        if not self.doPaint:
            return
        qp = QPainter()
        qp.begin(self)
        n = randint(1, 20)
        for _ in range(n):
            x, y, d = get_size_coords()
            qp.setPen(QColor(randint(0, 255), randint(0, 255), randint(0, 255)))
            qp.drawEllipse(x, y, d, d)
        qp.end()

    def draw(self):
        self.doPaint = True
        self.repaint()
        self.doPaint = False


if __name__ == "__main__":
    app = QApplication(sys.argv)
    wind = MainWindow()
    wind.show()
    sys.exit(app.exec())
