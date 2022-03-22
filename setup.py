from setuptools import setup, find_packages

setup(
    name='pyqt-html-viewer',
    version='0.1.1',
    author='Jung Gyu Yoon',
    author_email='yjg30737@gmail.com',
    license='MIT',
    packages=find_packages(),
    package_data={'pyqt_html_viewer.style': ['button.css', 'dark_gray_theme.css', 'viewer_button.css'],
                  'pyqt_html_viewer.ico': ['add_dir.png', 'add_file.png', 'close.png', 'list.png', 'navigation_bar.png',
                                           'remove.png', 'source.png', 'html.svg']},
    description='PyQt html viewer application',
    url='https://github.com/yjg30737/pyqt-html-viewer.git',
    install_requires=[
        'PyQt5>=5.15.1',
        'pyqtwebengine',
        'pyqt-checkbox-list-widget @ git+https://git@github.com/yjg30737/pyqt-checkbox-list-widget.git@main',
        'pyqt-style-setter @ git+https://git@github.com/yjg30737/pyqt-style-setter.git@main',
        'pyqt-custom-titlebar-setter @ git+https://git@github.com/yjg30737/pyqt-custom-titlebar-setter.git@main',
        'simplePyQt5 @ git+https://git@github.com/yjg30737/simplePyQt5.git@master'
    ]
)