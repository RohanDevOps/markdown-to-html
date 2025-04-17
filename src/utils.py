import re

def sanitize_html(text: str) -> str:
    """Basic HTML sanitization"""
    return (text.replace('&', '&amp;')
               .replace('<', '&lt;')
               .replace('>', '&gt;')
               .replace('"', '&quot;'))

def escape_markdown(text: str) -> str:
    """Escape markdown special characters"""
    chars = ['\\', '`', '*', '_', '{', '}', '[', ']', '(', ')', '#', '+', '-', '.', '!']
    for char in chars:
        text = text.replace(char, f'\\{char}')
    return text