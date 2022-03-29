from pyqt_viewer_widget import ViewerWidget
from pyqt_html_viewer.htmlViewerView import HtmlViewerView


class HtmlViewerWidget(ViewerWidget):

    def __init__(self):
        super().__init__()
        self.__initUi()

    def __initUi(self):
        mainWidget = HtmlViewerView()
        self.setView(mainWidget)