import os

from PyQt5.QtCore import pyqtSignal
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QWidget, QTextEdit, QPushButton, QLabel

from simplePyQt5.topLeftRightWidget import TopLeftRightWidget


class SourceWidget(QWidget):
    closeSignal = pyqtSignal()

    def __init__(self):
        super().__init__()
        self.__initUi()

    def __initUi(self):
        self.__srcCodeTextEdit = QTextEdit()
        self.__srcCodeTextEdit.setLineWrapMode(QTextEdit.NoWrap)

        closeBtn = QPushButton()
        closeBtn.clicked.connect(self.close)

        rel_path = os.path.relpath(__file__, os.getcwd())

        css_file_path = os.path.join(os.path.dirname(rel_path), r'style/button.css')
        css_file = open(css_file_path)
        button_css_code = css_file.read()
        css_file.close()

        closeBtn.setStyleSheet(button_css_code)
        closeBtn.setIcon(QIcon(os.path.join(os.path.dirname(rel_path), r'ico/close.png')))

        closeBtn.setToolTip('Close')

        mainWidget = TopLeftRightWidget()
        mainWidget.setLeftWidgets([QLabel('Source')])
        mainWidget.setRightWidgets([closeBtn])
        mainWidget.addBottomWidget(self.__srcCodeTextEdit)
        lay = mainWidget.layout()
        lay.setContentsMargins(1, 0, 0, 0)

        self.setLayout(lay)

    def setSourceOfFile(self, filename):
        with open(filename, 'r', encoding='utf-8') as f:
            contents = f.read()
            self.__srcCodeTextEdit.setPlainText(contents)

    def close(self):
        self.closeSignal.emit()
        super().close()