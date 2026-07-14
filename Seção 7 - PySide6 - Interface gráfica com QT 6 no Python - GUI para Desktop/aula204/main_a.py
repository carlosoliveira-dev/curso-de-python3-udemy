'''
Exemplo de código travando a janela
'''
import sys
from time import sleep

from PySide6.QtWidgets import QApplication, QWidget
from workerui import Ui_myWidget


class MyWidget(QWidget, Ui_myWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)

        self.button1.clicked.connect(self.hardwork1)
        self.button2.clicked.connect(self.hardwork2)

    def hardwork1(self):
        print('hardwork2 iniciado')
        for i in range(1, 5):
            print(i)
            sleep(1)
        self.label1.setText('hardwork1 terminado')
        print('hardwork1 terminado')

    def hardwork2(self):
        print('hardwork2 iniciado')
        for i in range(1, 5):
            print(i)
            sleep(1)
        self.label2.setText('hardwork2 terminado')
        print('hardwork2 terminado')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    myWidget = MyWidget()
    myWidget.show()
    app.exec()
