from PyQt5.QtWebEngineWidgets import QWebEngineView, QWebEnginePage
from PyQt5.QtCore import QUrl


class HtmlViewerView(QWebEngineView):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
    
    def setFilename(self, filename: str):
        self.__page = QWebEnginePage()
        self.__page.setUrl(QUrl(filename))
        self.setPage(self.__page)