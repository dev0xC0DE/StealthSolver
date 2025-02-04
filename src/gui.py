# src/gui.py
"""
This module contains the main window class for the Stealth Solver application.
"""

import shutil
import os

from PyQt5.QtWidgets import (
    QApplication,
    QMainWindow,
    QLabel,
    QWidget,
    QScrollArea,
    QVBoxLayout,
)
from PyQt5.QtCore import Qt

from .window_manager import (
    set_window_exclude_from_capture,
    move_to_target_screen,
    update_screen_info,
    resize_window,
    move_window,
)
from .hotkeys import setup_hotkeys
from .screenshot import take_screenshot
from .highlighter import extract_highlighted_code


class MainWindow(QMainWindow):
    def __init__(
        self,
        screen_num=0,
        media_folder="media",
        code_language="Python",
        provider_name="Blackbox",
    ):
        """
        Initialize the main window.

        Args:
            screen_num (int): The index of the screen to display on. Defaults to 0.
            media_folder (str): The path to the folder containing the screenshots.
                Defaults to "media".
        """
        super().__init__()
        self.setWindowTitle(" ")
        self.setWindowFlags(Qt.WindowStaysOnTopHint | Qt.FramelessWindowHint | Qt.Tool)
        self.setAttribute(Qt.WA_TranslucentBackground, True)

        # QApplication.instance().setStyle('Fusion')
        self.init_variables(screen_num, media_folder, code_language, provider_name)
        self.setup_window()
        _ = extract_highlighted_code(media_folder=self.media_folder)
        self.reset()
        self.setup_hotkeys()

    def init_variables(self, screen_num, media_folder, code_language, provider_name):
        """Initialize common variables."""
        self.current_screen = None
        self.screen_geometry = None
        self.brightness_level = 0.9
        self.screenShotsTaken = 0
        self.target_screen = screen_num
        self.media_folder = media_folder
        self.code_language = code_language
        self.provider_name = provider_name
        self.python_code = ""

    def setup_window(self):
        """Setup window position and background."""
        self.move_to_target_screen()
        self.update_screen_info()
        self.setup_ui()
        self.set_view()
        self.create_background()
        self.set_window_exclude_from_capture()

    def set_window_exclude_from_capture(self):
        """Exclude the main window from being captured by screen recording/sharing tools."""
        set_window_exclude_from_capture(self)

    def setup_hotkeys(self):
        """Set up keyboard shortcuts for various actions."""
        setup_hotkeys(self)

    def move_to_target_screen(self):
        """Move the main window to the target screen."""
        move_to_target_screen(self)

    def update_screen_info(self):
        """Update the screen information by determining the current screen and its geometry."""
        update_screen_info(self)

    def set_view(self):
        """Set window size and position."""
        self.resize_window()
        self.move_window(0.1, 0.15)

    def create_background(self):
        """Set background color based on brightness level"""
        self.bg_widget = QWidget(self)
        self.resize_window(widget=self.bg_widget)
        self.bg_widget.setStyleSheet(
            f"background-color: rgba(0, 0, 0, {self.brightness_level});"
        )

        # Ensure the background widget stays behind other widgets.
        self.bg_widget.lower()

    def setup_ui(self):
        """Set up UI components."""
        central_widget = QWidget(self)
        self.setCentralWidget(central_widget)
        self.main_layout = QVBoxLayout(central_widget)

        _, self.header_label = self.create_scroll_area()
        self.scroll_code_area, self.code_label = self.create_scroll_area()

        self.header_label.setText(self.get_header_text())
        self.header_label.setAlignment(Qt.AlignTop | Qt.AlignCenter)
        self.header_label.setStyleSheet(
            "background: transparent; border: none; margin-top:3px;"
        )
        self.main_layout.addWidget(self.header_label)

        self.scroll_code_area.setWidget(self.code_label)
        self.scroll_code_area.setStyleSheet(
            "background: transparent; border: none; margin: 10px 25px 20px 25px;"
        )
        self.main_layout.addWidget(self.scroll_code_area, stretch=8)

    def create_scroll_area(self):
        """Create a reusable scroll area with a label."""
        scroll_area = QScrollArea(self)
        scroll_area.setWidgetResizable(True)
        scroll_area.setStyleSheet("background: transparent; border: none;")
        scroll_area.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        scroll_area.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        label = QLabel(self)
        label.setWordWrap(True)
        label.setAlignment(Qt.AlignTop | Qt.AlignLeft)
        return scroll_area, label

    def get_header_text(self):
        """Return formatted header text."""
        return f"""
                <html>
                    <body style="background-color: rgba(0, 0, 0, 0); color: #E0E0E0; font-family: Arial, sans-serif; margin: 0; padding: 0;">
                        <div style="display: flex; justify-content: center; align-items: center; height: 100vh;">
                            <div>
                                <h1 style="font-size: 20px; font-weight: bold;  text-align: center;">Stealth Solver</h1>
                                <table style="margin: 0 auto; margin-top: 10px; font-size: 12px; font-weight: bold; border-collapse: collapse; text-align: center;">
                                    <tr>
                                        <td style="padding: 20px; border: 1px solid white; text-align: center; vertical-align: middle;">Move Window &nbsp; <span style="font-weight: bold;">[Cmd + arrows]</span></td>
                                        <td style="padding: 20px; border: 1px solid white; text-align: center; vertical-align: middle;">Take Screenshots &nbsp; <span style="font-weight: bold;">[Cmd + H]</span></td>
                                        <td style="padding: 20px; border: 1px solid white; text-align: center; vertical-align: middle;">Reset &nbsp; <span style="font-weight: bold;">[Cmd + R]</span></td>
                                    </tr>
                                    <tr>
                                        <td style="padding: 20px; border: 1px solid white; text-align: center; vertical-align: middle;">Toggle Brightness &nbsp; <span style="font-weight: bold;">[Cmd + b]</span></td>
                                        <td style="padding: 20px; border: 1px solid white; text-align: center; vertical-align: middle;">Get Code &nbsp; <span style="font-weight: bold;">[Cmd + Enter]</span></td>
                                        <td style="padding: 20px; border: 1px solid white; text-align: center; vertical-align: middle;">Quit &nbsp; <span style="font-weight: bold;">[Cmd + Q]</span></td>
                                    </tr>
                                </table>
                                <div style="display: flex; justify-content: center; align-items: center; margin-top: 10px;">
                                    <p style="font-size: 12px; font-weight: bold; color: green;">{self.screenShotsTaken} ScreenShot Taken</p>
                                </div>
                            </div>
                        </div>
                    </body>
                </html>
                """

    def resize_window(self, height_ratio=0, widget=None):
        """Resize a widget based on the main layout's preferred size, respecting the given height ratio.

        Args:
            height_ratio (float, optional): The ratio of the height to the preferred height of the main layout. Defaults to 0.
            widget (QWidget, optional): The widget to resize. Defaults to None.
        """

        resize_window(self, height_ratio, widget)

    def move_window(self, dx_ratio, dy_ratio):
        """Move window in percentage-based increments.

        Args:
            dx_ratio (float): The percentage to move horizontally.
            dy_ratio (float): The percentage to move vertically.
        """
        move_window(self, dx_ratio, dy_ratio)

    def toggle_brightness(self):
        """Reduce brightness by 20% with each toggle; reset to 90% at minimum brightness of 10%."""

        # Reduce brightness by 20%
        self.brightness_level -= 0.2

        # Ensure it doesn't go below the minimum brightness (10%)
        if self.brightness_level < 0.05:
            self.brightness_level = 0.9

        print(f"Setting brightness to {int(self.brightness_level * 100)}%.")
        self.bg_widget.setStyleSheet(
            f"background-color: rgba(0, 0, 0, {self.brightness_level});"
        )

    def take_screenshot(self):
        """Takes a screenshot of the current screen."""
        take_screenshot(self, self.media_folder)
        self.screenShotsTaken += 1
        self.header_label.setText(self.get_header_text())

    def process_screenshots(self):
        """Processes all screenshots from media folder and get the solved code from AI."""

        self.python_code = extract_highlighted_code(
            media_folder=self.media_folder,
            provider_name=self.provider_name,
            code_language=self.code_language,
        )
        self.code_label.setText(self.python_code)

        self.resize_window(0.6)
        self.resize_window(0.6, self.bg_widget)

    def clear_media_folder(self):
        """Clear the media folder of all files, then recreate it."""
        shutil.rmtree(self.media_folder, ignore_errors=True)
        os.makedirs(self.media_folder, exist_ok=True)
        print(f"Media folder cleared: {self.media_folder}")

    def reset(self):
        """Reset all application state to its default values.

        This includes clearing the media folder, resetting the code label text,
        and resizing the main window to its default size.
        """
        self.clear_media_folder()

        self.python_code = ""
        self.code_label.setText(self.python_code)

        self.screenShotsTaken = 0
        self.header_label.setText(self.get_header_text())

        self.resize_window()
        self.resize_window(widget=self.bg_widget)

        print("Reset to defaults.")

    def close_application(self):
        """Terminate the application when the Close button or shortcut is used."""
        self.clear_media_folder()
        print("Application closed.")
        QApplication.quit()
