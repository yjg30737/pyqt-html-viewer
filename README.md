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
* Being able to see as a full screen

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
from pyqt_html_viewer import HtmlViewerApp

if __name__ == "__main__":
    import sys

    app = HtmlViewerApp(sys.argv)
    app.exec_()
```

Result

Start page

![image](https://user-images.githubusercontent.com/55078043/161404544-2aeccc11-0c1e-4a20-8333-82ff485f25ac.png)

Viewing html file

![image](https://user-images.githubusercontent.com/55078043/161404550-ee106954-8710-4daf-bba2-543eef8df427.png)

File list

![image](https://user-images.githubusercontent.com/55078043/161404557-e65cde1e-fbf6-42d0-bda6-7c295df6b7d1.png)

Source code

![image](https://user-images.githubusercontent.com/55078043/161404573-40aaa9e7-387b-4ee3-9bf6-16ff0c6edd5f.png)
