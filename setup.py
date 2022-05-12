from setuptools import setup, find_packages

setup(
    name='pyqt-html-viewer',
    version='0.4.1',
    author='Jung Gyu Yoon',
    author_email='yjg30737@gmail.com',
    license='MIT',
    packages=find_packages(),
    package_data={'pyqt_html_viewer.ico': ['add_dir.svg', 'add_file.svg', 'close.svg',
                                           'list.svg', 'navigation_bar.svg',
                                           'source.svg', 'html.svg', 'full_screen.svg']},
    description='PyQt html viewer application',
    url='https://github.com/yjg30737/pyqt-html-viewer.git',
    install_requires=[
        'PyQt5>=5.15',
        'pyqtwebengine',
        'pyqt-style-setter>=0.0.1',
        'pyqt-custom-titlebar-setter>=0.0.1',
        'pyqt-description-tooltip @ git+https://git@github.com/yjg30737/pyqt-description-tooltip.git@main',
        'pyqt-list-viewer-widget @ git+https://git@github.com/yjg30737/pyqt-list-viewer-widget.git@main',
        'pyqt-get-selected-filter @ git+https://git@github.com/yjg30737/pyqt-get-selected-filter.git@main'
    ]
)