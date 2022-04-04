from setuptools import setup, find_packages

setup(
    name='pyqt-html-viewer',
    version='0.4.1',
    author='Jung Gyu Yoon',
    author_email='yjg30737@gmail.com',
    license='MIT',
    packages=find_packages(),
    package_data={'pyqt_html_viewer.ico': ['add_dir.svg', 'add_file.svg', 'close.svg', 'list.svg', 'navigation_bar.svg',
                                           'remove.svg', 'source.svg', 'html.svg', 'full_screen.svg']},
    description='PyQt html viewer application',
    url='https://github.com/yjg30737/pyqt-html-viewer.git',
    install_requires=[
        'PyQt5>=5.15',
        'pyqtwebengine',
        'pyqt-checkbox-list-widget @ git+https://git@github.com/yjg30737/pyqt-checkbox-list-widget.git@main',
        'pyqt-style-setter @ git+https://git@github.com/yjg30737/pyqt-style-setter.git@main',
        'pyqt-custom-titlebar-setter @ git+https://git@github.com/yjg30737/pyqt-custom-titlebar-setter.git@main',
        'pyqt-svg-icon-pushbutton @ git+https://git@github.com/yjg30737/pyqt-svg-icon-pushbutton.git@main',
        'pyqt-description-tooltip @ git+https://git@github.com/yjg30737/pyqt-description-tooltip.git@main',
        'pyqt-viewer-widget @ git+https://git@github.com/yjg30737/pyqt-viewer-widget.git@main',
        'simplePyQt5 @ git+https://git@github.com/yjg30737/simplePyQt5.git@master'
    ]
)