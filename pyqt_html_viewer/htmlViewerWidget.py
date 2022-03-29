from pyqt_viewer_widget import ViewerWidget
from pyqt_html_viewer.htmlViewerView import HtmlViewerView


class HtmlViewerWidget(ViewerWidget):

    def __init__(self):
        super().__init__()
        self.__initUi()

    def __initUi(self):
        mainWidget = HtmlViewerView()
        self.setView(mainWidget)

    def removeSomeFilesFromViewer(self, filenames_to_remove: list):
        cur_idx = self.getCurrentIndex()
        filenames = self.getFilenames()
        maintain_cur_idx_if_cur_idx_file_still_remain = filenames[cur_idx] in filenames_to_remove

        for filename in filenames_to_remove:
            filenames.remove(filename)

        if len(filenames) == 0:
            pass
        elif len(filenames) > cur_idx:
            if maintain_cur_idx_if_cur_idx_file_still_remain:
                self.setCurrentIndex(filenames.index(filenames[cur_idx]))
            else:
                self.setCurrentIndex(cur_idx-(len(filenames)-len(filenames_to_remove)))
        elif len(filenames) <= cur_idx:
            self.setCurrentIndex(-1)