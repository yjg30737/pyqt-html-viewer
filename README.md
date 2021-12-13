# pyqt-html-viewer
PyQt HTML Viewer 

## Requirements
* PyQt5 >= 5.8
* pyqtwebengine // For showing html file

## Setup
```
pip3 install pyqt5 --upgrade # If you don't have pyqt5
pip3 install pyqtwebengine --upgrade # If you don't have pyqtwebengine
pip3 install git+https://github.com/yjg30737/pyqt-html-viewer.git --upgrade
```
Note: Install order is important. pyqt5 first, pyqtwebengine second.

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

Result

Start page

![image](https://user-images.githubusercontent.com/55078043/145768616-99853ea0-10ef-49fb-97ef-5a54e5fab79e.png)

Viewing html file

![image](https://user-images.githubusercontent.com/55078043/145768743-47d43a7f-8294-490c-9dd3-386376e086da.png)

File list

![image](https://user-images.githubusercontent.com/55078043/145768850-78661206-de06-497d-ac4f-ecd621b68b2a.png)

Source code

![image](https://user-images.githubusercontent.com/55078043/145768928-c2dbadb7-3498-4dfb-ade7-bcdd370ce2eb.png)

HTML file web view only

![image](https://user-images.githubusercontent.com/55078043/145769084-ed38eca6-1306-41e9-b594-571e11a2d4a1.png)


