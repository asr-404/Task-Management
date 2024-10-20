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

        # Menu bar
        menu_bar = self.menuBar()

        # Adding stylesheet to the menu bar
        menu_bar.setStyleSheet("""
            QMenuBar {color: green; font-weight:500;}
            QMenuBar::item:selected {background-color: yellow;}  # Highlighted menu item
        """)

        # Create menus and actions
        self.all_tasks_action = QAction("All Tasks", self)
        self.new_tasks_action = QAction("New Tasks", self)
        self.pending_tasks_action = QAction("Pending Tasks", self)
        self.completed_tasks_action = QAction("Completed Tasks", self)

        # Create the menu and add actions
        tasks_menu = menu_bar.addMenu("Tasks")
        tasks_menu.addAction(self.all_tasks_action)
        tasks_menu.addAction(self.new_tasks_action)
        tasks_menu.addAction(self.pending_tasks_action)
        tasks_menu.addAction(self.completed_tasks_action)

        # Creating widgets for each task category
        self.all_tasks_container = QWidget()
        self.new_tasks_container = QWidget()
        self.pending_tasks_container = QWidget()
        self.completed_tasks_container = QWidget()

        # Set background colors for clarity
        self.all_tasks_container.setStyleSheet("background:red;")
        # self.new_tasks_container.setStyleSheet("background:green;")
        self.pending_tasks_container.setStyleSheet("background:blue;")
        self.completed_tasks_container.setStyleSheet("background:yellow;")

        # Add the containers to the stacked widget
        self.stacked_widget.addWidget(self.all_tasks_container)
        self.stacked_widget.addWidget(self.new_tasks_container)
        self.stacked_widget.addWidget(self.pending_tasks_container)
        self.stacked_widget.addWidget(self.completed_tasks_container)

        # Set the first container to be shown initially
        self.stacked_widget.setCurrentWidget(self.all_tasks_container)

        # Connect actions to manually switch views
        self.all_tasks_action.triggered.connect(self.showAllTasks)
        self.new_tasks_action.triggered.connect(self.showNewTasks)
        self.pending_tasks_action.triggered.connect(self.showPendingTasks)
        self.completed_tasks_action.triggered.connect(self.showCompletedTasks)



if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = TaskMgt()
    window.show()
    sys.exit(app.exec_())