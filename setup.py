import os

from setuptools import setup, find_packages

setup(
    name='pyqt-html-viewer',
    version='0.0.1',
    author='Jung Gyu Yoon',
    author_email='yjg30737@gmail.com',
    license='MIT',
    packages=find_packages(),
    package_data={'pyqt-html-viewer.style': ['button.css', 'dark_gray_theme.css', 'viewer_button.css'],
                  'pyqt-html-viewer.ico': os.listdir()[1:]},
    description='PyQt html viewer',
    url='https://github.com/yjg30737/pyqt-html-viewer.git',
    install_requires=[
        'PyQt5>=5.8',
        'pyqt-checkbox-list-widget @ git+https://git@github.com/yjg30737/pyqt-checkbox-list-widget.git@main',
        'simplePyQt5 @ git+https://git@github.com/yjg30737/simplePyQt5.git@main'
    ]
)