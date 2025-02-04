# src/window_manager.py
"""This module contains functions for managing the main window."""

import ctypes
from ctypes import wintypes
from PyQt5.QtWidgets import QApplication

WDA_NONE = 0x0
WDA_EXCLUDEFROMCAPTURE = 0x11

user32 = ctypes.WinDLL("user32", use_last_error=True)
SetWindowDisplayAffinity = user32.SetWindowDisplayAffinity
SetWindowDisplayAffinity.argtypes = [wintypes.HWND, wintypes.DWORD]
SetWindowDisplayAffinity.restype = wintypes.BOOL


def set_window_exclude_from_capture(self):
    """Exclude window from being captured by screen recording/sharing tools."""
    hwnd = int(self.winId())

    result = SetWindowDisplayAffinity(hwnd, WDA_EXCLUDEFROMCAPTURE)
    if result:
        print("Window successfully excluded from screen capture.")
    else:
        print(f"Failed to exclude window. Error: {ctypes.get_last_error()}")


def move_to_target_screen(self):
    """Moves window to the specified screen."""
    screens = QApplication.screens()
    if 0 <= self.target_screen < len(screens):
        target_geom = screens[self.target_screen].geometry()
        print(f"Moving to screen {self.target_screen}: {target_geom}")
        self.move(target_geom.topLeft())
        self.screen_geometry = target_geom  # Update geometry for the selected screen
    else:
        print(f"Invalid screen number {self.target_screen}. Defaulting to main screen.")
        self.target_screen = 0  # Default to the main screen


def update_screen_info(self):
    """Update screen geometry based on current window position"""
    self.current_screen = QApplication.screenAt(self.geometry().center())
    if self.current_screen:
        self.screen_geometry = self.current_screen.geometry()
        print(f"Updated to screen: {self.screen_geometry}")


def resize_window(self, height_ratio=0, widget=None):
    """Resize a widget based on the main layout's preferred size, respecting the given height ratio."""
    widget = widget or self

    layout_size = self.code_label.sizeHint()

    # Calculate the new width and height based on the layout's size hint and add the offsets
    new_height = layout_size.height() + 180

    # Define the minimum size for the widget
    min_width = 700
    min_height = 230

    # If height_ratio is given, use it to determine the new height
    if height_ratio > 0:
        max_height = max(int(self.screen_geometry.height() * height_ratio), min_height)
        new_height = min(new_height, max_height)

    # Set the new geometry for the widget
    widget.setGeometry(widget.x(), widget.y(), min_width, new_height)


def move_window(self, dx_ratio, dy_ratio):
    """Move window in percentage-based increments."""
    new_x = self.x() + int(self.screen_geometry.width() * dx_ratio)
    new_y = self.y() + int(self.screen_geometry.height() * dy_ratio)

    # Keep within current screen bounds
    new_x = max(
        self.screen_geometry.left(),
        min(new_x, self.screen_geometry.right() - self.width()),
    )
    new_y = max(
        self.screen_geometry.top(),
        min(new_y, self.screen_geometry.bottom() - self.height()),
    )

    self.move(int(new_x), int(new_y))
