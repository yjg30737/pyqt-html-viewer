# pyqt-html-viewer
PyQt HTML Viewer 

## Requirements
* PyQt5 >= 5.8
* pyqtwebengine // For showing html file

## Setup
```
pip3 install pyqt5 --upgrade  # If you don't have pyqt5
pip3 install pyqtwebengine --upgrade
pip3 install git+https://github.com/yjg30737/pyqt-html-viewer.git --upgrade
```

## Code Example
```python
from PyQt5.QtWidgets import QApplication
from pyqt_html_viewer.htmlViewer import HtmlViewer

if __name__ == "__main__":
    import sys

    app = QApplication(sys.argv)
    htmlViewer = HtmlViewer()
    htmlViewer.show()
    app.exec_()
```

## Note
I'm still working.
