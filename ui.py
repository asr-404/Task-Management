from PyQt5.QtWidgets import (QApplication, 
    QWidget, 
    QMainWindow, 
    QStackedWidget, 
    QAction, 
    QFormLayout, 
    QLabel, 
    QLineEdit, 
    QRadioButton, QHBoxLayout,
    QDateEdit )

import sys

class TaskMgt(QMainWindow):
    def __init__(self):

        super().__init__()
        self.setGeometry(300, 300, 500, 400)
        self.setWindowTitle("Task Manager")
        self.stacked_widget = QStackedWidget()
        self.setCentralWidget(self.stacked_widget)
