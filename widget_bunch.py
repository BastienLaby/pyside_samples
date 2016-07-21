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

        widget = QWidget()
        layout = QVBoxLayout()
        widget.setLayout(layout)

        # Checkbox
        checkbox = QCheckBox("Checkbox", self)
        layout.addWidget(checkbox)

        # Combobox
        combobox = QComboBox(self)
        combobox.addItem("Combobox 1")
        combobox.addItem("Combobox 2")
        combobox.addItem("Combobox 3")
        layout.addWidget(combobox)

        # Command Link Button
        cmdLinkButton = QCommandLinkButton(self)
        cmdLinkButton.setDescription("Command Link Button")
        layout.addWidget(cmdLinkButton)

        # Date Time Edit
        dateTimeEdit = QDateTimeEdit(self)
        dateTimeEdit.setCalendarPopup(True)
        dateTimeEdit.setDisplayFormat("dd.MM.yyyy")
        layout.addWidget(dateTimeEdit)

        # Date Edit
        dateEdit = QDateEdit(self)
        dateEdit.setCalendarPopup(True)
        layout.addWidget(dateEdit)

        # QDial
        dial = QDial(self)
        dial.setNotchesVisible(True)
        layout.addWidget(dial)

        # Double SpinBox
        doubleSpinBox = QDoubleSpinBox(self)
        doubleSpinBox.setMinimum(-10.0)
        doubleSpinBox.setMaximum(10.0)
        doubleSpinBox.setSingleStep(0.1)
        layout.addWidget(doubleSpinBox)

        # Font Combo Box
        fontCombobox = QFontComboBox(self)
        layout.addWidget(fontCombobox)

        # LCD Number
        lcdNumber = QLCDNumber(10, self)
        lcdNumber.display("123 ABC")
        layout.addWidget(lcdNumber)

        # Object Name Test
        obj1 = QPushButton("1")
        obj1.setObjectName("objtest")
        layout.addWidget(obj1)
        obj2 = QPushButton("2")
        obj2.setObjectName("objtest")
        layout.addWidget(obj2)
        print obj1.objectName(), obj2.objectName()

        layout.addStretch(1)
        self.setCentralWidget(widget)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Window(app)
    window.show()
    sys.exit(app.exec_())