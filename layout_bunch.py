#!/usr/bin/env python
# -*- coding: utf-8 -*-

# @Package widget_bunch.py
# Package description
# Created on 14/09/2015
# @author bastien.laby
# Updated on 14/09/2015 by bastien.laby

# -*- coding: utf-8 -*-

# @Package widget_bunch.py
# Package description
# Created on 11/09/2015
# @author bastien.laby
# Updated on 11/09/2015 by bastien.laby

# -*- coding: utf-8 -*-

import sys

from PySide.QtGui import *
from PySide.QtCore import *

class Window(QMainWindow):
    def __init__(self, parent=None):
        super(Window, self).__init__()
        self.setWindowTitle("Pyside Widgets")

        # qgridlayout
        widget = QWidget()
        layout = QGridLayout()
        widget.setLayout(layout)

        layout.addWidget(QPushButton("1"), 0, 0, 2, 1)
        layout.addWidget(QPushButton("3"), 0, 1)
        layout.addWidget(QPushButton("4"), 1, 1)

        self.setCentralWidget(widget)
        


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Window(app)
    window.show()
    sys.exit(app.exec_())