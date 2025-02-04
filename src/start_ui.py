# start_ui.py
"""This module contains the InputDialog class for the Stealth Solver application."""

import sys
from PyQt5.QtWidgets import (
    QDialog,
    QGridLayout,
    QLabel,
    QComboBox,
    QSpinBox,
    QPushButton,
    QHBoxLayout,
)
from PyQt5.QtGui import QIcon


class InputDialog(QDialog):
    def __init__(self):
        """Initialize the InputDialog."""
        super().__init__()
        self.setWindowTitle("Stealth Solver")

        self.setWindowIcon(QIcon('assets/logo128.png'))

        # Apply the dark stylesheet specifically to the InputDialog
        dark_stylesheet = """
        QDialog {
            background-color: #2b2b2b;
        }
        QLabel {
            color: white;
        }
        QPushButton:hover {
            background-color: #606366;
        }
        QPushButton:pressed {
            background-color: #404244;
        }
        """
        self.setStyleSheet(dark_stylesheet)  # Apply the stylesheet to this dialog

        self.resize(500, 300)

        # Layout for the dialog
        layout = QGridLayout()

        # Add 20px margins around the grid layout
        layout.setContentsMargins(50, 0, 50, 0)

        # Screen number input (Label and SpinBox)
        self.screen_label = QLabel("Screen Number :")
        self.screen_label.setStyleSheet(
            "font-size: 16px; font-weight: bold;"
        )  # Slightly smaller text
        self.screen_input = QSpinBox()
        self.screen_input.setMinimum(0)  # Minimum screen number
        self.screen_input.setStyleSheet(
            """
            QSpinBox {
                font-size: 16px;
                padding: 6px;
                background-color: #3c3f41;
                color: white;
                border-radius: 5px;
            }
           

            QSpinBox:hover {
                background-color: #2b2d30; /* Darker color when hovering over the input box */
            }
        """
        )
        layout.addWidget(self.screen_label, 0, 0)  # Row 0, Column 0
        layout.addWidget(self.screen_input, 0, 1)  # Row 0, Column 1

        # Code language selection (Label and ComboBox)
        self.language_label = QLabel("Coding Language :")
        self.language_label.setStyleSheet(
            "font-size: 16px; font-weight: bold;"
        )  # Slightly smaller text
        self.language_input = QComboBox()
        self.language_input.addItems(
            ["Python", "Java", "C++", "JavaScript", "TypeScript", "C", "C#"]
        )  # Options
        self.language_input.setStyleSheet(
            """
            QComboBox {
                font-size: 16px;
                padding: 6px;
                background-color: #3c3f41;
                color: white;
                border-radius: 5px;
            }
            QComboBox::drop-down {
                border: none;
            }
            QComboBox:hover {
                background-color: #2b2d30; /* Darker color on hover */
            }
            QComboBox QAbstractItemView {
                background-color: #3c3f41; /* Dropdown background color */
                color: white; /* Text color */
                border: 1px solid #2b2d30; /* Border around the dropdown */
                selection-background-color: #2b2d30; /* Background color of selected item */
                selection-color: white; /* Text color of selected item */
            }
            QComboBox QAbstractItemView::item:hover {
                background-color: #2b2d30; /* Darker hover color for dropdown items */
                color: white; /* Text color on hover */
            }
        """
        )
        layout.addWidget(self.language_label, 1, 0)  # Row 1, Column 0
        layout.addWidget(self.language_input, 1, 1)  # Row 1, Column 1

        # Provider name selection (Label and ComboBox)
        self.provider_name = QLabel("gpt4free Provider :")
        self.provider_name.setStyleSheet(
            "font-size: 16px; font-weight: bold;"
        )  # Slightly smaller text
        self.provider_input = QComboBox()
        self.provider_input.addItems(
            [
                "g4f.Provider.Blackbox",
                "g4f.Provider.OIVSCode",
                "g4f.Provider.PollinationsAI",
            ]
        )  # Options
        self.provider_input.setStyleSheet(
            """
            QComboBox {
                font-size: 16px;
                padding: 6px;
                background-color: #3c3f41;
                color: white;
                border-radius: 5px;
            }
            QComboBox::drop-down {
                border: none;
            }
            QComboBox:hover {
                background-color: #2b2d30; /* Darker color on hover */
            }
            QComboBox QAbstractItemView {
                background-color: #3c3f41; /* Dropdown background color */
                color: white; /* Text color */
                border: 1px solid #2b2d30; /* Border around the dropdown */
                selection-background-color: #2b2d30; /* Background color of selected item */
                selection-color: white; /* Text color of selected item */
            }
            QComboBox QAbstractItemView::item:hover {
                background-color: #2b2d30; /* Darker hover color for dropdown items */
                color: white; /* Text color on hover */
            }
        """
        )
        layout.addWidget(self.provider_name, 2, 0)  # Row 2, Column 0
        layout.addWidget(self.provider_input, 2, 1)  # Row 2, Column 1

        # OK and Cancel buttons
        button_layout = QHBoxLayout()
        self.ok_button = QPushButton("OK")
        self.ok_button.setStyleSheet(
            """
            QPushButton {
                font-size: 16px;
                padding: 8px;
                background-color: #505357;
                color: white;
                border-radius: 5px;
            }
            QPushButton:hover {
                background-color: #606366;
            }
            QPushButton:pressed {
                background-color: #404244;
            }
            """
        )  # Neutral dark theme for OK button
        self.ok_button.clicked.connect(self.accept)  # Close dialog and return values

        self.cancel_button = QPushButton("Cancel")
        self.cancel_button.setStyleSheet(
            """
            QPushButton {
                font-size: 16px;
                padding: 8px;
                background-color: #505357;
                color: white;
                border-radius: 5px;
            }
            QPushButton:hover {
                background-color: #606366;
            }
            QPushButton:pressed {
                background-color: #404244;
            }
            """
        )  # Neutral dark theme for Cancel button
        self.cancel_button.clicked.connect(sys.exit)  # Close dialog without saving

        button_layout.addWidget(self.ok_button)
        button_layout.addWidget(self.cancel_button)

        layout.addLayout(button_layout, 3, 0, 1, 2)  # Buttons span across columns

        self.setLayout(layout)

    def closeEvent(self, event):
        """
        Close the application when the window is closed.
        """
        sys.exit()

    def get_values(self):
        """Retrieve the user inputs."""
        return (
            self.screen_input.value(),
            self.language_input.currentText(),
            self.provider_input.currentText().split(".")[-1],
        )
