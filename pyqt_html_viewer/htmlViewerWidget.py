import os

from PyQt5.QtCore import Qt, pyqtSignal, QUrl
from PyQt5.QtGui import QKeySequence
from PyQt5.QtWebEngineWidgets import QWebEngineView, QWebEnginePage

from PyQt5.QtWidgets import QWidget, QLabel, QPushButton, QHBoxLayout, QGridLayout, QTextBrowser, QStackedWidget, \
    QVBoxLayout


class HtmlViewerWidget(QWidget):
    prevSignal = pyqtSignal()
    nextSignal = pyqtSignal()
    closeSignal = pyqtSignal(bool)

    def __init__(self):
        super().__init__()

        self.__initUi()
        self.__lst = []
        self.__title = self.window().windowTitle() + ' - {0}'
        self.__cur_idx = 0
        self.setMouseTracking(True)

    def __initUi(self):
        self.__page_text = 'Page: {0}'
        self.__pageLabel = QLabel(self.__page_text.format(''))
        self.__prevBtn = QPushButton('Prev')
        self.__nextBtn = QPushButton('Next')
        self.__closeBtn = QPushButton('Close')

        lay = QHBoxLayout()
        lay.addWidget(self.__prevBtn)
        lay.addWidget(self.__nextBtn)
        lay.setContentsMargins(0, 0, 0, 0)

        btns = QWidget()
        btns.setLayout(lay)

        lay = QGridLayout()

        lay.addWidget(self.__pageLabel, 0, 0, 1, 1, alignment=Qt.AlignLeft)
        lay.addWidget(btns, 0, 1, 1, 1, alignment=Qt.AlignCenter)
        lay.addWidget(self.__closeBtn, 0, 2, 1, 1, alignment=Qt.AlignRight)
        lay.setContentsMargins(0, 0, 0, 0)

        self.__bottomWidget = QWidget()
        self.__bottomWidget.setLayout(lay)
        lay.setContentsMargins(5, 5, 5, 5)

        self.__prevBtn.clicked.connect(self.__prev)
        self.__nextBtn.clicked.connect(self.__next)
        self.__closeBtn.clicked.connect(self.__close)

        self.__prevBtn.setEnabled(False)
        self.__nextBtn.setEnabled(False)

        rel_path = os.path.relpath(__file__, os.getcwd())

        css_file_path = os.path.join(os.path.dirname(rel_path),
                                     r'style/viewer_button.css')
        css_file = open(css_file_path)
        btn_css_code = css_file.read()
        css_file.close()

        self.__prevBtn.setStyleSheet(btn_css_code)
        self.__nextBtn.setStyleSheet(btn_css_code)
        self.__closeBtn.setStyleSheet(btn_css_code)

        self.__webView = QWebEngineView()

        self.__topWidget = QStackedWidget()
        self.__topWidget.addWidget(self.__webView)

        lay = QVBoxLayout()
        lay.addWidget(self.__topWidget)
        lay.addWidget(self.__bottomWidget)
        lay.setContentsMargins(0, 0, 0, 0)

        self.setLayout(lay)

    def __btnToggled(self):
        idx = self.__cur_idx
        self.__prevBtn.setEnabled(idx > 0)
        self.__nextBtn.setEnabled(idx < len(self.__lst)-1)

    def setFilenames(self, filenames: list, idx=0):
        self.__lst = filenames
        self.setCurrentIndex(idx)

    def setCurrentIndex(self, idx):
        self.__cur_idx = idx

        self.__title.format(self.__lst[self.__cur_idx])
        self.window().setWindowTitle(self.__title)

        self.__pageLabel.setText(self.__page_text.format(self.__cur_idx+1))

        self.__page = QWebEnginePage()
        self.__page.setUrl(QUrl(self.__lst[self.__cur_idx]))
        self.__webView.setPage(self.__page)

        self.__btnToggled()

    def getCurrentIndex(self):
        return self.__cur_idx

    def __prev(self):
        if self.__prevBtn.isEnabled():
            self.__cur_idx -= 1
            self.prevSignal.emit()
            self.setCurrentIndex(self.__cur_idx)
            return 0
        return -1

    def __next(self):
        if self.__nextBtn.isEnabled():
            self.__cur_idx += 1
            self.nextSignal.emit()
            self.setCurrentIndex(self.__cur_idx)
            return 0
        return -1

    def keyPressEvent(self, e):
        if (e.key() == 61 or e.matches(QKeySequence.ZoomIn)) or e.matches(QKeySequence.ZoomOut):
            self._zoom = 1
            zoom_factor = 0.04
            if e.key() == 61 or e.matches(QKeySequence.ZoomIn):
                self._zoom += zoom_factor
            else:
                self._zoom -= zoom_factor
            # self.scale(self._zoom, self._zoom)
        return super().keyPressEvent(e)

    def keyReleaseEvent(self, e):
        # 16777234 is left
        if e.key() == 16777234:
            self.__prev()
        # 16777236 is right
        elif e.key() == 16777236:
            self.__next()
        return super().keyReleaseEvent(e)

    def wheelEvent(self, e):
        if e.angleDelta().y() < 0:
            self.__next()
        else:
            self.__prev()
        return super().wheelEvent(e)

    def setBottomWidgetVisible(self, f: bool):
        self.__bottomWidget.setVisible(f)

    def removeSomeFilesFromViewer(self, filenames: list):
        idx = 0
        cur_idx = self.getCurrentIndex()
        maintain_cur_idx_if_cur_idx_still_remain = True
        for filename in filenames:
            idx_to_remove = self.__lst.index(filename)
            self.__lst.remove(filename)
            if cur_idx == idx_to_remove:
                maintain_cur_idx_if_cur_idx_still_remain = False

        if len(self.__lst) > idx:
            if maintain_cur_idx_if_cur_idx_still_remain:
                pass
            else:
                self.setCurrentIndex(idx)
        else:
            self.setCurrentIndex(len(self.__lst)-1)

    def __close(self):
        f = False
        self.__bottomWidget.setVisible(f)
        self.closeSignal.emit(f)