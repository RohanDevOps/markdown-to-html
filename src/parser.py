import re
from typing import List, Dict, Union


class MarkdownParser:
    def __init__(self, extensions=None):
        self.extensions = extensions or []
        self.rules = self._init_rules()

    def _init_rules(self) -> List[Dict]:
        """Initialize basic markdown parsing rules"""
        return [
            # Headers
            {'pattern': r'^#\s+(.*)', 'type': 'h1'},
            {'pattern': r'^##\s+(.*)', 'type': 'h2'},
            {'pattern': r'^###\s+(.*)', 'type': 'h3'},
            {'pattern': r'^####\s+(.*)', 'type': 'h4'},
            {'pattern': r'^#####\s+(.*)', 'type': 'h5'},
            {'pattern': r'^######\s+(.*)', 'type': 'h6'},

            # Lists
            {'pattern': r'^-\s+(.*)', 'type': 'ul'},
            {'pattern': r'^\*\s+(.*)', 'type': 'ul'},
            {'pattern': r'^\d+\.\s+(.*)', 'type': 'ol'},

            # Links and images
            {'pattern': r'!\[(.*?)\]\((.*?)\)', 'type': 'image'},
            {'pattern': r'\[(.*?)\]\((.*?)\)', 'type': 'link'},

            # Text formatting
            {'pattern': r'\*\*(.*?)\*\*', 'type': 'bold'},
            {'pattern': r'\*(.*?)\*', 'type': 'italic'},
            {'pattern': r'`(.*?)`', 'type': 'code'},

            # Paragraphs
            {'pattern': r'^(.*?)$', 'type': 'paragraph'},
        ]

    def parse(self, markdown_text: str) -> List[Dict]:
        """Parse markdown text into a structured document"""
        lines = markdown_text.split('\n')
        document = []

        for line in lines:
            if not line.strip():
                continue

            element = self._parse_line(line)
            if element:
                document.append(element)

        # Apply extensions
        for extension in self.extensions:
            if hasattr(extension, 'preprocess'):
                document = extension.preprocess(document)

        return document

    def _parse_line(self, line: str) -> Union[Dict, None]:
        """Parse a single line of markdown"""
        for rule in self.rules:
            match = re.match(rule['pattern'], line)
            if match:
                return {
                    'type': rule['type'],
                    'content': match.group(1).strip() if len(match.groups()) > 0 else line.strip()
                }
        return None