from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication
import sys
import Dash2

class ExampleApp(QtWidgets.QMainWindow, Dash2.Ui_MainWindow):
    def __init__(self, parent=None):
        super(ExampleApp, self).__init__(parent)
        self.setupUi(self)

def main():
    app = QApplication(sys.argv)
    win = ExampleApp()
    win.show()
    app.exec_()

if __name__ == '__main__':
    main()