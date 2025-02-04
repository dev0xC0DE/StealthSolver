# main.py
import sys
import os
from PyQt5.QtWidgets import QApplication
from src.start_ui import InputDialog  # Import InputDialog from start_ui.py

if hasattr(sys, "frozen"):
    sys.stdout = open(os.devnull, "w")

if __name__ == "__main__":
    app = QApplication(sys.argv)

    # Show the custom input dialog
    dialog = InputDialog()
    if dialog.exec_() == InputDialog.Accepted:  # If the user clicks OK
        screen_num, code_language, provider_name = dialog.get_values()

        # Get the media folder path
        media_folder = "media"

        # Launch the main application window with user inputs
        from src.gui import MainWindow

        main_window = MainWindow(
            screen_num=screen_num,
            media_folder=media_folder,
            code_language=code_language,
            provider_name=provider_name,
        )
        main_window.show()

    sys.exit(app.exec_())
