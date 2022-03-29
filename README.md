# pyqt-html-viewer
PyQt HTML Viewer 

## Requirements
* PyQt5 >= 5.15
* pyqtwebengine // For showing html file

## Features
* Being able to view all of html files in the folder
* Being able to see all of html files in the files list
* Being able to see html file when double-clicking one of files in the list 
* Being able to view the source of current html file
* Being able to see previous, next html file with left, right key
* Being able to resize each of widgets. (QSplitter)

## Setup
```
pip3 install pyqt5 --upgrade # If you don't have pyqt5
pip3 install pyqtwebengine --upgrade # If you don't have pyqtwebengine
pip3 install git+https://github.com/yjg30737/pyqt-html-viewer.git --upgrade
```
Note: If ModuleNotFoundError occured then do it all above in order.

## Included packages
* <a href="https://github.com/yjg30737/pyqt-checkbox-list-widget.git">pyqt-checkbox-list-widget</a>
* <a href="https://github.com/yjg30737/pyqt-style-setter.git">pyqt-style-setter</a>
* <a href="https://github.com/yjg30737/pyqt-custom-titlebar-setter.git">pyqt-custom-titlebar-setter</a>
* <a href="https://github.com/yjg30737/pyqt-svg-icon-pushbutton.git">pyqt-svg-icon-pushbutton</a>
* <a href="https://github.com/yjg30737/pyqt-description-tooltip.git">pyqt-description-tooltip</a>
* <a href="https://github.com/yjg30737/pyqt-viewer-widget.git">pyqt-viewer-widget</a>
* <a href="https://github.com/yjg30737/simplePyQt5.git">simplePyQt5</a>

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


