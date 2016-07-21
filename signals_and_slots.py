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

        # spinboxes
        self.sp1 = QDoubleSpinBox()
        self.sp2 = QDoubleSpinBox()
        self.sp1.valueChanged.connect(self.cb_spinboxes)
        self.sp2.valueChanged.connect(self.cb_spinboxes)
        layout.addWidget(self.sp1)
        layout.addWidget(self.sp2)

        lineEdit.textEdited.connect(label.setText)

        self.setCentralWidget(widget)


    def cb_spinboxes(self, value):
        print self.sender(), value


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Window(app)
    window.show()
    sys.exit(app.exec_())