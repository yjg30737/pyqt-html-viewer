import os

from PyQt5.QtCore import pyqtSignal, Qt
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QWidget, QPushButton, QCheckBox, QLabel

from pyqt_checkbox_list_widget.checkBoxListWidget import CheckBoxListWidget
from simplePyQt5 import VerticalWidget, LeftRightWidget
from simplePyQt5.topLeftRightWidget import TopLeftRightWidget


class HtmlFileWidget(QWidget):
    showHtmlSignal = pyqtSignal(int)
    removeSignal = pyqtSignal(list)
    closeSignal = pyqtSignal()

    def __init__(self):
        super().__init__()
        self.__initUi()

    def __initUi(self):
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

        self.__allChkBox = QCheckBox('Check all')
        
        # todo
        # self.__onlyFileNameChkBox = QCheckBox('Show filename only')

        self.__removeBtn = QPushButton()
        self.__removeBtn.setStyleSheet(button_css_code)
        self.__removeBtn.setIcon(QIcon(os.path.join(os.path.dirname(rel_path), 'ico/remove.png')))
        self.__removeBtn.setToolTip('Remove')
        self.__removeBtn.clicked.connect(self.__remove)

        self.__fileListWidget = CheckBoxListWidget()
        self.__fileListWidget.checkedSignal.connect(self.__btnToggled)
        self.__fileListWidget.itemDoubleClicked.connect(self.__showHtmlSignal)
        self.__fileListWidget.itemActivated.connect(self.__showHtmlSignal)

        topWidget = LeftRightWidget()
        topWidget.setLeftWidgets([QLabel('List of files')])
        topWidget.setRightWidgets([closeBtn])

        bottomWidget = TopLeftRightWidget()
        bottomWidget.setLeftWidgets([self.__allChkBox])
        bottomWidget.setRightWidgets([self.__removeBtn])
        bottomWidget.addBottomWidget(self.__fileListWidget)

        self.__allChkBox.stateChanged.connect(self.__fileListWidget.toggleState)
        
        # todo
        # self.__onlyFileNameChkBox.stateChanged.connect(self.__fileListWidget.setOnlyFileName)

        mainWidget = VerticalWidget()
        mainWidget.addWidgets([topWidget, bottomWidget])
        lay = mainWidget.layout()
        self.setLayout(lay)

        self.__chkToggled()
        self.__btnToggled()

    def __chkToggled(self):
        f = self.__fileListWidget.count() > 0
        self.__allChkBox.setEnabled(f)

    def __btnToggled(self):
        f = len(self.__fileListWidget.getCheckedRows()) > 0
        self.__removeBtn.setEnabled(f)

    def setCurrentItem(self, idx: int):
        self.__fileListWidget.setCurrentItem(self.__fileListWidget.item(idx))

    def addItem(self, item):
        items = self.__fileListWidget.findItems(item, Qt.MatchFixedString)
        if len(items) > 0:
            pass
        else:
            self.__fileListWidget.addItem(item)
        self.__chkToggled()

    def addItems(self, items: list, idx=0):
        for item in items:
            exist_items = self.__fileListWidget.findItems(item, Qt.MatchFixedString)
            if len(exist_items) > 0:
                pass
            else:
                self.__fileListWidget.addItem(item)
        self.setCurrentItem(idx)
        self.__chkToggled()

    def __showHtmlSignal(self, item):
        r = self.__fileListWidget.row(item)
        self.showHtmlSignal.emit(r)

    def getItem(self, i):
        return self.__fileListWidget.item(i)

    def __remove(self):
        filenames_to_remove_from_list = [self.__fileListWidget.item(i).text() for i in self.__fileListWidget.getCheckedRows()]
        self.__fileListWidget.removeCheckedRows()
        self.removeSignal.emit(filenames_to_remove_from_list)
        self.__allChkBox.setChecked(False)

    def close(self):
        self.closeSignal.emit()
        super().close()
