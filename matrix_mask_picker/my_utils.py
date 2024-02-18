#!/usr/bin/python3

import json
import csv
import sys
import numpy as np

from PyQt5 import QtWidgets, QtGui
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QTableWidget,
    QTableWidgetItem, QFileDialog, QMessageBox
)
class change_clicked_cell_value:
    def __init__(self, on_value, off_value, item, on_color, off_color):
        self.on_value = on_value
        self.off_value = off_value
        self.item = item
        self.off_color = off_color
        self.on_clolr = on_color

    def set_cell_color(self, item, new_value, on_color, off_color):
        if int(item.text()) == self.off_value:
            item.setBackground(on_color)
        else:
            item.setBackground(off_color)
    
    def on_table_item_clicked(self, item, on_value, off_value):
        current_value = int(item.text())
        new_value = on_value if current_value == off_value else off_value
        item.setText(str(new_value))

        self.set_cell_color(item, new_value, QtGui.QColor(0, 255, 0), QtGui.QColor(0, 0, 255))
