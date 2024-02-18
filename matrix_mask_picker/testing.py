from PyQt5 import QtWidgets, QtGui
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QTableWidget,
    QTableWidgetItem, QFileDialog, QMessageBox
)
import json
import csv
import sys
import numpy as np


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()

        self.setGeometry(200, 200, 1550, 700)
        self.setWindowTitle("Matrix Mask Picker")
        self.init_UI()

    def init_UI(self):
        # QLabel for displaying text
        self.label = QtWidgets.QLabel(self)
        self.label.setText("Calib Data")
        self.label.move(130, 20)

        font = QtGui.QFont()
        font.setPointSize(14)
        self.label.setFont(font)

        self.label = QtWidgets.QLabel(self)
        self.label.setText("File Data")
        self.label.move(1200, 20)
        
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label.setFont(font)

        # QPushButton for opening a JSON file
        self.btn1 = QtWidgets.QPushButton(self)
        self.btn1.setText("Open JSON File")
        self.btn1.move(120, 60)
        self.btn1.clicked.connect(self.open_file)

        # QPushButton for opening a CSV file
        self.btn_csv = QtWidgets.QPushButton(self)
        self.btn_csv.setText("Open CSV File")
        self.btn_csv.move(1195, 60)
        self.btn_csv.clicked.connect(self.open_csv)

        # QPushButton for loading Actuators Mask
        self.btn_Actuators_Mask = QtWidgets.QPushButton(self)
        self.btn_Actuators_Mask.setText("Actuators Mask")
        self.btn_Actuators_Mask.move(50, 100)
        self.btn_Actuators_Mask.clicked.connect(self.load_actuators_mask)

        # QPushButton for loading Relevant Lenslets Vector
        self.btn_relevant_lenslets = QtWidgets.QPushButton(self)
        self.btn_relevant_lenslets.setText("Relevant Lenslets")
        self.btn_relevant_lenslets.move(200, 100)
        self.btn_relevant_lenslets.clicked.connect(
            self.load_relevant_lenslets_vector
        )
        # QPushButton for syncing data 
        self.btn_sync = QtWidgets.QPushButton(self)
        self.btn_sync.setText("Sync")
        self.btn_sync.move(720, 200)
        self.btn_sync.clicked.connect(self.sync_tables)

        # QPushButton for changing all cells to off 
        self.btn_all_off = QtWidgets.QPushButton(self)
        self.btn_all_off.setText("All off")
        self.btn_all_off.move(720, 240)
        self.btn_all_off.clicked.connect(self.all_off)

        # QPushButton for changing all cells to on
        self.btn_all_on = QtWidgets.QPushButton(self)
        self.btn_all_on.setText("All on")
        self.btn_all_on.move(720, 280)
        self.btn_all_on.clicked.connect(self.all_on)

        # QPushButton for saving data 
        self.btn_save = QtWidgets.QPushButton(self)
        self.btn_save.setText("Save")
        self.btn_save.move(720, 360)
        self.btn_save.clicked.connect(self.save_table)

        # A variable to store the CSV and JSON data as a dictionary
        self.json_data = {}
        self.csv_data ={}

        # Table widget to display the Actuators Mask matrix
        self.actuators_mask_table = QTableWidget(self)
        self.setup_table(self.actuators_mask_table, 12, 12, 50, 150)
        self.actuators_mask_table.setHorizontalHeaderLabels(['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l'])
        self.actuators_mask_table.hide()

        # Table widget to display the Relevant Lenslets Vector matrix
        self.relevant_lenslets_table = QTableWidget(self)
        self.setup_table(self.relevant_lenslets_table, 15, 16, 50, 150)
        self.relevant_lenslets_table.setHorizontalHeaderLabels(
            ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q']
        )
        self.relevant_lenslets_table.hide()

        # Table widget to display the output of Actuators Mask matrix Vector matrix
        self.output_mask_table = QTableWidget(self)
        self.setup_table(self.output_mask_table, 12, 12, 850, 150)
        self.output_mask_table.setHorizontalHeaderLabels(['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l'])
        self.output_mask_table.hide()


        # Table widget to display the output of Lenslets Vector matrix Vector matrix
        self.output_lenslets_table = QTableWidget(self)
        self.setup_table(self.output_lenslets_table, 15, 16, 850, 150)
        self.output_lenslets_table.setHorizontalHeaderLabels(
            ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q']
        )
        self.output_lenslets_table.hide()


    def setup_table(self, table, rows, columns, x, y):
        table.setGeometry(x, y, columns * 41, rows * 33)
        table.setRowCount(rows)
        table.setColumnCount(columns)
        for i in range(columns):
            table.setColumnWidth(i, 5)

        table.itemClicked.connect(self.on_table_item_clicked)

    def open_file(self):
        # Open a file dialog to select a JSON file
        options = QFileDialog.Options()
        options |= QFileDialog.ReadOnly
        file_name, _ = QFileDialog.getOpenFileName(
            self, "Open JSON File", "", "JSON Files (*.json);;All Files (*)", options=options
        )
        if file_name:
            # User selected a file, read and parse it using the json library
            with open(file_name, 'r') as file:
                self.json_data = json.load(file)
                print("JSON Data as a Python Dictionary:")
                print(self.json_data)

    def open_csv(self):
        # Open a file dialog to select a CSV file
        options = QFileDialog.Options()
        options |= QFileDialog.ReadOnly
        file_name, _ = QFileDialog.getOpenFileName(
            self, "Open CSV File", "", "CSV Files (*.csv);;All Files (*)", options=options
        )

        if file_name:
            # User selected a file, read and parse it using the csv module
            with open(file_name, 'r') as file:
                reader = csv.reader(file)
                csv_data = list(reader)
                print("CSV Data as a Python List:")
                print(csv_data)

            # Determine the dimensions of the CSV data
            rows, columns = len(csv_data), len(csv_data[0]) if csv_data else (0, 0)

            # Set up the output table based on dimensions
            if rows == 12 and columns == 12:
                self.output_mask_table.show()
                self.output_lenslets_table.hide()
            elif rows == 15 and columns == 16:
                self.output_lenslets_table.show()
                self.output_mask_table.hide()
            else:
                self.show_popup("Unknown table dimensions")

            # Store the CSV data for future use
            self.csv_data = csv_data

            # Load CSV data into the output table
            self.load_csv_matrix()

    def load_csv_matrix(self):
        if not self.csv_data:
            # No CSV file loaded, show a pop-up
            self.show_popup("Please load a CSV file first.")
        else:
            rows, columns = len(self.csv_data), len(self.csv_data[0])

            # Set up the table based on CSV dimensions
            if rows == 12 and columns == 12:
                table = self.output_mask_table
            elif rows == 15 and columns == 16:
                table = self.output_lenslets_table
            else:
                # Should not reach here, as this is handled in open_csv
                return

            self.setup_table(table, rows, columns, table.x(), table.y())

            for i in range(rows):
                for j in range(columns):
                    # Convert boolean value to 1 or 0
                    value = int(self.csv_data[i][j])

                    # If the item already exists, update it; otherwise, create a new item
                    item = table.item(i, j)
                    if item is None:
                        item = QTableWidgetItem(str(value))
                        table.setItem(i, j, item)
                    else:
                        item.setText(str(value))

                    # Set the cell color
                    if value == 1:
                        item.setBackground(QtGui.QColor(80, 205, 80))  # Green
                    else:
                        item.setBackground(QtGui.QColor(80, 80, 205))  # Blue

            table.show()  # Show the table after loading data

            # Hide the other tables
            self.output_mask_table.hide() if table == self.output_lenslets_table else self.output_lenslets_table.hide()
            table.itemClicked.connect(self.on_table_item_clicked)

    def load_actuators_mask(self):
        self.load_matrix('actuatorsMask', self.actuators_mask_table)

    def load_relevant_lenslets_vector(self):
        self.load_matrix('relevantLensletsVector', self.relevant_lenslets_table)

    def load_matrix(self, key, table):
        if not self.json_data:
            # No JSON file loaded, show a pop-up
            self.show_popup("Please load a JSON file first.")
        else:
            matrix_data = self.json_data.get(key)
            if matrix_data is None:
                # Key not found, show a pop-up
                self.show_popup(f"'{key}' key not found in the JSON data.")
            else:
                # Reshape the data into a 2D array
                reshaped_data = np.array(matrix_data).reshape((table.rowCount(), table.columnCount()))
                self.update_matrix_table(table, reshaped_data)
                table.show()  # Show the table after loading data

                # Hide the other table
                if table == self.actuators_mask_table:
                    self.relevant_lenslets_table.hide()
                else:
                    self.actuators_mask_table.hide()

 
    def update_matrix_table(self, table, data):
        for i in range(table.rowCount()):
            for j in range(table.columnCount()):
                # Convert boolean value to 1 or 0
                value = int(data[i, j])
                item = QTableWidgetItem(str(value))
                table.setItem(i, j, item)

                # Set the cell color
                if value == 1:
                    item.setBackground(QtGui.QColor(80, 205, 80))  # Green
                else:
                    item.setBackground(QtGui.QColor(80, 80, 205))  # Blue

    def sync_tables(self):
        # Check which tables are currently visible
        source_table = None
        destination_table = None

        if self.actuators_mask_table.isVisible():
            source_table = self.actuators_mask_table
            destination_table = self.output_mask_table
        elif self.relevant_lenslets_table.isVisible():
            source_table = self.relevant_lenslets_table
            destination_table = self.output_lenslets_table

        if source_table and destination_table:
            # Copy data from the source table to the destination table
            self.copy_table_data(source_table, destination_table)
        else:
            self.show_popup("Please load data first.")

    def copy_table_data(self, source_table, destination_table):
        for i in range(source_table.rowCount()):
            for j in range(source_table.columnCount()):
                source_item = source_table.item(i, j)
                destination_item = destination_table.item(i, j)

                if source_item and destination_item:
                    # Copy the value from the source cell to the destination cell
                    destination_item.setText(source_item.text())
                    destination_item.setBackground(source_item.background())

    def save_table(self):
        if not self.csv_data:
            self.show_popup("Please load a CSV file first.")
            return

        rows, columns = len(self.csv_data), len(self.csv_data[0])

        # Determine which output table is visible
        if self.output_mask_table.isVisible():
            table = self.output_mask_table
        elif self.output_lenslets_table.isVisible():
            table = self.output_lenslets_table
        else:
            self.show_popup("No output table visible.")
            return

        # Update the CSV data with the data from the output table
        for i in range(rows):
            for j in range(columns):
                item = table.item(i, j)
                if item:
                    self.csv_data[i][j] = item.text()

        # Save the updated data back to the CSV file
        file_name, _ = QFileDialog.getSaveFileName(
            self, "Save CSV File", "", "CSV Files (*.csv);;All Files (*)"
        )
        if file_name:
            with open(file_name, 'w', newline='') as file:
                writer = csv.writer(file)
                writer.writerows(self.csv_data)

    def all_off(self):
        self.set_all_cells(0)

    def all_on(self):
        self.set_all_cells(1)

    def set_all_cells(self, value):
        # Determine which output table is visible
        if self.output_mask_table.isVisible():
            table = self.output_mask_table
        elif self.output_lenslets_table.isVisible():
            table = self.output_lenslets_table
        else:
            self.show_popup("No output table visible.")
            return

        # Iterate through all cells and set the value
        for i in range(table.rowCount()):
            for j in range(table.columnCount()):
                item = table.item(i, j)
                if item:
                    item.setText(str(value))

                    # Update the cell color
                    if value == 1:
                        item.setBackground(QtGui.QColor(0, 255, 0))  # Green
                    else:
                        item.setBackground(QtGui.QColor(0, 0, 255))  # Blue


    def on_table_item_clicked(self, item):
        # Toggle between 1 and 0 when a cell is clicked
        current_value = int(item.text())
        new_value = 1 if current_value == 0 else 0
        item.setText(str(new_value))

        # Update the cell color
        if new_value == 1:
            item.setBackground(QtGui.QColor(0, 255, 0))  # Green
        else:
            item.setBackground(QtGui.QColor(0, 0, 255))  # Blue

    def show_popup(self, message):
        # Create a QMessageBox with the specified message
        popup = QMessageBox(self)
        popup.setWindowTitle("Information")
        popup.setText(message)
        popup.setIcon(QMessageBox.Information)
        popup.addButton(QMessageBox.Ok)
        popup.exec_()


def window():
    app = QtWidgets.QApplication(sys.argv)
    main_win = MainWindow()
    main_win.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    window()