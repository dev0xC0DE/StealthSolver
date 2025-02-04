# src/highlighter.py
"""
This module contains the code highlighter functions.
"""

from pygments import highlight
from pygments.lexers import PythonLexer
from pygments.formatters import HtmlFormatter
from .chat import chat_completion


def highlight_python_code(code):
    """
    Highlight Python code and return as an HTML string with white text
    and a transparent background.
    """
    # Generate HTML with inline styles for syntax highlighting
    formatter = HtmlFormatter(
        noclasses=True,
        style="monokai",
        full=True,
        cssclass="code",
        prestyles="color: white; background-color: transparent; font-size: 14px; font-family: sans-serif; font-weight: medium;",
    )
    highlighted_code = highlight(code, PythonLexer(), formatter)
    return highlighted_code


def extract_highlighted_code(
    media_folder, provider_name="Blackbox", code_language="Python"
):
    """Processes all screenshots from media folder and get the solved code from AI."""

    prompt = f"These attached images contains a coding problem question. Give the solved {code_language} language solution code for the coding problem with the optimized least possible time and space complexity. Give only the complete code, don't give any other text or info, just give the {code_language} language complete code."

    python_code = chat_completion(
        prompt=prompt, provider_name=provider_name, media_folder=media_folder
    )

    return highlight_python_code(python_code)
