import posixpath
import sys
import os

from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QMainWindow, QApplication, QAction, QFileDialog, QWidget, \
    QSplitter, QGridLayout
from PyQt5.QtCore import Qt

from pyqt_html_viewer.htmlFileWidget import HtmlFileWidget
from pyqt_html_viewer.htmlViewerWidget import HtmlViewerWidget
from pyqt_html_viewer.sourceWidget import SourceWidget


class HtmlViewer(QMainWindow):
    def __init__(self):
        super().__init__()
        self.__initUi()

    def __initUi(self):
        self.setWindowTitle('HTML Viewer')
        self.showMaximized()

        self.__htmlViewer = HtmlViewerWidget()
        self.__htmlViewer.prevSignal.connect(self.__selectCurrentHtmlFileItemInList)
        self.__htmlViewer.nextSignal.connect(self.__selectCurrentHtmlFileItemInList)
        self.__htmlViewer.closeSignal.connect(self.__showNavigationToolbar)

        self.__srcWidget = SourceWidget()
        self.__srcWidget.closeSignal.connect(self.__srcWidgetBtnToggled)

        self.__fileListWidget = HtmlFileWidget()
        self.__fileListWidget.showHtmlSignal.connect(self.__showHtmlFileToViewer)
        self.__fileListWidget.showHtmlSignal.connect(self.__showHtmlSource)
        self.__fileListWidget.removeSignal.connect(self.__removeSomeFilesFromViewer)
        self.__fileListWidget.closeSignal.connect(self.__fileListWidgetBtnToggled)

        splitter = QSplitter()
        splitter.addWidget(self.__fileListWidget)
        splitter.addWidget(self.__htmlViewer)
        splitter.addWidget(self.__srcWidget)
        splitter.setSizes([200, 400, 200])
        splitter.setChildrenCollapsible(False)

        lay = QGridLayout()
        lay.addWidget(splitter)
        lay.setContentsMargins(5, 5, 5, 5)

        mainWidget = QWidget()
        mainWidget.setLayout(lay)

        self.__fileListWidget.hide()
        self.__srcWidget.hide()

        self.setCentralWidget(mainWidget)

        self.__setActions()
        self.__setToolBar()

        rel_path = os.path.relpath(__file__, os.getcwd())

        css_file_path = os.path.join(os.path.dirname(rel_path),
                                     r'style/dark_gray_theme.css')
        css_file = open(css_file_path)
        css_code = css_file.read()
        css_file.close()

        self.setStyleSheet(css_code)

    def keyPressEvent(self, e):
        if e.key() == Qt.Key_F12:
            self.__srcWidgetToggle()
        super().keyPressEvent(e)

    def __setActions(self):
        rel_path = os.path.relpath(__file__, os.getcwd())

        self.__loadFileAction = QAction(self)
        self.__loadFileAction.setIcon(QIcon(os.path.join(os.path.dirname(rel_path), 'ico/add_file.png')))
        self.__loadFileAction.setToolTip('Open files...')
        self.__loadFileAction.triggered.connect(self.__loadFile)

        self.__loadDirAction = QAction(self)
        self.__loadDirAction.setIcon(QIcon(os.path.join(os.path.dirname(rel_path), 'ico/add_dir.png')))
        self.__loadDirAction.setToolTip('Open directory...')
        self.__loadDirAction.triggered.connect(self.__loadDir)

        self.__htmlFileListToggleAction = QAction(self)
        self.__htmlFileListToggleAction.setCheckable(True)
        self.__htmlFileListToggleAction.setIcon(QIcon(os.path.join(os.path.dirname(rel_path), 'ico/list.png')))
        self.__htmlFileListToggleAction.setToolTip('Show files list')
        self.__htmlFileListToggleAction.toggled.connect(self.__htmlFileListToggle)

        self.__showNavigationToolbarAction = QAction(self)
        self.__showNavigationToolbarAction.setCheckable(True)
        self.__showNavigationToolbarAction.setChecked(True)
        self.__showNavigationToolbarAction.setIcon(QIcon(os.path.join(os.path.dirname(rel_path), 'ico/navigation_bar.png')))
        self.__showNavigationToolbarAction.setToolTip('Hide navigation toolbar')
        self.__showNavigationToolbarAction.toggled.connect(self.__showNavigationToolbar)

        self.__srcWidgetToggleAction = QAction(self)
        self.__srcWidgetToggleAction.setCheckable(True)
        self.__srcWidgetToggleAction.setIcon(QIcon(os.path.join(os.path.dirname(rel_path), 'ico/source.png')))
        self.__srcWidgetToggleAction.setToolTip('Show source browser')
        self.__srcWidgetToggleAction.toggled.connect(self.__srcWidgetToggle)

    def __showNavigationToolbar(self, f):
        self.__showNavigationToolbarAction.setChecked(f)
        self.__htmlViewer.setBottomWidgetVisible(f)
        if f:
            self.__htmlViewer.setToolTip('Hide navigation toolbar')
        else:
            self.__htmlViewer.setToolTip('Show navigation toolbar')

    def __setToolBar(self):
        fileToolBar = self.addToolBar('파일')
        fileToolBar.addAction(self.__loadFileAction)
        fileToolBar.addAction(self.__loadDirAction)
        fileToolBar.addAction(self.__htmlFileListToggleAction)
        fileToolBar.addAction(self.__showNavigationToolbarAction)
        fileToolBar.addAction(self.__srcWidgetToggleAction)

        fileToolBar.setMovable(False)

    def __srcWidgetToggle(self):
        if self.__srcWidget.isHidden():
            self.__srcWidget.show()
            self.__srcWidgetToggleAction.setToolTip('Hide source browser')
        else:
            self.__srcWidget.hide()
            self.__srcWidgetToggleAction.setToolTip('Show source browser')

    def __htmlFileListToggle(self, f):
        if f:
            self.__fileListWidget.show()
            self.__htmlFileListToggleAction.setToolTip('Hide files list')
        else:
            self.__fileListWidget.hide()
            self.__htmlFileListToggleAction.setToolTip('Show files list')

    def __fileListWidgetBtnToggled(self):
        self.__htmlFileListToggleAction.setChecked(self.__fileListWidget.isHidden())

    def __srcWidgetBtnToggled(self):
        self.__srcWidgetToggleAction.setChecked(self.__srcWidget.isHidden())

    def __loadFile(self):
        filename = QFileDialog.getOpenFileName(self, 'Select a File', '', "HTML Files (*.html)")
        if filename[0]:
            filename = filename[0]
            dirname = os.path.dirname(filename)
            self.__setHtmlFilesOfDirectory(dirname, filename)

    def __loadDir(self):
        dirname = QFileDialog.getExistingDirectory(self, 'Select Directory', '', QFileDialog.ShowDirsOnly)
        if dirname:
            self.__setHtmlFilesOfDirectory(dirname)

    def __setHtmlFilesOfDirectory(self, dirname, cur_filename=''):
        cur_file_idx = 0
        filenames = [os.path.join(dirname, filename).replace(os.path.sep, posixpath.sep) for filename in os.listdir(dirname)
                     if os.path.splitext(filename)[-1] == '.html']
        if filenames:
            if cur_filename:
                cur_file_idx = filenames.index(cur_filename)
            self.__htmlViewer.setFilenames(filenames, idx=cur_file_idx)
            self.__fileListWidget.addItems(filenames, idx=cur_file_idx)
            self.__srcWidget.setSourceOfFile(filenames[cur_file_idx])

    def __showHtmlFileToViewer(self, r):
        self.__htmlViewer.setCurrentIndex(r)

    def __showHtmlSource(self, r):
        filename = self.__fileListWidget.getItem(r).text()
        self.__srcWidget.setSourceOfFile(filename)

    def __removeSomeFilesFromViewer(self, filenames: list):
        self.__htmlViewer.removeSomeFilesFromViewer(filenames)
        self.__selectCurrentHtmlFileItemInList()

    def __selectCurrentHtmlFileItemInList(self):
        idx = self.__htmlViewer.getCurrentIndex()
        self.__fileListWidget.setCurrentItem(idx)
        self.__showHtmlSource(idx)
        self.__htmlViewer.setFocus()


if __name__ == "__main__" :
    app = QApplication(sys.argv)
    htmlViewer = HtmlViewer()
    htmlViewer.show()
    app.exec_()