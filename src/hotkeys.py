# src/hotkeys.py
"""This module contains functions for setting up keyboard shortcuts for various actions."""

from PyQt5.QtWidgets import QShortcut
from PyQt5.QtGui import QKeySequence


def setup_hotkeys(window):
    """Assigns keyboard shortcuts to various actions."""
    QShortcut(QKeySequence("Ctrl+B"), window).activated.connect(
        window.toggle_brightness
    )
    QShortcut(QKeySequence("Ctrl+Up"), window).activated.connect(
        lambda: window.move_window(0, -0.05)
    )
    QShortcut(QKeySequence("Ctrl+Down"), window).activated.connect(
        lambda: window.move_window(0, 0.05)
    )
    QShortcut(QKeySequence("Ctrl+Left"), window).activated.connect(
        lambda: window.move_window(-0.05, 0)
    )
    QShortcut(QKeySequence("Ctrl+Right"), window).activated.connect(
        lambda: window.move_window(0.05, 0)
    )
    QShortcut(QKeySequence("Ctrl+H"), window).activated.connect(window.take_screenshot)
    QShortcut(QKeySequence("Ctrl+Return"), window).activated.connect(
        window.process_screenshots
    )
    QShortcut(QKeySequence("Ctrl+R"), window).activated.connect(window.reset)
    QShortcut(QKeySequence("Ctrl+Q"), window).activated.connect(
        window.close_application
    )
