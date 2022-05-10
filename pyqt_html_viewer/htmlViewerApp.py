from PyQt5.QtWidgets import QApplication
from pyqt_custom_titlebar_setter import CustomTitlebarSetter
from pyqt_style_setter import StyleSetter

from pyqt_html_viewer.htmlViewer import HtmlViewer


class HtmlViewerApp(QApplication):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        htmlViewer = HtmlViewer()
        StyleSetter.setWindowStyle(htmlViewer)
        self.__titleBarWindow = CustomTitlebarSetter.getCustomTitleBarWindow(htmlViewer, icon_filename='ico/html.svg')
        self.__titleBarWindow.show()