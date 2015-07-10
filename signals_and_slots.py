#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys

from PySide.QtGui import *
from PySide.QtCore import *

class Window(QMainWindow):
    def __init__(self, parent=None):
        super(Window, self).__init__()
        self.setWindowTitle("Pyside Widgets")

        widget = QWidget()
        layout = QVBoxLayout()
        widget.setLayout(layout)

        # Combobox
        lineEdit = QLineEdit(self)
        layout.addWidget(lineEdit)

        # Label
        label = QLabel("Something here.")
        layout.addWidget(label)

        lineEdit.textEdited.connect(label.setText)

        self.setCentralWidget(widget)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Window(app)
    window.show()
    sys.exit(app.exec_())