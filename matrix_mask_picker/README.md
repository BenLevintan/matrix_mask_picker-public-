Matrix Mask Picker
Overview
Matrix Mask Picker is a Python application designed to toggle matrix masks on and off. It provides a graphical user interface (GUI) built using PyQt5, allowing users to open JSON and CSV files, load data into tables, visualize and manipulate matrices, and save modified data back to CSV files.

Features
Open JSON and CSV Files: Users can open JSON and CSV files containing matrix data through the application.
Load Matrix Data: Matrix data from JSON files can be loaded into corresponding tables.
Visualize Matrix Masks: The application provides tables to visualize Actuators Mask and Relevant Lenslets Vector matrices.
Sync Tables: Users can synchronize data between input and output tables.
Manipulate Matrix Data: All cells can be set to either "on" or "off" state, and individual cells can be toggled.
Save Modified Data: Modified matrix data can be saved back to CSV files.
Usage
Open Files: Click on "Open JSON File" or "Open CSV File" buttons to select respective files.
Load Matrix Data: Click on "Actuators Mask" or "Relevant Lenslets" buttons to load data into the corresponding tables.
Manipulate Data: Use "All off", "All on", or click on individual cells to manipulate matrix data.
Sync Tables: Click on the "Sync" button to synchronize data between input and output tables.
Save Data: Click on the "Save" button to save modified matrix data to a CSV file.
Requirements
Python 3.11.4
PyQt5
NumPy
Installation
Install PyQt5 and NumPy using pip:
Copy code
pip install PyQt5 numpy
How to Run
Run the Python script matrix_mask_picker.py.

bash
Copy code
python matrix_mask_picker.py
Contributors
[Your Name]
Version
Matrix visualizer 1.0.0
