# src/screenshot.py
"""This module provides a function for capturing a screenshot of the current screen."""

import time
import os


def take_screenshot(self, media_folder="media"):
    """Capture entire current screen"""
    if self.current_screen:
        timestamp = time.strftime("%Y%m%d-%H%M%S")
        filename = f"screenshot_{timestamp}.png"

        # Capture entire screen
        pixmap = self.current_screen.grabWindow(0)
        if not os.path.exists(media_folder):
            os.makedirs(media_folder)
        pixmap.save(os.path.join(media_folder, filename), "PNG")
        print(f"Screenshot saved as {filename}")
